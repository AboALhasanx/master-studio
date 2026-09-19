/**
 * Master Studio Interactive Quiz Subsystem - Client Controller
 * 
 * Features:
 * - Dwell timer per question & total session timer
 * - Responsive 48px+ touch targets & Lucide SVG icons
 * - Metacognitive reflection chips & Lucky Guess toggle
 * - LocalStorage state recovery & Bookmarks management
 * - Telemetry sync (POST /api/quiz/submit) with UUID
 * - Light/Dark mode theming
 */

const I18N = {
    ar: {
        dir: 'rtl',
        indicator: 'AR',
        question: 'السؤال',
        prev: 'السابق',
        next: 'التالي',
        finish: 'إنهاء الكوز',
        tryAgain: 'إعادة المحاولة',
        sendStudio: 'إرسال إلى ماستر ستوديو',
        syncedStudio: 'تمت المزامنة بنجاح مع ماستر ستوديو',
        syncing: 'جاري إرسال البيانات والمزامنة...',
        luckyToggle: 'تخمين محظوظ / فلوك (جاوبت بالحظ)',
        whyPick: 'ما سبب اختيارك لهذا الجواب؟',
        rootCauseTitle: 'سبب الخطأ',
        reflectionPlaceholder: 'ملاحظة شخصية عن سبب الخطأ (مثل: نسيت القانون أو خلطت بالمصطلح)...',
        explanation: 'الشرح:',
        optionLetters: ['أ', 'ب', 'ج', 'د'],
        chips: {
            'Misread Question': 'قراءة غير دقيقة للسؤال',
            'Calculation Slip': 'خطأ في الحسابات',
            'Terminology Mix-up': 'خلط في المصطلحات',
            'Concept Gap': 'فجوة مفهومية في المادة'
        },
        correctLabel: 'الإجابة الصحيحة',
        yourChoiceLabel: 'إجابتك',
        bookmarksTitle: 'الأسئلة المحفوظة'
    },
    en: {
        dir: 'ltr',
        indicator: 'EN',
        question: 'Question',
        prev: 'Previous',
        next: 'Next',
        finish: 'Finish Quiz',
        tryAgain: 'Try Again',
        sendStudio: 'Send to Master Studio',
        syncedStudio: 'Performance metrics synced with Master Studio.',
        syncing: 'Syncing telemetry...',
        luckyToggle: 'Lucky Guess / WOW (I guessed this without being sure)',
        whyPick: 'Why did you pick this?',
        rootCauseTitle: 'Root Cause',
        reflectionPlaceholder: 'Reflection notes (e.g. key formula or condition forgotten)...',
        explanation: 'Explanation:',
        optionLetters: ['A', 'B', 'C', 'D'],
        chips: {
            'Misread Question': 'Misread Question',
            'Calculation Slip': 'Calculation Slip',
            'Terminology Mix-up': 'Terminology Mix-up',
            'Concept Gap': 'Concept Gap'
        },
        correctLabel: 'Correct Answer',
        yourChoiceLabel: 'Your Choice',
        bookmarksTitle: 'Saved Questions'
    }
};
const SUBJECT_MAP = {
    '01_Cyber_Security': 'الأمن السيبراني',
    '02_English_Language': 'اللغة الإنجليزية',
    '03_Data_Mining': 'تنقيب البيانات',
    '04_Advanced_Software_Eng': 'هندسة البرمجيات المتقدمة',
    '05_Soft_Computing': 'الحوسبة المرنة',
    '06_Artificial_Intelligence': 'الذكاء الاصطناعي'
};
class SoundManager {
    constructor() {
        this.muted = localStorage.getItem('master_studio_muted') === 'true';
        this.sounds = {
            correct: new Audio('/static/sounds/correct.mp3'),
            wrong: new Audio('/static/sounds/wrong.mp3'),
            completed: new Audio('/static/sounds/completed.mp3')
        };

        // Preload to eliminate delay and start gaps
        Object.values(this.sounds).forEach(audio => {
            audio.preload = 'auto';
            audio.load();
        });
    }

    play(name) {
        if (this.muted) return;
        const audio = this.sounds[name];
        if (!audio) return;
        try {
            audio.currentTime = 0;
            const playPromise = audio.play();
            if (playPromise !== undefined) {
                playPromise.catch(() => {});
            }
        } catch (_) {}
    }

    toggleMute() {
        this.muted = !this.muted;
        localStorage.setItem('master_studio_muted', this.muted ? 'true' : 'false');
        return this.muted;
    }
}

