(() => {
  const page = document.body.dataset.page;
  const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  const subjectNames = {
    '01_Cyber_Security':'الأمن السيبراني','02_English_Language':'اللغة الإنجليزية',
    '03_Data_Mining':'التنقيب عن البيانات','04_Advanced_Software_Eng':'هندسة البرمجيات',
    '05_Soft_Computing':'الحوسبة الناعمة','06_Artificial_Intelligence':'الذكاء الاصطناعي'
  };
  const getSubject = id => subjectNames[id] || String(id || 'عام').replace(/^\d+_/,'').replace(/_/g,' ');
  const getBookmarks = async () => {
    let remote = [];
    try { const res = await fetch('/api/quiz/bookmarks'); if (res.ok) { const data = await res.json(); remote = Array.isArray(data) ? data : (data.bookmarks || []); } } catch (_) {}
    let local = []; try { local = JSON.parse(localStorage.getItem('master_studio_bookmarks') || '[]'); } catch (_) {}
    const map = new Map();
    [...remote, ...(Array.isArray(local) ? local : [])].forEach(item => { if (item && item.k) map.set(item.k, item); });
    return [...map.values()];
  };
  const getRecentLocal = () => {
    const cutoff = Date.now() - 7 * 86400000;
    let all = []; try { all = JSON.parse(localStorage.getItem('master_studio_quiz_history') || '[]'); } catch (_) {}
    const recent = (Array.isArray(all) ? all : []).filter(item => Date.parse(item.finishedAt) >= cutoff);
    try { localStorage.setItem('master_studio_quiz_history', JSON.stringify(recent)); } catch (_) {}
    return recent;
  };
  const fmtDate = stamp => {
    const date = new Date(stamp);
    return Number.isNaN(date.getTime()) ? 'تاريخ غير متاح' : new Intl.DateTimeFormat('ar-IQ',{weekday:'long',day:'numeric',month:'long'}).format(date);
  };
  const fmtTime = stamp => {
    const date = new Date(stamp);
    return Number.isNaN(date.getTime()) ? '' : new Intl.DateTimeFormat('ar-IQ',{hour:'2-digit',minute:'2-digit'}).format(date);
  };
  const loadBookmarks = async () => {
    const list = await getBookmarks();
    const filters = document.getElementById('bookmark-filters');
    const content = document.getElementById('bookmark-content');
    document.getElementById('bookmark-total').textContent = `${list.length} سؤال`;
    if (!list.length) {
      content.innerHTML='<div class="library-empty"><strong>ماكو أسئلة محفوظة بعد</strong><span>احفظ سؤالاً من داخل أي اختبار حتى يظهر هنا.</span></div>';
      const practiceButton=document.getElementById('bookmark-practice');
      if(practiceButton)practiceButton.disabled=true;
      const countLabel=document.getElementById('bookmark-practice-count');
      if(countLabel)countLabel.textContent='(0)';
      return;
    }
    const subjects = [...new Set(list.map(x=>x.subject || '').filter(Boolean))];
    filters.innerHTML = `<button type="button" class="library-filter active" data-filter="all">الكل (${list.length})</button>` + subjects.map(id=>`<button type="button" class="library-filter" data-filter="${escapeHtml(id)}">${escapeHtml(getSubject(id))} (${list.filter(x=>x.subject===id).length})</button>`).join('');
    let activeFilter='all';
    const practiceButton=document.getElementById('bookmark-practice');
    const render = filter => {
      activeFilter=filter;
      const selected = filter === 'all' ? list : list.filter(x=>x.subject===filter);
      const practiceItems=selected.filter(item=>item.question_data && Array.isArray(item.question_data.options) && item.question_data.options.length>1 && (item.question_data.correct!==undefined || item.question_data.answer!==undefined || item.question_data.correctLetter!==undefined));
      const countLabel=document.getElementById('bookmark-practice-count');
      if(countLabel)countLabel.textContent=`(${practiceItems.length})`;
      if(practiceButton)practiceButton.disabled=!practiceItems.length;
      content.innerHTML = `<div class="bookmark-list">${selected.map((item,index)=>{
        const text=item.question_data?.question_ar || item.question_data?.question || item.text || 'سؤال محفوظ';
        const href=item.url ? `${item.url}#q=${Number(item.n||0)+1}` : '/quiz';
        return `<article class="bookmark-row"><div><div class="bookmark-question">${escapeHtml(text)}</div><div class="bookmark-meta">${escapeHtml(getSubject(item.subject))} · سؤال ${Number(item.n||0)+1}</div></div><div class="bookmark-actions"><a class="bookmark-open" href="${escapeHtml(href)}">افتح موضع السؤال <i data-lucide="arrow-up-left"></i></a><button type="button" class="bookmark-remove" data-key="${escapeHtml(item.k)}">إزالة</button></div></article>`;
      }).join('')}</div>`;
      window.lucide?.createIcons();
      content.querySelectorAll('.bookmark-remove').forEach(button=>button.addEventListener('click',async()=>{
        const key=button.dataset.key;
        const next=list.filter(item=>item.k!==key);
        try{localStorage.setItem('master_studio_bookmarks',JSON.stringify(next));}catch(_){}
        try{await fetch('/api/quiz/bookmarks',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(next)});}catch(_){}
        await loadBookmarks();
      }));
    };
    filters.querySelectorAll('button').forEach(button=>button.addEventListener('click',()=>{
      filters.querySelectorAll('button').forEach(x=>x.classList.toggle('active',x===button)); render(button.dataset.filter);
    }));
    practiceButton?.addEventListener('click',()=>{
      const selected=activeFilter==='all'?list:list.filter(item=>item.subject===activeFilter);
      const practiceItems=selected.filter(item=>item.question_data && Array.isArray(item.question_data.options) && item.question_data.options.length>1 && (item.question_data.correct!==undefined || item.question_data.answer!==undefined || item.question_data.correctLetter!==undefined));
      if(!practiceItems.length)return;
      const subjectTitle=activeFilter==='all'?'كل المواد':getSubject(activeFilter);
      const payload={quiz_id:`bookmarks_drill_${Date.now()}`,subject_id:activeFilter==='all'?'00_STUDIO_HUB':activeFilter,subject:subjectTitle,topic:`مراجعة الأسئلة المحفوظة: ${subjectTitle} (${practiceItems.length} أسئلة)`,questions:practiceItems.map(item=>JSON.parse(JSON.stringify(item.question_data)))};
      try{localStorage.setItem('ms_bookmarks_drill_payload',JSON.stringify(payload));window.location.href='/quiz?bookmarks-drill=1';}catch(_){alert('تعذر بدء التدريب؛ مساحة التخزين المحلية ممتلئة.');}
    });
    render('all');
  };
  const renderQuestions = attempt => {
    const main=document.getElementById('library-main');
    const questions=Array.isArray(attempt.questions)?attempt.questions:[];
    main.innerHTML=`<a class="library-back" href="/quiz/history"><i data-lucide="arrow-right"></i> سجل الاختبارات</a>
      <header class="review-head"><h1>${escapeHtml(attempt.title || attempt.topic || 'مراجعة الاختبار')}</h1><p>${escapeHtml(getSubject(attempt.subjectId || attempt.subject_id))} · ${escapeHtml(fmtDate(attempt.finishedAt || attempt.finished_at || attempt.timestamp))} ${escapeHtml(fmtTime(attempt.finishedAt || attempt.finished_at || attempt.timestamp))}</p>
      <div class="review-summary">النتيجة: ${escapeHtml(attempt.score ?? 0)} / ${escapeHtml(attempt.total ?? 0)} · ${escapeHtml(attempt.percentage ?? 0)}%</div></header>
      <section aria-label="مراجعة الإجابات">${questions.map((q,i)=>{
        const options=Array.isArray(q.options)?q.options:(q.options_ar || []);
        const correct=Number(q.correct); const selected=q.selected===null || q.selected===undefined ? null:Number(q.selected);
        const isCorrect=q.isCorrect ?? (selected!==null && selected===correct);
        return `<article class="saved-review-question"><h2>${i+1}. ${escapeHtml(q.question || q.question_ar || q.questionEn || q.question_en)}</h2>
          ${options.map((option,index)=>`<div class="saved-option ${index===correct?'correct':''} ${index===selected && index!==correct?'selected-wrong':''}"><span>${index===correct?'✓':index===selected?'●':'○'}</span><span>${escapeHtml(option)}</span>${index===selected?'<b class="saved-review-status">إجابتك</b>':''}${index===correct?'<b class="saved-review-status">الصحيحة</b>':''}</div>`).join('')}
          ${q.explanation?`<p class="saved-explanation"><strong>التفسير:</strong> ${escapeHtml(q.explanation)}</p>`:''}
          ${selected===null?'<p class="legacy-note">لم تُسجّل إجابة لهذا السؤال.</p>':''}</article>`;
      }).join('') || '<p class="legacy-note">تفاصيل الأسئلة لهذه المحاولة القديمة غير متوفرة؛ النتيجة محفوظة كملخص فقط.</p>'}</section>`;
    window.lucide?.createIcons();
  };
  const loadHistory = async () => {
    const target=document.getElementById('history-content');
    const local=getRecentLocal();
    let remote=[];
    try { const res=await fetch('/api/quiz/history'); if(res.ok){const data=await res.json();remote=data.history||[];} } catch (_) {}
    const byId=new Map(local.map(item=>[item.id,item]));
    remote.forEach(item=>{
      const stamp=item.finished_at || item.timestamp;
      const parsedStamp=Date.parse(stamp);
      if(!Number.isFinite(parsedStamp) || Date.now()-parsedStamp>7*86400000) return;
      const id=item.submission_uuid || `server-${item.quiz_id}-${stamp}`;
      if(!byId.has(id)) byId.set(id,{id,finishedAt:stamp,title:item.topic,subjectId:item.subject_id,score:item.score,total:item.total,percentage:item.percentage,questions:[]});
    });
    const attempts=[...byId.values()].sort((a,b)=>Date.parse(b.finishedAt)-Date.parse(a.finishedAt));
    const attemptId=document.body.dataset.attemptId;
    if(attemptId){const found=attempts.find(x=>x.id===attemptId); if(found){renderQuestions(found);return;} target.innerHTML='<div class="library-empty"><strong>ما لقينا هذه المحاولة على هذا الجهاز</strong><span>تفاصيل المراجعة محفوظة محلياً في المتصفح الذي أُجري فيه الاختبار.</span></div>';return;}
    if(!attempts.length){target.innerHTML='<div class="library-empty"><strong>ماكو اختبارات خلال آخر ٧ أيام</strong><span>بعد ما تكمل اختبار، راح يظهر هنا تلقائياً مع مراجعة إجاباتك.</span></div>';return;}
    const grouped=new Map(); attempts.forEach(item=>{const day=new Date(item.finishedAt).toLocaleDateString('en-CA'); if(!grouped.has(day))grouped.set(day,[]);grouped.get(day).push(item);});
    target.innerHTML=[...grouped.entries()].map(([day,items])=>`<section><h2 class="library-day">${escapeHtml(fmtDate(day+'T12:00:00'))}</h2><div class="history-list">${items.map(item=>{
      const pct=Number(item.percentage)||0; const href=`/quiz/history/${encodeURIComponent(item.id)}`;
      return `<a class="history-row" href="${href}"><div><div class="history-title">${escapeHtml(item.title || 'اختبار')}</div><div class="history-subject">${escapeHtml(getSubject(item.subjectId || item.subject_id))} · ${escapeHtml(item.score ?? 0)} من ${escapeHtml(item.total ?? 0)}</div></div><div class="history-date">${escapeHtml(fmtTime(item.finishedAt))}</div><div class="history-score ${pct<60?'needs-review':''}">${escapeHtml(pct)}% <span class="history-arrow">›</span></div></a>`;
    }).join('')}</div></section>`).join('');
  };
  const savedTheme=localStorage.getItem('master_studio_theme');
  if(savedTheme) document.documentElement.dataset.theme=savedTheme;
  const themeIcon=document.getElementById('library-theme-icon');
  if(themeIcon)themeIcon.setAttribute('data-lucide',document.documentElement.dataset.theme==='dark'?'moon':'sun');
  document.getElementById('library-theme-toggle')?.addEventListener('click',()=>{const next=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=next;localStorage.setItem('master_studio_theme',next);themeIcon?.setAttribute('data-lucide',next==='dark'?'moon':'sun');window.lucide?.createIcons();});
  window.lucide?.createIcons();
  if(page==='bookmarks') loadBookmarks(); else loadHistory();
})();
