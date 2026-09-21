/**
 * Master Studio Flashcards & Active Recall Subsystem
 * Architecture: Mobile-First, 100% Offline-Capable (PWA), Local Storage Persistence
 */

class SoundManager {
    constructor() {
        this.ctx = null;
        this.muted = localStorage.getItem('master_studio_muted') === 'true';
    }

    init() {
        if (!this.ctx && typeof AudioContext !== 'undefined') {
            this.ctx = new AudioContext();
        }
    }

    play(type) {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.connect(gain);
        gain.connect(this.ctx.destination);

        if (type === 'flip') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(320, now);
            osc.frequency.exponentialRampToValueAtTime(480, now + 0.08);
            gain.gain.setValueAtTime(0.06, now);
            gain.gain.linearRampToValueAtTime(0.01, now + 0.08);
            osc.start(now);
            osc.stop(now + 0.08);
        } else if (type === 'rate') {
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(520, now);
            osc.frequency.exponentialRampToValueAtTime(780, now + 0.12);
            gain.gain.setValueAtTime(0.08, now);
            gain.gain.linearRampToValueAtTime(0.01, now + 0.12);
            osc.start(now);
            osc.stop(now + 0.12);
        }
    }

    toggleMute() {
        this.muted = !this.muted;
        localStorage.setItem('master_studio_muted', String(this.muted));
        return this.muted;
    }
}

class CardsApp {
    constructor() {
        this.sound = new SoundManager();
        this.lang = localStorage.getItem('master_studio_lang') || 'ar';
        this.root = document.getElementById('cards-root');

        const urlParams = new URLSearchParams(window.location.search);
        this.subjectId = this.root?.dataset?.subjectId || urlParams.get('subject') || '';
        this.quizId = this.root?.dataset?.quizId || urlParams.get('quiz') || '';

        this.deckData = null;
        this.cards = [];
        this.currentIndex = 0;
        this.isFlipped = false;
        this.ratings = {}; // { [cardId]: 'again' | 'hard' | 'good' | 'easy' }

        this.dom = {
            deckTitle: document.getElementById('deck-title'),
            deckSubtitle: document.getElementById('deck-subtitle'),
            btnExit: document.getElementById('btn-exit'),
            btnLangToggle: document.getElementById('btn-lang-toggle'),
            btnSoundToggle: document.getElementById('btn-sound-toggle'),
            soundIcon: document.getElementById('sound-icon'),
            btnThemeToggle: document.getElementById('btn-theme-toggle'),
            themeIcon: document.getElementById('theme-icon'),

            progressBarFill: document.getElementById('progress-bar-fill'),
            cardIndexLabel: document.getElementById('card-index-label'),
            cardTotalLabel: document.getElementById('card-total-label'),

            cardsLoading: document.getElementById('cards-loading'),
            cardsError: document.getElementById('cards-error'),
            errorMessage: document.getElementById('error-message'),
            btnRetryLoad: document.getElementById('btn-retry-load'),
            cardsView: document.getElementById('cards-view'),
            completeView: document.getElementById('cards-complete-view'),

            activeCard: document.getElementById('active-card'),
            cardConceptTag: document.getElementById('card-concept-tag'),
            cardBloomTag: document.getElementById('card-bloom-tag'),
            cardFrontText: document.getElementById('card-front-text'),
            cardModelAnswer: document.getElementById('card-model-answer'),
            cardExplanationText: document.getElementById('card-explanation-text'),

            ratingButtons: document.querySelectorAll('.rating-btn'),
            sumAgain: document.getElementById('sum-again'),
            sumHard: document.getElementById('sum-hard'),
            sumGood: document.getElementById('sum-good'),
            sumEasy: document.getElementById('sum-easy'),
            btnRestartDeck: document.getElementById('btn-restart-deck'),
            linkOpenAsQuiz: document.getElementById('link-open-as-quiz'),
        };

        this.init();
    }

    async init() {
        this.initTheme();
        this.initEvents();
        await this.loadDeck();
        this.refreshLucideIcons();
    }

    initTheme() {
        const saved = localStorage.getItem('master_studio_theme') || 'dark';
        document.documentElement.setAttribute('data-theme', saved);
        this.updateThemeIcon(saved);
    }

    toggleTheme() {
        const current = document.documentElement.getAttribute('data-theme') || 'dark';
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('master_studio_theme', next);
        this.updateThemeIcon(next);
    }

    updateThemeIcon(theme) {
        if (this.dom.themeIcon) {
            this.dom.themeIcon.setAttribute('data-lucide', theme === 'dark' ? 'moon' : 'sun');
            this.refreshLucideIcons();
        }
    }