class QuizApp {
    constructor() {
        this.soundManager = new SoundManager();
        this.lang = localStorage.getItem('master_studio_lang') || 'ar';
        this.root = document.getElementById('quiz-root');
        
        // Configuration from dataset or URL query params
        const urlParams = new URLSearchParams(window.location.search);
        this.subjectId = this.root?.dataset?.subjectId || urlParams.get('subject') || '';
        this.quizId = this.root?.dataset?.quizId || urlParams.get('quiz') || '';
        this.directMode = this.root?.dataset?.directMode === 'true' || urlParams.get('direct') === 'true';

        // Core State
        this.quizData = null;
        this.currentIndex = 0;
        this.answers = {};           // { [qIndex]: selectedOptionIndex }
        this.dwellTimes = {};        // { [qIndex]: totalSecondsElapsed }
        this.dwellStartTime = Date.now();
        this.sessionStartTime = Date.now();
        this.sessionDuration = 0;
        this.timerInterval = null;
        
        // Metacognitive & Telemetry State
        this.reflections = {};       // { [qIndex]: { reason: string, notes: string } }
        this.luckyGuesses = {};      // { [qIndex]: boolean }
        this.answerTimestamps = {};  // { [qIndex]: epochMs when the option was selected }
        this.bookmarks = new Set();  // Set of question IDs (e.g. "q1")
        this.submissionUUID = this.generateUUID();
        this.isSubmitted = false;
        this.activeFilter = 'all';

        // DOM Element References
        this.dom = {
            // Header
            quizTitle: document.getElementById('quiz-title'),
            quizSubtitle: document.getElementById('quiz-subtitle'),
            btnExit: document.getElementById('btn-exit'),
            btnBookmarksToggle: document.getElementById('btn-toggle-bookmarks'),
            btnLangToggle: document.getElementById('btn-lang-toggle'),
            langIndicator: document.getElementById('lang-indicator'),
            btnSoundToggle: document.getElementById('btn-sound-toggle'),
            soundIcon: document.getElementById('sound-icon'),
            btnThemeToggle: document.getElementById('btn-theme-toggle'),
            themeIcon: document.getElementById('theme-icon'),
            bookmarksBadge: document.getElementById('bookmarks-badge'),
            progressBarFill: document.getElementById('progress-bar-fill'),
            questionIndexLabel: document.getElementById('question-index-label'),
            questionTotalLabel: document.getElementById('question-total-label'),
            dwellTimer: document.getElementById('dwell-timer'),
            sessionTimer: document.getElementById('session-timer'),

            // Views
            quizLoading: document.getElementById('quiz-loading'),
            quizError: document.getElementById('quiz-error'),
            errorMessage: document.getElementById('error-message'),
            btnRetryLoad: document.getElementById('btn-retry-load'),
            quizView: document.getElementById('quiz-view'),
            resultsView: document.getElementById('results-view'),

            // Question Card
            btnBookmarkQuestion: document.getElementById('btn-bookmark-question'),
            bookmarkCardIcon: document.getElementById('bookmark-card-icon'),
            questionText: document.getElementById('question-text'),
            optionsContainer: document.getElementById('options-container'),

            // Navigation
            btnPrev: document.getElementById('btn-prev'),
            btnNext: document.getElementById('btn-next'),
            liveFeedbackBox: document.getElementById('live-feedback-box'),
            liveFeedbackBanner: document.getElementById('live-feedback-banner'),
            liveFeedbackIcon: document.getElementById('live-feedback-icon'),
            liveFeedbackText: document.getElementById('live-feedback-text'),
            liveExplanationText: document.getElementById('live-explanation-text'),
            nextBtnText: document.getElementById('next-btn-text'),
            nextBtnIcon: document.getElementById('next-btn-icon'),

            // Results
            scorePercentage: document.getElementById('score-percentage'),
            scoreFraction: document.getElementById('score-fraction'),
            scoreBadge: document.getElementById('score-badge'),
            scoreBadgeText: document.getElementById('score-badge-text'),
            scoreBadgeIcon: document.getElementById('score-badge-icon'),
            statCorrect: document.getElementById('stat-correct'),
            statWrong: document.getElementById('stat-wrong'),
            statAvgDwell: document.getElementById('stat-avg-dwell'),
            statLucky: document.getElementById('stat-lucky'),
            btnRetryQuiz: document.getElementById('btn-retry-quiz'),
            btnSubmitTelemetry: document.getElementById('btn-submit-telemetry'),
            syncStatusBanner: document.getElementById('sync-status-banner'),
            reviewCardsList: document.getElementById('review-cards-list'),
            filterCountAll: document.getElementById('filter-count-all'),
            filterCountWrong: document.getElementById('filter-count-wrong'),
            filterCountCorrect: document.getElementById('filter-count-correct'),
            filterCountLucky: document.getElementById('filter-count-lucky'),

            // Drawers & Overlays
            drawerOverlay: document.getElementById('drawer-overlay'),
            bookmarksDrawer: document.getElementById('bookmarks-drawer'),
            btnCloseBookmarks: document.getElementById('btn-close-bookmarks'),
            bookmarksList: document.getElementById('bookmarks-list'),
            bookmarksEmpty: document.getElementById('bookmarks-empty')
        };

        this.init();
    }

    /**
     * Initialize App, Events, Theme, and Load Quiz
     */
    async init() {
        this.initLanguage();
        this.initTheme();
        this.updateSoundIcon();
        this.initEvents();
        this.flushOfflineQueue();
        await this.loadBookmarks();
        await this.loadQuiz();
        this.refreshLucideIcons();
    }

    /**
     * Safe UUID Generator
     */
    generateUUID() {
        if (typeof crypto !== 'undefined' && crypto.randomUUID) {
            return crypto.randomUUID();
        }
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
            const r = Math.random() * 16 | 0;
            const v = c === 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    /**
     * Theme Initialization (Dark mode default)
     */
    initTheme() {
        const savedTheme = localStorage.getItem('master_studio_theme') || 'dark';
        document.documentElement.setAttribute('data-theme', savedTheme);
        this.updateThemeIcon(savedTheme);
    }

    toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', nextTheme);
        localStorage.setItem('master_studio_theme', nextTheme);
        this.updateThemeIcon(nextTheme);
    }

    updateThemeIcon(theme) {
        if (this.dom.themeIcon) {
            this.dom.themeIcon.setAttribute('data-lucide', theme === 'dark' ? 'moon' : 'sun');
            this.refreshLucideIcons();
        }
    }
    toggleSound() {
        const isMuted = this.soundManager.toggleMute();
        this.updateSoundIcon();
        this.showTemporaryToast(isMuted ? 'تم كتم الصوت' : 'تم تشغيل الصوت');
    }

    updateSoundIcon() {
        if (this.dom.btnSoundToggle) {
            const isMuted = this.soundManager.muted;
            this.dom.btnSoundToggle.innerHTML = `<i data-lucide="${isMuted ? 'volume-x' : 'volume-2'}"></i>`;
            this.dom.btnSoundToggle.setAttribute('title', isMuted ? 'تشغيل الصوت' : 'كتم الصوت');
            this.refreshLucideIcons();
        }
    }

    /**
     * Language & BiDi Initialization
     * WebUI shell is 100% Arabic always (dir="rtl").
     * Language toggle controls ONLY the question card (EN / AR).
     */
    initLanguage() {
        this.cardLang = localStorage.getItem('master_studio_card_lang') || 'en';
        this.applyLanguage();
    }

    toggleLanguage() {
        this.cardLang = this.cardLang === 'en' ? 'ar' : 'en';
        localStorage.setItem('master_studio_card_lang', this.cardLang);
        this.applyLanguage();
        if (this.dom.quizView && !this.dom.quizView.classList.contains('hidden')) {
            this.renderQuestion(this.currentIndex);
        } else if (this.dom.resultsView && !this.dom.resultsView.classList.contains('hidden')) {
            this.renderResults();
        }
    }

    applyLanguage() {
        // Entire WebUI is ALWAYS Arabic & RTL
        document.documentElement.setAttribute('dir', 'rtl');
        document.documentElement.setAttribute('lang', 'ar');
        if (this.dom.langIndicator) {
            this.dom.langIndicator.textContent = this.cardLang.toUpperCase();
        }
        const card = document.getElementById('question-card');
        if (card) {
            card.setAttribute('data-card-lang', this.cardLang);
        }
    }
    /**
     * Bind UI Event Listeners
     */
    initEvents() {
        // Theme & Language & Sound Header
        this.dom.btnSoundToggle?.addEventListener('click', () => this.toggleSound());
        this.dom.btnLangToggle?.addEventListener('click', () => this.toggleLanguage());
        this.dom.btnThemeToggle?.addEventListener('click', () => this.toggleTheme());
        this.dom.btnExit?.addEventListener('click', () => this.handleExit());
        // Question Navigation
        this.dom.btnPrev?.addEventListener('click', () => this.prevQuestion());
        this.dom.btnNext?.addEventListener('click', () => this.nextQuestion());
        this.dom.btnBookmarkQuestion?.addEventListener('click', () => this.toggleCurrentBookmark());

        // Results Actions
        this.dom.btnRetryQuiz?.addEventListener('click', () => this.restartQuiz());
        this.dom.btnSubmitTelemetry?.addEventListener('click', () => this.submitTelemetry());
        this.dom.btnRetryLoad?.addEventListener('click', () => this.loadQuiz());

        // Drawers
        this.dom.btnBookmarksToggle?.addEventListener('click', () => this.openDrawer(this.dom.bookmarksDrawer));
        this.dom.btnCloseBookmarks?.addEventListener('click', () => this.closeDrawer(this.dom.bookmarksDrawer));
        this.dom.drawerOverlay?.addEventListener('click', () => this.closeAllDrawers());

        // Filter Pills on Results Page
        document.querySelectorAll('.filter-pill').forEach(pill => {
            pill.addEventListener('click', (e) => {
                const filter = e.currentTarget.dataset.filter;
                this.setReviewFilter(filter);
            });
        });

        // Keyboard Shortcuts
        document.addEventListener('keydown', (e) => this.handleKeyboardShortcuts(e));
    }

    handleKeyboardShortcuts(e) {
        // Disable keyboard shortcuts when modal or typing in text input
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

        if (this.dom.quizView && !this.dom.quizView.classList.contains('hidden')) {
            if (e.key === 'ArrowRight' || e.key === 'Enter') {
                this.nextQuestion();
            } else if (e.key === 'ArrowLeft') {
                this.prevQuestion();
            } else if (['1', '2', '3', '4'].includes(e.key)) {
                this.selectOption(parseInt(e.key, 10) - 1);
            } else if (['a', 'b', 'c', 'd'].includes(e.key.toLowerCase())) {
                const map = { a: 0, b: 1, c: 2, d: 3 };
                this.selectOption(map[e.key.toLowerCase()]);
            } else if (e.key.toLowerCase() === 'b') {
                this.toggleCurrentBookmark();
            }
        }
    }

    handleExit() {
        if (window.history.length > 1) {
            window.history.back();
        } else {
            window.location.href = '/';
        }
    }

    /**
     * Load Quiz Data from Server or Fallback
     */
    async loadQuiz() {
        this.showState('loading');

        try {
            if (this.subjectId && this.quizId) {
                const response = await fetch(`/api/quiz/${encodeURIComponent(this.subjectId)}/${encodeURIComponent(this.quizId)}`);
                if (!response.ok) {
                    throw new Error(`Failed to load quiz (${response.status} ${response.statusText})`);
                }
                this.quizData = await response.json();
            } else {
                // Fallback / Demonstration Sample Quiz if no parameters provided
                this.quizData = this.getFallbackQuizData();
            }

            if (!this.quizData || !this.quizData.questions || this.quizData.questions.length === 0) {
                throw new Error('Quiz contains no questions.');
            }

            this.setupQuizSession();
        } catch (error) {
            console.error('Quiz loading error:', error);
            if (this.dom.errorMessage) {
                this.dom.errorMessage.textContent = error.message || 'Unable to connect to quiz server.';
            }
            this.showState('error');
        }
    }

    setupQuizSession() {
        this.currentIndex = 0;
        this.answers = {};
        this.dwellTimes = {};
        this.reflections = {};
        this.luckyGuesses = {};
        this.answerTimestamps = {};
        this.isSubmitted = false;
        this.submissionUUID = this.generateUUID();

        // Initialize timers
        this.sessionStartTime = Date.now();
        this.dwellStartTime = Date.now();
        
        // Normalize Subject ID & Questions Data
        const subjectDisplay = this.quizData.subject || this.quizData.subject_id || this.subjectId || '';
        this.quizData.subject_id = subjectDisplay;

        if (Array.isArray(this.quizData.questions)) {
            this.quizData.questions.forEach((q, idx) => {
                if (!q) return;

                // Ensure question id
                if (!q.id) {
                    q.id = `q_${idx + 1}`;
                }

                let optionsArray = [];
                let optionKeys = [];

                if (Array.isArray(q.options)) {
                    optionsArray = q.options;
                    optionKeys = ['A', 'B', 'C', 'D'].slice(0, q.options.length);
                } else if (q.options && typeof q.options === 'object') {
                    optionKeys = Object.keys(q.options);
                    optionsArray = Object.values(q.options);
                } else {
                    optionsArray = [];
                    optionKeys = [];
                }

                // Resolve correct answer index (0-3) and correct letter ('A'-'D')
                let correctIdx = 0;
                let correctLetter = 'A';

                if (q.answer !== undefined && q.answer !== null) {
                    if (typeof q.answer === 'string') {
                        const cleanAns = q.answer.trim().toUpperCase();
                        const keyIdx = optionKeys.indexOf(cleanAns);
                        if (keyIdx !== -1) {
                            correctIdx = keyIdx;
                            correctLetter = cleanAns;
                        } else {
                            const parsed = parseInt(cleanAns, 10);
                            if (!isNaN(parsed) && parsed >= 0 && parsed < optionsArray.length) {
                                correctIdx = parsed;
                                correctLetter = optionKeys[parsed] || ['A', 'B', 'C', 'D'][parsed] || 'A';
                            } else {
                                correctIdx = 0;
                                correctLetter = optionKeys[0] || 'A';
                            }
                        }
                    } else if (typeof q.answer === 'number') {
                        correctIdx = q.answer;
                        correctLetter = optionKeys[q.answer] || ['A', 'B', 'C', 'D'][q.answer] || 'A';
                    }
                } else if (q.correct !== undefined && q.correct !== null) {
                    if (typeof q.correct === 'number') {
                        correctIdx = q.correct;
                        correctLetter = optionKeys[q.correct] || ['A', 'B', 'C', 'D'][q.correct] || 'A';
                    } else if (typeof q.correct === 'string') {
                        const cleanCorr = q.correct.trim().toUpperCase();
                        const keyIdx = optionKeys.indexOf(cleanCorr);
                        if (keyIdx !== -1) {
                            correctIdx = keyIdx;
                            correctLetter = cleanCorr;
                        } else {
                            const parsed = parseInt(cleanCorr, 10);
                            if (!isNaN(parsed) && parsed >= 0 && parsed < optionsArray.length) {
                                correctIdx = parsed;
                                correctLetter = optionKeys[parsed] || ['A', 'B', 'C', 'D'][parsed] || 'A';
                            } else {
                                correctIdx = 0;
                                correctLetter = optionKeys[0] || 'A';
                            }
                        }
                    }
                } else {
                    correctIdx = 0;
                    correctLetter = optionKeys[0] || 'A';
                }

                q.options = optionsArray;
                q.optionKeys = optionKeys;
                q.correct = correctIdx;
                q.correctLetter = correctLetter;
            });
        }

        // Update Header Titles
        const rawSubj = this.quizData.subject || this.quizData.subject_id || this.subjectId || '';
        const cleanSubj = SUBJECT_MAP[rawSubj] || rawSubj.replace(/^\d+_/, '').replace(/_/g, ' ');

        if (this.dom.quizTitle) {
            this.dom.quizTitle.textContent = this.quizData.topic || 'كوز تفاعلي';
        }
        if (this.dom.quizSubtitle) {
            this.dom.quizSubtitle.textContent = cleanSubj;
        }

        // Start 1s timer loop
        this.startTimerLoop();

        // Show Active Quiz
        this.showState('quiz');
        this.renderQuestion(0);
    }