    toggleLanguage() {
        this.lang = this.lang === 'ar' ? 'en' : 'ar';
        localStorage.setItem('master_studio_lang', this.lang);
        if (this.cards.length > 0) {
            this.renderCard(this.currentIndex);
        }
    }

    toggleSound() {
        const muted = this.sound.toggleMute();
        if (this.dom.soundIcon) {
            this.dom.soundIcon.setAttribute('data-lucide', muted ? 'volume-x' : 'volume-2');
            this.refreshLucideIcons();
        }
    }

    initEvents() {
        this.dom.btnThemeToggle?.addEventListener('click', () => this.toggleTheme());
        this.dom.btnLangToggle?.addEventListener('click', () => this.toggleLanguage());
        this.dom.btnSoundToggle?.addEventListener('click', () => this.toggleSound());
        this.dom.btnRetryLoad?.addEventListener('click', () => this.loadDeck());
        this.dom.btnRestartDeck?.addEventListener('click', () => this.restartDeck());

        // Card flip on tap / click
        this.dom.activeCard?.addEventListener('click', () => this.flipCard());

        // Rating buttons
        this.dom.ratingButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const rating = btn.getAttribute('data-rating');
                this.rateCard(rating);
            });
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.code === 'Space' || e.key === ' ') {
                e.preventDefault();
                this.flipCard();
            } else if (['1', '2', '3', '4'].includes(e.key)) {
                const map = { '1': 'again', '2': 'hard', '3': 'good', '4': 'easy' };
                this.rateCard(map[e.key]);
            }
        });
    }

    async loadDeck() {
        this.showState('loading');

        try {
            if (this.subjectId && this.quizId) {
                const res = await fetch(`/api/quiz/${encodeURIComponent(this.subjectId)}/${encodeURIComponent(this.quizId)}`);
                if (!res.ok) throw new Error(`HTTP ${res.status}`);
                this.deckData = await res.json();
            } else {
                this.deckData = this.getFallbackDeck();
            }

            this.setupDeck();
        } catch (err) {
            console.error('Failed to load flashcard deck:', err);
            if (this.dom.errorMessage) {
                this.dom.errorMessage.textContent = err.message || 'تعذر تحميل البطاقات.';
            }
            this.showState('error');
        }
    }

    setupDeck() {
        this.cards = (this.deckData?.questions || []).map((q, idx) => {
            // Determine correct answer text
            let answerText = '';
            let optionsArr = Array.isArray(q.options) ? q.options : Object.values(q.options || {});
            let optionsEnArr = Array.isArray(q.options_en) ? q.options_en : (q.options_en ? Object.values(q.options_en) : null);

            let corrIdx = 0;
            if (typeof q.answer === 'string') {
                const cleanAns = q.answer.trim().toUpperCase();
                corrIdx = ['A', 'B', 'C', 'D'].indexOf(cleanAns);
                if (corrIdx === -1) corrIdx = 0;
            } else if (typeof q.correct === 'number') {
                corrIdx = q.correct;
            }

            const arAnswer = optionsArr[corrIdx] || 'الإجابة النموذجية';
            const enAnswer = (optionsEnArr && optionsEnArr[corrIdx]) || optionsArr[corrIdx] || 'Model Answer';

            return {
                id: q.id || `card_${idx + 1}`,
                concept: q.concept_id || 'Concept',
                bloom: q.bloom_level || 'Recall',
                prompt_ar: q.question_ar || q.text || q.question || '',
                prompt_en: q.question || q.text_en || q.question_ar || '',
                answer_ar: arAnswer,
                answer_en: enAnswer,
                explanation: q.explanation || ''
            };
        });

        if (this.cards.length === 0) {
            throw new Error('لا توجد بطاقات في هذه المجموعة.');
        }

        const cleanSubj = this.deckData.subject?.replace(/^0\d_/, '').replace(/_/g, ' ') || 'Master Studio';
        if (this.dom.deckSubtitle) this.dom.deckSubtitle.textContent = cleanSubj;
        if (this.dom.deckTitle) this.dom.deckTitle.textContent = this.deckData.topic || 'بطاقات الاسترجاع';
        if (this.dom.cardTotalLabel) this.dom.cardTotalLabel.textContent = this.cards.length.toString();

        this.currentIndex = 0;
        this.ratings = {};
        this.showState('cards');
        this.renderCard(0);
    }

    renderCard(index) {
        if (!this.cards[index]) return;
        const card = this.cards[index];
        const isAr = this.lang === 'ar';

        // Unflip card
        this.isFlipped = false;
        this.dom.activeCard?.classList.remove('is-flipped');

        // Tags
        if (this.dom.cardConceptTag) this.dom.cardConceptTag.textContent = card.concept.replace(/_/g, ' ');
        if (this.dom.cardBloomTag) this.dom.cardBloomTag.textContent = card.bloom;

        // Front Face
        if (this.dom.cardFrontText) {
            this.dom.cardFrontText.textContent = isAr ? card.prompt_ar : card.prompt_en;
            this.dom.cardFrontText.style.direction = isAr ? 'rtl' : 'ltr';
            this.dom.cardFrontText.style.textAlign = isAr ? 'right' : 'left';
        }

        // Back Face
        if (this.dom.cardModelAnswer) {
            this.dom.cardModelAnswer.textContent = isAr ? card.answer_ar : card.answer_en;
            this.dom.cardModelAnswer.style.direction = isAr ? 'rtl' : 'ltr';
        }
        if (this.dom.cardExplanationText) {
            this.dom.cardExplanationText.textContent = card.explanation;
            this.dom.cardExplanationText.style.direction = 'rtl';
        }

        // Progress
        if (this.dom.cardIndexLabel) this.dom.cardIndexLabel.textContent = (index + 1).toString();
        if (this.dom.progressBarFill) {
            const pct = (index / this.cards.length) * 100;
            this.dom.progressBarFill.style.width = `${pct}%`;
        }

        this.refreshLucideIcons();
    }

    flipCard() {
        this.isFlipped = !this.isFlipped;
        this.dom.activeCard?.classList.toggle('is-flipped', this.isFlipped);
        this.sound.play('flip');
    }

    rateCard(rating) {
        if (!['again', 'hard', 'good', 'easy'].includes(rating)) return;
        const card = this.cards[this.currentIndex];
        if (!card) return;

        this.ratings[card.id] = rating;
        this.sound.play('rate');

        // Save progress to localStorage
        try {
            const storageKey = `cards_ratings_${this.subjectId}_${this.quizId}`;
            localStorage.setItem(storageKey, JSON.stringify(this.ratings));
        } catch (e) {
            console.error('LocalStorage error:', e);
        }

        if (this.currentIndex < this.cards.length - 1) {
            this.currentIndex++;
            this.renderCard(this.currentIndex);
        } else {
            this.finishDeck();
        }
    }

    finishDeck() {
        this.showState('complete');
        if (this.dom.progressBarFill) {
            this.dom.progressBarFill.style.width = '100%';
        }

        // Count ratings
        const counts = { again: 0, hard: 0, good: 0, easy: 0 };
        Object.values(this.ratings).forEach(r => {
            if (counts[r] !== undefined) counts[r]++;
        });

        if (this.dom.sumAgain) this.dom.sumAgain.textContent = counts.again.toString();
        if (this.dom.sumHard) this.dom.sumHard.textContent = counts.hard.toString();
        if (this.dom.sumGood) this.dom.sumGood.textContent = counts.good.toString();
        if (this.dom.sumEasy) this.dom.sumEasy.textContent = counts.easy.toString();

        if (this.dom.linkOpenAsQuiz) {
            this.dom.linkOpenAsQuiz.href = `/quiz/${encodeURIComponent(this.subjectId)}/${encodeURIComponent(this.quizId)}`;
        }

        this.refreshLucideIcons();
    }

    restartDeck() {
        this.currentIndex = 0;
        this.ratings = {};
        this.showState('cards');
        this.renderCard(0);
    }

    showState(state) {
        this.dom.cardsLoading?.classList.toggle('hidden', state !== 'loading');
        this.dom.cardsError?.classList.toggle('hidden', state !== 'error');
        this.dom.cardsView?.classList.toggle('hidden', state !== 'cards');
        this.dom.completeView?.classList.toggle('hidden', state !== 'complete');
    }

    refreshLucideIcons() {
        if (typeof lucide !== 'undefined' && lucide.createIcons) {
            lucide.createIcons();
        }
    }

    getFallbackDeck() {
        return {
            subject: "04_Advanced_Software_Eng",
            topic: "Lecture 01: Foundations & Software Crisis",
            questions: [
                {
                    id: "q1",
                    concept_id: "patriot_missile_clock_drift",
                    bloom_level: "Apply",
                    question: "What kinematic consequence caused the 1991 Dhahran Patriot missile failure?",
                    question_ar: "ما هي النتيجة الحركية المباشرة التي أدت لفشل صاروخ باتريوت الظهران عام 1991؟",
                    options: [
                        "Clock drift of 0.34 seconds shifted the radar range gate by ~687 meters."
                    ],
                    correct: 0,
                    explanation: "أدى اقتطاع النقطة الثابتة 24-بت لـ 1/10 على مدار 100 ساعة إلى فقدان 0.34 ثانية، مما أزاح بوابة النطاق بـ 687 متراً."
                }
            ]
        };
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.cardsApp = new CardsApp();
});