    /**
     * Timer Management
     */
    startTimerLoop() {
        if (this.timerInterval) clearInterval(this.timerInterval);

        this.timerInterval = setInterval(() => {
            const now = Date.now();
            
            // Total Session Duration
            this.sessionDuration = Math.floor((now - this.sessionStartTime) / 1000);
            if (this.dom.sessionTimer) {
                this.dom.sessionTimer.textContent = this.formatTime(this.sessionDuration);
            }

            // Current Question Dwell Time
            const currentQuestionElapsed = (this.dwellTimes[this.currentIndex] || 0) + Math.floor((now - this.dwellStartTime) / 1000);
            if (this.dom.dwellTimer) {
                this.dom.dwellTimer.textContent = this.formatTime(currentQuestionElapsed);
            }
        }, 1000);
    }

    flushCurrentDwellTime() {
        const now = Date.now();
        const deltaSeconds = (now - this.dwellStartTime) / 1000;
        this.dwellTimes[this.currentIndex] = (this.dwellTimes[this.currentIndex] || 0) + deltaSeconds;
        this.dwellStartTime = Date.now();
    }

    formatTime(totalSeconds) {
        const mins = Math.floor(totalSeconds / 60);
        const secs = Math.floor(totalSeconds % 60);
        return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }

    /**
     * Render Active Question
     */
    renderQuestion(index) {
        if (!this.quizData || !this.quizData.questions[index]) return;

        window.scrollTo({ top: 0, behavior: 'smooth' });

        this.currentIndex = index;
        const q = this.quizData.questions[index];
        const total = this.quizData.questions.length;

        // Update Progress Bar & Counter
        const progressPercent = Math.round(((index + 1) / total) * 100);
        if (this.dom.progressBarFill) {
            this.dom.progressBarFill.style.width = `${progressPercent}%`;
        }
        if (this.dom.questionIndexLabel) {
            this.dom.questionIndexLabel.textContent = (index + 1).toString();
        }
        if (this.dom.questionTotalLabel) {
            this.dom.questionTotalLabel.textContent = total.toString();
        }

        // Update Bookmark Button
        const isBookmarked = this.bookmarks.has(q.id || `q_${index}`);
        if (this.dom.btnBookmarkQuestion) {
            this.dom.btnBookmarkQuestion.classList.toggle('bookmarked', isBookmarked);
        }

        const isCardAr = this.cardLang === 'ar';
        const cardOptionLetters = isCardAr ? ['أ', 'ب', 'ج', 'د'] : ['A', 'B', 'C', 'D'];

        // Dynamic bilingual question text
        const qText = isCardAr ? (q.text || q.question_ar || q.question) : (q.text_en || q.question_en || q.question);
        if (this.dom.questionText) {
            this.dom.questionText.textContent = qText;
            this.dom.questionText.style.direction = isCardAr ? 'rtl' : 'ltr';
            this.dom.questionText.style.textAlign = isCardAr ? 'right' : 'left';
        }

        // Dynamic bilingual options
        let qOptions = q.options || [];
        if (isCardAr && Array.isArray(q.options_ar) && q.options_ar.length > 0) {
            qOptions = q.options_ar;
        } else if (!isCardAr && Array.isArray(q.options_en) && q.options_en.length > 0) {
            qOptions = q.options_en;
        }

        const userAns = this.answers[index];
        const isAnswered = userAns !== undefined;

        if (this.dom.optionsContainer) {
            this.dom.optionsContainer.innerHTML = '';
            if (isAnswered) {
                this.dom.optionsContainer.classList.add('locked');
            } else {
                this.dom.optionsContainer.classList.remove('locked');
            }

            const optionKeys = q.optionKeys || ['A', 'B', 'C', 'D'];

            qOptions.forEach((optText, optIdx) => {
                const isSelected = userAns === optIdx;
                const isCorrectOpt = q.correct === optIdx;

                const tile = document.createElement('button');
                let tileClass = 'option-tile';
                if (isAnswered) {
                    if (isSelected) {
                        tileClass += (optIdx === q.correct) ? ' correct-answer' : ' user-wrong';
                    } else if (isCorrectOpt) {
                        tileClass += ' correct-answer';
                    }
                }

                tile.className = tileClass;
                tile.setAttribute('role', 'radio');
                tile.setAttribute('aria-checked', isSelected ? 'true' : 'false');
                tile.setAttribute('data-option-index', optIdx);
                tile.style.direction = isCardAr ? 'rtl' : 'ltr';
                tile.style.textAlign = isCardAr ? 'right' : 'left';

                const letter = document.createElement('div');
                letter.className = 'option-letter';
                letter.textContent = cardOptionLetters[optIdx] || optionKeys[optIdx] || `${optIdx + 1}`;

                const content = document.createElement('div');
                content.className = 'option-content';
                content.textContent = optText;

                tile.appendChild(letter);
                tile.appendChild(content);

                tile.addEventListener('click', () => this.selectOption(optIdx));
                this.dom.optionsContainer.appendChild(tile);
            });
        }

        // Sleek explanation card (ONLY shown for wrong answers)
        if (this.dom.liveFeedbackBox) {
            if (isAnswered && userAns !== q.correct) {
                this.dom.liveFeedbackBox.classList.remove('hidden');
                if (this.dom.liveExplanationText) {
                    this.dom.liveExplanationText.textContent = q.explanation || '';
                }
            } else {
                this.dom.liveFeedbackBox.classList.add('hidden');
            }
        }

        // Update Navigation Buttons
        if (this.dom.btnPrev) {
            this.dom.btnPrev.disabled = index === 0;
        }
        if (this.dom.nextBtnText && this.dom.nextBtnIcon) {
            if (index === total - 1) {
                this.dom.nextBtnText.textContent = 'إنهاء الكوز';
                this.dom.nextBtnIcon.setAttribute('data-lucide', 'check-circle');
            } else {
                this.dom.nextBtnText.textContent = 'التالي';
                this.dom.nextBtnIcon.setAttribute('data-lucide', 'arrow-left');
            }
        }

        this.refreshLucideIcons();
    }

    selectOption(optionIndex) {
        if (this.answers[this.currentIndex] !== undefined) return; // Locked: no changing answers!

        this.answers[this.currentIndex] = optionIndex;
        this.answerTimestamps[this.currentIndex] = Date.now();
        const q = this.quizData?.questions[this.currentIndex];
        if (!q) return;

        const isCorrect = optionIndex === q.correct;
        const tiles = this.dom.optionsContainer?.querySelectorAll('.option-tile');

        // Lock options grid
        this.dom.optionsContainer?.classList.add('locked');

        // Instant visual feedback
        if (isCorrect) {
            tiles?.[optionIndex]?.classList.add('correct-answer');
            this.soundManager.play('correct');

            // Correct Answer: Keep momentum, DO NOT show explanation
            if (this.dom.liveFeedbackBox) {
                this.dom.liveFeedbackBox.classList.add('hidden');
            }
        } else {
            tiles?.[optionIndex]?.classList.add('user-wrong');
            if (q.correct !== undefined && tiles?.[q.correct]) {
                tiles[q.correct].classList.add('correct-answer');
            }
            this.soundManager.play('wrong');

            // Wrong Answer: Show sleek explanation card
            if (this.dom.liveFeedbackBox) {
                this.dom.liveFeedbackBox.classList.remove('hidden');
                if (this.dom.liveExplanationText) {
                    this.dom.liveExplanationText.textContent = q.explanation || '';
                }
                this.refreshLucideIcons();
                setTimeout(() => {
                    this.dom.liveFeedbackBox?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }, 100);
            }
        }
    }

    /**
     * Question Navigation Handlers
     */
    prevQuestion() {
        if (this.currentIndex > 0) {
            this.flushCurrentDwellTime();
            this.renderQuestion(this.currentIndex - 1);
        }
    }

    nextQuestion() {
        this.flushCurrentDwellTime();
        if (this.currentIndex < this.quizData.questions.length - 1) {
            this.renderQuestion(this.currentIndex + 1);
        } else {
            this.finishQuiz();
        }
    }

    jumpToQuestion(index) {
        if (index >= 0 && index < this.quizData.questions.length) {
            this.flushCurrentDwellTime();
            this.closeAllDrawers();
            this.showState('quiz');
            this.renderQuestion(index);
        }
    }

    /**
     * Quiz Completion & Scoring
     */
    finishQuiz() {
        if (this.timerInterval) clearInterval(this.timerInterval);
        this.flushCurrentDwellTime();

        const questions = this.quizData.questions;
        let correctCount = 0;
        let wrongCount = 0;
        let totalDwell = 0;

        questions.forEach((q, idx) => {
            const userAns = this.answers[idx];
            const isCorrect = userAns !== undefined && userAns === q.correct;
            if (isCorrect) correctCount++;
            else wrongCount++;

            totalDwell += (this.dwellTimes[idx] || 0);

            // Initialize default reflection state for wrong answers if not set
            if (!isCorrect && !this.reflections[idx]) {
                this.reflections[idx] = { reason: 'Concept Gap', notes: '' };
            }
        });

        const total = questions.length;
        const percentage = Math.round((correctCount / total) * 100);
        const avgDwell = total > 0 ? (totalDwell / total).toFixed(1) : 0;
        const isPassed = percentage >= 75;

        this.renderResults();

        this.soundManager.play('completed');
    }

    /**
     * Render the results view from current answers (stats + review cards).
     * Safe to re-run — e.g. when the card-language toggle flips mid-review.
     */
    renderResults() {
        const questions = this.quizData.questions;
        let correctCount = 0;
        let wrongCount = 0;
        let totalDwell = 0;

        questions.forEach((q, idx) => {
            const userAns = this.answers[idx];
            if (userAns !== undefined && userAns === q.correct) correctCount++;
            else wrongCount++;
            totalDwell += (this.dwellTimes[idx] || 0);
        });

        const total = questions.length;
        const percentage = total > 0 ? Math.round((correctCount / total) * 100) : 0;
        const avgDwell = total > 0 ? (totalDwell / total).toFixed(1) : 0;
        const isPassed = percentage >= 75;

        // Update Overview Cards
        if (this.dom.scorePercentage) this.dom.scorePercentage.textContent = `${percentage}%`;
        if (this.dom.scoreFraction) this.dom.scoreFraction.textContent = `${correctCount} / ${total}`;

        if (this.dom.scoreBadge) {
            this.dom.scoreBadge.className = `score-status-badge ${isPassed ? 'pass' : 'fail'}`;
        }
        if (this.dom.scoreBadgeText) {
            this.dom.scoreBadgeText.textContent = isPassed ? (this.lang === 'ar' ? 'ناجح' : 'Pass') : (this.lang === 'ar' ? 'بحاجة لمراجعة' : 'Needs Review');
        }
        if (this.dom.scoreBadgeIcon) {
            this.dom.scoreBadgeIcon.setAttribute('data-lucide', isPassed ? 'check-circle-2' : 'alert-triangle');
        }

        if (this.dom.statCorrect) this.dom.statCorrect.textContent = correctCount.toString();
        if (this.dom.statWrong) this.dom.statWrong.textContent = wrongCount.toString();
        if (this.dom.statAvgDwell) this.dom.statAvgDwell.textContent = `${avgDwell}${this.lang === 'ar' ? ' ث' : 's'}`;
        if (this.dom.statLucky) {
            const luckyCount = Object.values(this.luckyGuesses).filter(Boolean).length;
            this.dom.statLucky.textContent = luckyCount.toString();
        }

        // Render Detailed Review Cards
        this.renderReviewCards();
        this.updateFilterCounts();

        // Switch View
        this.showState('results');
        this.refreshLucideIcons();
    }

    /**
     * Render Metacognitive Review & Reflection Cards
     */
    renderReviewCards() {
        if (!this.dom.reviewCardsList || !this.quizData) return;
        this.dom.reviewCardsList.innerHTML = '';

        const questions = this.quizData.questions;
        const t = I18N[this.lang] || I18N.ar;
        const reflectionOptions = [
            'Misread Question',
            'Calculation Slip',
            'Terminology Mix-up',
            'Concept Gap'
        ];
        questions.forEach((q, idx) => {
            const userAns = this.answers[idx];
            const isCorrect = userAns !== undefined && userAns === q.correct;
            const isLucky = !!this.luckyGuesses[idx];
            const dwellSec = Math.round(this.dwellTimes[idx] || 0);

            // Check Filter
            if (this.activeFilter === 'wrong' && isCorrect) return;
            if (this.activeFilter === 'correct' && !isCorrect) return;
            if (this.activeFilter === 'lucky' && !isLucky) return;

            const card = document.createElement('div');
            card.className = `review-card ${isCorrect ? 'correct-border' : 'wrong-border'}`;
            card.setAttribute('data-q-index', idx);

            // Bilingual content — mirrors the live question-card language
            const isAr = this.cardLang === 'ar';
            const qText = isAr ? (q.text || q.question_ar || q.question) : (q.text_en || q.question_en || q.question);
            const qOptions = isAr
                ? (Array.isArray(q.options_ar) && q.options_ar.length > 0 ? q.options_ar : (q.options || []))
                : (Array.isArray(q.options_en) && q.options_en.length > 0 ? q.options_en : (q.options || []));
            const optionLetters = isAr ? ['أ', 'ب', 'ج', 'د'] : ['A', 'B', 'C', 'D'];

            // Review Card Header
            const header = document.createElement('div');
            header.className = 'review-card-header';
            const statusLabel = isCorrect ? (isAr ? 'صحيحة' : 'Correct') : (isAr ? 'خاطئة' : 'Wrong');
            header.innerHTML = `
                <div class="review-q-meta">
                    <span class="review-q-num">${t.question} ${idx + 1}</span>
                    <span class="review-status-tag ${isCorrect ? 'correct' : 'wrong'}">
                        <i data-lucide="${isCorrect ? 'check' : 'x'}"></i>
                        <span>${statusLabel}</span>
                    </span>
                </div>
                <span class="review-dwell-tag">
                    <i data-lucide="clock"></i>
                    <span>${dwellSec}s</span>
                </span>
            `;
            card.appendChild(header);

            // Question Stem (direction follows the text language)
            const qStem = document.createElement('p');
            qStem.className = 'review-question-text';
            qStem.textContent = qText;
            qStem.style.direction = isAr ? 'rtl' : 'ltr';
            qStem.style.textAlign = isAr ? 'right' : 'left';
            card.appendChild(qStem);

            // Options — show ONLY your pick and the correct answer (zero noise)
            const optionsList = document.createElement('div');
            optionsList.className = 'review-options-list';
            const optionKeys = q.optionKeys || ['A', 'B', 'C', 'D'];

            qOptions.forEach((optText, optIdx) => {
                const isUserChoice = userAns === optIdx;
                const isCorrectOption = q.correct === optIdx;

                // Skip distractors entirely
                if (!isUserChoice && !isCorrectOption) return;

                let optClass = 'review-option-item';
                if (isUserChoice && !isCorrect) {
                    optClass += ' user-wrong';
                } else if (isCorrectOption) {
                    optClass += ' correct-answer';
                }

                const optItem = document.createElement('div');
                optItem.className = optClass;
                optItem.style.direction = isAr ? 'rtl' : 'ltr';
                optItem.style.textAlign = isAr ? 'right' : 'left';
                optItem.innerHTML = `
                    <span class="review-option-indicator">${optionLetters[optIdx] || optionKeys[optIdx]}</span>
                    <span class="review-option-text">${this.escapeHtml(optText)}</span>
                `;
                optionsList.appendChild(optItem);
            });
            card.appendChild(optionsList);

            // Explanation Box
            if (q.explanation) {
                const expBox = document.createElement('div');
                expBox.className = 'review-explanation-box';
                expBox.innerHTML = `
                    <strong>${t.explanation}</strong>
                    <span>${q.explanation}</span>
                `;
                card.appendChild(expBox);
            }

            // Metacognitive Section
            if (!isCorrect) {
                // Wrong Answer: compact reason picker + optional note
                const reflectionBox = document.createElement('div');
                reflectionBox.className = 'reflection-box';

                const currentReason = this.reflections[idx]?.reason || 'Concept Gap';
                const currentNotes = this.reflections[idx]?.notes || '';

                reflectionBox.innerHTML = `
                    <label class="reflection-select-wrap">
                        <select class="reflection-select" aria-label="${t.rootCauseTitle}">
                            ${reflectionOptions.map(reason => `
                                <option value="${reason}" ${currentReason === reason ? 'selected' : ''}>${t.chips[reason] || reason}</option>
                            `).join('')}
                        </select>
                        <i data-lucide="chevron-down" class="reflection-caret"></i>
                    </label>
                    <textarea class="reflection-notes-input" rows="1" placeholder="${t.reflectionPlaceholder}">${this.escapeHtml(currentNotes)}</textarea>
                `;

                // Handle Reason selection (native picker — mobile bottom-sheet)
                const reasonSelect = reflectionBox.querySelector('.reflection-select');
                reasonSelect?.addEventListener('change', (e) => {
                    if (!this.reflections[idx]) this.reflections[idx] = { reason: 'Concept Gap', notes: '' };
                    this.reflections[idx].reason = e.target.value;
                });

                // Handle Notes input
                const noteInput = reflectionBox.querySelector('.reflection-notes-input');
                noteInput?.addEventListener('input', (e) => {
                    if (!this.reflections[idx]) this.reflections[idx] = { reason: 'Concept Gap', notes: '' };
                    this.reflections[idx].notes = e.target.value;
                });

                card.appendChild(reflectionBox);

            } else {
                // Correct Answer: Lucky Guess Toggle Switch
                const luckyBox = document.createElement('div');
                luckyBox.className = 'lucky-guess-box';
                luckyBox.innerHTML = `
                    <label class="lucky-guess-label" for="lucky-switch-${idx}">
                        <i data-lucide="zap" class="lucky-guess-icon"></i>
                        <span>${t.luckyToggle}</span>
                    </label>
                    <label class="switch">
                        <input type="checkbox" id="lucky-switch-${idx}" ${isLucky ? 'checked' : ''}>
                        <span class="slider"></span>
                    </label>
                `;

                const checkbox = luckyBox.querySelector('input[type="checkbox"]');
                checkbox?.addEventListener('change', (e) => {
                    this.luckyGuesses[idx] = e.target.checked;
                    const luckyCount = Object.values(this.luckyGuesses).filter(Boolean).length;
                    if (this.dom.statLucky) this.dom.statLucky.textContent = luckyCount.toString();
                    this.updateFilterCounts();
                });

                card.appendChild(luckyBox);
            }

            this.dom.reviewCardsList.appendChild(card);
        });

        this.refreshLucideIcons();
    }

    setReviewFilter(filter) {
        this.activeFilter = filter;
        document.querySelectorAll('.filter-pill').forEach(pill => {
            pill.classList.toggle('active', pill.dataset.filter === filter);
        });
        this.renderReviewCards();
    }

    updateFilterCounts() {
        if (!this.quizData) return;
        const total = this.quizData.questions.length;
        let correct = 0;
        let wrong = 0;

        this.quizData.questions.forEach((q, idx) => {
            if (this.answers[idx] === q.correct) correct++;
            else wrong++;
        });

        const lucky = Object.values(this.luckyGuesses).filter(Boolean).length;

        if (this.dom.filterCountAll) this.dom.filterCountAll.textContent = total.toString();
        if (this.dom.filterCountWrong) this.dom.filterCountWrong.textContent = wrong.toString();
        if (this.dom.filterCountCorrect) this.dom.filterCountCorrect.textContent = correct.toString();
        if (this.dom.filterCountLucky) this.dom.filterCountLucky.textContent = lucky.toString();
    }

    /**
     * Telemetry Submission (POST /api/quiz/submit)
     */
    async submitTelemetry() {
        if (!this.quizData || this.isSubmitted) return;

        if (this.dom.btnSubmitTelemetry) {
            this.dom.btnSubmitTelemetry.disabled = true;
            this.dom.btnSubmitTelemetry.innerHTML = `
                <div class="spinner" style="width: 18px; height: 18px; border-width: 2px;"></div>
                <span>Sending...</span>
            `;
        }

        const questions = this.quizData.questions;
        let correctCount = 0;
        let wrongCount = 0;
        let totalDwell = 0;

        const questionPayloads = questions.map((q, idx) => {
            const userAns = this.answers[idx];
            const isCorrect = userAns !== undefined && userAns === q.correct;
            if (isCorrect) correctCount++;
            else wrongCount++;

            const dwell = this.dwellTimes[idx] || 0;
            totalDwell += dwell;

            const isLucky = !!this.luckyGuesses[idx];
            const reflection = this.reflections[idx];
            const optionKeys = q.optionKeys || ['A', 'B', 'C', 'D'];
            const selectedKey = userAns !== undefined ? (optionKeys[userAns] || ['A', 'B', 'C', 'D'][userAns] || null) : null;
            const correctKey = q.correctLetter || optionKeys[q.correct] || ['A', 'B', 'C', 'D'][q.correct] || 'A';

            return {
                id: q.id || `q_${idx + 1}`,
                selected: selectedKey,
                correct: correctKey,
                concept_id: q.concept_id || 'concept_general',
                bloom_level: q.bloom_level || null,
                is_correct: isCorrect,
                is_lucky_guess: isLucky,
                reflection: !isCorrect ? {
                    reason: reflection?.reason || 'Concept Gap',
                    note: reflection?.notes || reflection?.note || ''
                } : null,
                dwell_time_seconds: parseFloat(dwell.toFixed(1)),
                answered_at: this.answerTimestamps[idx]
                    ? new Date(this.answerTimestamps[idx]).toISOString()
                    : null
            };
        });

        const total = questions.length;
        const percentage = total > 0 ? parseFloat(((correctCount / total) * 100).toFixed(1)) : 0.0;
        const avgDwell = total > 0 ? parseFloat((totalDwell / total).toFixed(1)) : 0.0;

        const now = new Date();
        const pad = (n) => n.toString().padStart(2, '0');
        const finishedAt = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}`;
        const sessionDuration = this.sessionDuration || Math.round((Date.now() - this.sessionStartTime) / 1000);

        const payload = {
            submission_uuid: this.submissionUUID,
            quiz_id: this.quizId || this.quizData.quiz_id || null,
            instructor: this.quizData.instructor || null,
            subject_id: this.quizData.subject || this.quizData.subject_id || this.subjectId || 'CS_GENERAL',
            topic: this.quizData.topic || 'Interactive Quiz',
            finished_at: finishedAt,
            session_duration_seconds: sessionDuration,
            summary: {
                total,
                correct: correctCount,
                wrong: wrongCount,
                percentage,
                avg_dwell_time_seconds: avgDwell,
                total_time_seconds: parseFloat(totalDwell.toFixed(1)),
                wrong_ids: questionPayloads.filter(p => !p.is_correct).map(p => p.id),
                lucky_ids: questionPayloads.filter(p => p.is_lucky_guess).map(p => p.id)
            },
            questions: questionPayloads
        };

        try {
            const response = await fetch('/api/quiz/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error(`Submission failed with status ${response.status}`);
            }

            this.isSubmitted = true;
            if (this.dom.syncStatusBanner) {
                this.dom.syncStatusBanner.classList.remove('hidden');
            }

            if (this.dom.btnSubmitTelemetry) {
                this.dom.btnSubmitTelemetry.innerHTML = `
                    <i data-lucide="check"></i>
                    <span>Synced</span>
                `;
            }
        } catch (err) {
            console.error('Telemetry submit error:', err);
            // Save to localStorage as offline queue
            this.saveOfflineTelemetry(payload);

            this.showTemporaryToast('Telemetry saved locally (server offline)');
            if (this.dom.syncStatusBanner) {
                this.dom.syncStatusBanner.classList.remove('hidden');
                this.dom.syncStatusBanner.querySelector('strong').textContent = 'Telemetry Saved Locally';
            }
            if (this.dom.btnSubmitTelemetry) {
                this.dom.btnSubmitTelemetry.innerHTML = `
                    <i data-lucide="cloud-off"></i>
                    <span>Saved Locally</span>
                `;
            }
        } finally {
            this.refreshLucideIcons();
        }
    }

    saveOfflineTelemetry(payload) {
        try {
            const queue = JSON.parse(localStorage.getItem('master_studio_offline_telemetry') || '[]');
            queue.push(payload);
            localStorage.setItem('master_studio_offline_telemetry', JSON.stringify(queue));
        } catch (e) {
            console.error('Failed to save offline telemetry:', e);
        }
    }

    /**
     * Retry any telemetry queued while the server was offline.
     * Called on page load; successfully synced payloads drain from the queue.
     */
    async flushOfflineQueue() {
        let queue = [];
        try {
            queue = JSON.parse(localStorage.getItem('master_studio_offline_telemetry') || '[]');
        } catch (e) {
            return;
        }
        if (!Array.isArray(queue) || queue.length === 0) return;

        const remaining = [];
        for (const payload of queue) {
            try {
                const res = await fetch('/api/quiz/submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                if (!res.ok) remaining.push(payload);
            } catch (e) {
                remaining.push(payload);
            }
        }
        try {
            localStorage.setItem('master_studio_offline_telemetry', JSON.stringify(remaining));
        } catch (e) { /* storage unavailable — keep queue intact */ }
        const flushed = queue.length - remaining.length;
        if (flushed > 0) {
            this.showTemporaryToast(`Synced ${flushed} offline quiz result${flushed > 1 ? 's' : ''}`);
        }
    }

    restartQuiz() {
        this.setupQuizSession();
    }

    /**
     * Bookmarks Management (GET / POST /api/quiz/bookmarks)
     */
    async loadBookmarks() {
        try {
            const response = await fetch('/api/quiz/bookmarks');
            if (response.ok) {
                const data = await response.json();
                const list = Array.isArray(data) ? data : (data.bookmarks || []);
                this.bookmarks = new Set(list);
            } else {
                throw new Error('Bookmarks API not available');
            }
        } catch (e) {
            // Load from LocalStorage fallback
            const saved = JSON.parse(localStorage.getItem('master_studio_bookmarks') || '[]');
            this.bookmarks = new Set(saved);
        }
        this.updateBookmarksBadge();
        this.renderBookmarksDrawer();
    }

    async saveBookmarks() {
        const list = Array.from(this.bookmarks);
        localStorage.setItem('master_studio_bookmarks', JSON.stringify(list));
        this.updateBookmarksBadge();
        this.renderBookmarksDrawer();

        try {
            await fetch('/api/quiz/bookmarks', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(list)
            });
        } catch (e) {
            // Silently fallback to local storage
        }
    }

    toggleCurrentBookmark() {
        if (!this.quizData || !this.quizData.questions[this.currentIndex]) return;
        const qId = this.quizData.questions[this.currentIndex].id || `q_${this.currentIndex}`;
        
        if (this.bookmarks.has(qId)) {
            this.bookmarks.delete(qId);
            this.dom.btnBookmarkQuestion?.classList.remove('bookmarked');
        } else {
            this.bookmarks.add(qId);
            this.dom.btnBookmarkQuestion?.classList.add('bookmarked');
        }

        this.saveBookmarks();
        this.refreshLucideIcons();
    }

    updateBookmarksBadge() {
        const count = this.bookmarks.size;
        if (this.dom.bookmarksBadge) {
            this.dom.bookmarksBadge.textContent = count.toString();
            this.dom.bookmarksBadge.style.display = count > 0 ? 'flex' : 'none';
        }
    }

    renderBookmarksDrawer() {
        if (!this.dom.bookmarksList || !this.dom.bookmarksEmpty) return;

        if (this.bookmarks.size === 0) {
            this.dom.bookmarksList.innerHTML = '';
            this.dom.bookmarksEmpty.classList.remove('hidden');
            return;
        }

        this.dom.bookmarksEmpty.classList.add('hidden');
        this.dom.bookmarksList.innerHTML = '';

        this.bookmarks.forEach(qId => {
            const item = document.createElement('div');
            item.className = 'drawer-item';
            
            let label = qId;
            let targetIdx = -1;
            if (this.quizData && this.quizData.questions) {
                const idx = this.quizData.questions.findIndex(q => (q.id || `q_${this.quizData.questions.indexOf(q)}`) === qId);
                if (idx !== -1) {
                    label = `Q${idx + 1}: ${this.quizData.questions[idx].question.substring(0, 40)}...`;
                    targetIdx = idx;
                }
            }

            item.innerHTML = `
                <span class="drawer-item-title">${this.escapeHtml(label)}</span>
                <div style="display: flex; gap: 0.25rem;">
                    ${targetIdx !== -1 ? `
                        <button class="icon-btn-sm btn-jump" title="Jump to question">
                            <i data-lucide="arrow-right"></i>
                        </button>
                    ` : ''}
                    <button class="icon-btn-sm btn-remove" title="Remove bookmark">
                        <i data-lucide="trash-2"></i>
                    </button>
                </div>
            `;

            item.querySelector('.btn-jump')?.addEventListener('click', () => {
                this.jumpToQuestion(targetIdx);
            });

            item.querySelector('.btn-remove')?.addEventListener('click', () => {
                this.bookmarks.delete(qId);
                this.saveBookmarks();
                if (this.currentIndex === targetIdx) {
                    this.dom.btnBookmarkQuestion?.classList.remove('bookmarked');
                }
            });

            this.dom.bookmarksList.appendChild(item);
        });

        this.refreshLucideIcons();
    }

    /**
     * Drawer Controls
     */
    openDrawer(drawer) {
        if (!drawer || !this.dom.drawerOverlay) return;
        this.dom.drawerOverlay.classList.add('active');
        this.dom.drawerOverlay.setAttribute('aria-hidden', 'false');
        drawer.classList.add('open');
        drawer.setAttribute('aria-hidden', 'false');
        this.refreshLucideIcons();
    }

    closeDrawer(drawer) {
        if (!drawer) return;
        drawer.classList.remove('open');
        drawer.setAttribute('aria-hidden', 'true');
        if (!document.querySelector('.drawer.open')) {
            this.dom.drawerOverlay?.classList.remove('active');
            this.dom.drawerOverlay?.setAttribute('aria-hidden', 'true');
        }
    }

    closeAllDrawers() {
        document.querySelectorAll('.drawer').forEach(d => {
            d.classList.remove('open');
            d.setAttribute('aria-hidden', 'true');
        });
        this.dom.drawerOverlay?.classList.remove('active');
        this.dom.drawerOverlay?.setAttribute('aria-hidden', 'true');
    }

    /**
     * UI State Management (loading, error, quiz, results)
     */
    showState(state) {
        this.dom.quizLoading?.classList.toggle('hidden', state !== 'loading');
        this.dom.quizError?.classList.toggle('hidden', state !== 'error');
        this.dom.quizView?.classList.toggle('hidden', state !== 'quiz');
        this.dom.resultsView?.classList.toggle('hidden', state !== 'results');
    }

    /**
     * Lucide Icons Refresh Utility
     */
    refreshLucideIcons() {
        if (typeof lucide !== 'undefined' && lucide.createIcons) {
            lucide.createIcons();
        }
    }

    showTemporaryToast(message) {
        const toast = document.createElement('div');
        toast.style.position = 'fixed';
        toast.style.bottom = '80px';
        toast.style.left = '50%';
        toast.style.transform = 'translateX(-50%)';
        toast.style.backgroundColor = 'var(--bg-card)';
        toast.style.color = 'var(--text-main)';
        toast.style.border = '1px solid var(--border-focus)';
        toast.style.padding = '0.6rem 1.2rem';
        toast.style.borderRadius = 'var(--radius-full)';
        toast.style.boxShadow = 'var(--shadow-lg)';
        toast.style.zIndex = '100';
        toast.style.fontSize = '0.875rem';
        toast.style.fontWeight = '600';
        toast.textContent = message;

        document.body.appendChild(toast);
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.3s ease';
            setTimeout(() => toast.remove(), 300);
        }, 2000);
    }

    escapeHtml(str) {
        if (!str) return '';
        const div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    }

    /**
     * Fallback Quiz Data (For standalone demo/testing)
     */
    getFallbackQuizData() {
        return {
            quiz_id: "demo_quiz_01",
            subject_id: "CS501",
            topic: "Search & Optimization Algorithms",
            questions: [
                {
                    id: "q1",
                    concept_id: "bfs_traversal",
                    question: "Which data structure is fundamentally used by Breadth-First Search (BFS) to maintain the frontier of vertices?",
                    options: [
                        "FIFO Queue",
                        "LIFO Stack",
                        "Binary Max-Heap",
                        "Disjoint-Set Union"
                    ],
                    correct: 0,
                    explanation: "BFS explores nodes in level-order, requiring a FIFO (First-In, First-Out) queue to process nodes in the order they are discovered.",
                    bloom_level: "Understand"
                },
                {
                    id: "q2",
                    concept_id: "astar_heuristics",
                    question: "In the A* search algorithm, which condition guarantees that the algorithm finds an optimal path on tree search?",
                    options: [
                        "The heuristic function h(n) must be consistent (monotonic)",
                        "The heuristic function h(n) must be admissible (never overestimates true cost)",
                        "The cost function g(n) must equal zero for all nodes",
                        "The branching factor must be strictly less than 2"
                    ],
                    correct: 1,
                    explanation: "Admissibility (h(n) <= h*(n)) is both necessary and sufficient to guarantee optimality for A* tree search.",
                    bloom_level: "Analyze"
                },
                {
                    id: "q3",
                    concept_id: "dijkstra_complexity",
                    question: "What is the tightest worst-case time complexity of Dijkstra's algorithm implemented with a Fibonacci Heap for graph G = (V, E)?",
                    options: [
                        "O(|E| + |V| log |V|)",
                        "O(|V|^2)",
                        "O(|E| log |V|)",
                        "O(|V| |E|)"
                    ],
                    correct: 0,
                    explanation: "With a Fibonacci heap, decrease-key takes amortized O(1) time and extract-min takes O(log |V|), yielding overall O(|E| + |V| log |V|).",
                    bloom_level: "Apply"
                },
                {
                    id: "q4",
                    concept_id: "minimax_pruning",
                    question: "Alpha-Beta pruning reduces the search space of the Minimax algorithm without altering the final optimal move choice.",
                    options: [
                        "True, it prunes branches that cannot possibly influence the final decision",
                        "False, it is an approximation heuristic that may choose suboptimal moves",
                        "True, but only when evaluation depths are odd numbers",
                        "False, because alpha and beta bounds change the minimax values"
                    ],
                    correct: 0,
                    explanation: "Alpha-Beta pruning is mathematically exact and computes the exact same minimax value at the root as standard Minimax, while skipping provably irrelevant branches.",
                    bloom_level: "Evaluate"
                }
            ]
        };
    }
}

// Instantiate QuizApp on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    window.quizApp = new QuizApp();
});
