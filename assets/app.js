'use strict';
(() => {
 const langs=['da','en','pt'];
 const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
 const read=(key,fallback)=>{try{return JSON.parse(localStorage.getItem('elev:'+key))??fallback;}catch{return fallback;}};
 const write=(key,val)=>{try{localStorage.setItem('elev:'+key,JSON.stringify(val));return true;}catch{return false;}};
 const i18n={da:{search:'Søg i materialet…',none:'Ingen resultater',saved:'Gemt på denne enhed',fail:'Kunne ikke gemme på enheden',done:'Markér som læst',undone:'Læst',copy:'Kopiér mine svar',copied:'Svar kopieret',stop:'Stop',listen:'Lyt',login:'Log ind · ord',logout:'Log ud',voice:'Google TTS svarede ikke. Bruger enhedens stemme.',noVoice:'Dansk stemme er ikke tilgængelig på denne enhed.',unavailable:'Funktionen kunne ikke indlæses. Prøv igen.',meaning:'Betydning',cancel:'Luk'},en:{search:'Search the material…',none:'No results',saved:'Saved on this device',fail:'Could not save on this device',done:'Mark as read',undone:'Read',copy:'Copy my answers',copied:'Answers copied',stop:'Stop',listen:'Listen',login:'Sign in · words',logout:'Sign out',voice:'Google TTS unavailable. Using the device voice.',noVoice:'No Danish voice is available on this device.',unavailable:'Could not load this feature. Try again.',meaning:'Meaning',cancel:'Close'},pt:{search:'Buscar no material…',none:'Nenhum resultado',saved:'Salvo neste dispositivo',fail:'Não foi possível salvar neste dispositivo',done:'Marcar como lido',undone:'Lido',copy:'Copiar minhas respostas',copied:'Respostas copiadas',stop:'Parar',listen:'Ouvir',login:'Entrar · palavras',logout:'Sair',voice:'Google TTS indisponível. Usando a voz do dispositivo.',noVoice:'Não há voz em dinamarquês neste dispositivo.',unavailable:'Não foi possível carregar. Tente novamente.',meaning:'Significado',cancel:'Fechar'}};
 let lang=read('lang','da');if(!langs.includes(lang))lang='da';
 let langTicket=0,toastTimer,saveTimer,positionTimer;
 function toast(text){const el=$('#toast');el.textContent=text;el.hidden=false;clearTimeout(toastTimer);toastTimer=setTimeout(()=>el.hidden=true,4200);}
 window.elev={get lang(){return lang},get labels(){return i18n[lang]},read,write,toast};
 function getAnchor(){const y=window.scrollY, top=105;const blocks=$$('.lang-panel:not([hidden]) [data-anchor]').filter(el=>el.getBoundingClientRect().height>0&&el.getBoundingClientRect().top<=top);const el=blocks.at(-1)||$('.lang-panel:not([hidden]) [data-anchor]');if(!el)return{y};const rect=el.getBoundingClientRect();return {id:el.dataset.anchor,ratio:(top-rect.top)/Math.max(rect.height,1),y};}
 function restoreAnchor(anchor){if(!anchor)return;const el=$(`.lang-panel:not([hidden]) [data-anchor="${anchor.id}"]`);if(el)window.scrollTo({top:window.scrollY+el.getBoundingClientRect().top+anchor.ratio*el.getBoundingClientRect().height-105,behavior:'instant'});else window.scrollTo({top:anchor.y||0,behavior:'instant'});}
 function setLang(next,initial=false){if(!langs.includes(next))return;const previous=lang,anchor=initial?null:getAnchor(),ticket=++langTicket;stopTts();lang=next;write('lang',lang);document.documentElement.dataset.preferredLang=lang;document.documentElement.lang=lang==='pt'?'pt-BR':lang;document.body.dataset.lang=lang;
  $$('.lang-panel').forEach(el=>el.hidden=el.dataset.lang!==lang);$$('[data-ui-lang]').forEach(el=>el.hidden=el.dataset.uiLang!==lang);$$('[data-set-lang]').forEach(el=>el.setAttribute('aria-pressed',String(el.dataset.setLang===lang)));
  const title=$('.lang-panel:not([hidden]) h1');if(title)document.title=title.textContent+' · elev';
  const search=$('#search');if(search){search.placeholder=i18n[lang].search;search.setAttribute('aria-label',i18n[lang].search);}
  $$('.complete').forEach(updateComplete);$$('.copy-answers').forEach(el=>el.textContent=i18n[lang].copy);$('#selection-actions').hidden=true;$('#word-overlay').hidden=true;
  $$('.save-state').forEach(el=>el.textContent=i18n[lang].saved);
  if(!initial&&location.hash.endsWith('-'+previous))history.replaceState(null,'',location.pathname+location.search+location.hash.slice(0,-previous.length)+lang);
  if(!initial)requestAnimationFrame(()=>{if(ticket===langTicket)restoreAnchor(anchor)});
  if(window.vocabulary)window.vocabulary.enable(lang==='da');
  document.dispatchEvent(new CustomEvent('elev:language',{detail:lang}));
 }
 $$('[data-set-lang]').forEach(el=>el.addEventListener('click',()=>setLang(el.dataset.setLang)));
 $('.menu-toggle')?.addEventListener('click',()=>{const open=$('.sidebar').classList.toggle('open');$('.menu-toggle').setAttribute('aria-expanded',String(open));});
 const page=document.body.dataset.page;
 // The side navigation belongs to the current book, not the entire library.
 const nav=$('#sidebar nav'), sidebarLabel=$('#sidebar .sidebar-label'), sidebarBottom=$('#sidebar .sidebar-bottom');
 const isHandbook=page.startsWith('programme/'), isLogistics=page.startsWith('logistik/');
 const bookLabels={programme:['Elevmappe · IKEA Logistik 2026','Apprenticeship handbook · IKEA Logistics 2026','Guia de formação · IKEA Logística 2026'],logistik:['Logistik · første skoleophold','Logistics · first school period','Logística · primeira etapa escolar']};
 function localizedText(values){return values.map((value,i)=>{const label=document.createElement('span');label.dataset.uiLang=langs[i];label.hidden=langs[i]!==lang;label.textContent=value;return label;});}
 function navLink(number,labels,href){const a=document.createElement('a'),n=document.createElement('span');a.href=href;n.className='nav-number';n.textContent=number;a.append(n,...localizedText(labels));return a;}
 function closeSidebar(){if($('.sidebar')?.classList.contains('open')){$('.sidebar').classList.remove('open');$('.menu-toggle')?.setAttribute('aria-expanded','false');}}
 function handbookTarget(anchor){return document.getElementById(anchor+'-'+lang);}
 function markHandbookChapter(){if(!isHandbook||!nav)return;const links=$$('[data-book-anchor]',nav);let active=links[0];for(const a of links){const section=handbookTarget(a.dataset.bookAnchor);if(section&&section.getBoundingClientRect().top<=150)active=a;else break;}for(const a of links){const selected=a===active;a.classList.toggle('active',selected);if(selected)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');}}
 if(nav){
  if(isHandbook){
   sidebarLabel.replaceChildren(...localizedText(bookLabels.programme));
   nav.replaceChildren();
   const topSections=$$('.lang-panel[data-lang="da"] .handbook-level-1');
   for(const [i,section] of topSections.entries()){
    const anchor=section.dataset.anchor,labels=langs.map(l=>document.getElementById(anchor+'-'+l)?.querySelector('h2')?.textContent.replace(/^\d+\.\s*/,'')||'');
    const a=navLink(String(i+1).padStart(2,'0'),labels,'#'+anchor+'-'+lang);a.dataset.bookAnchor=anchor;
    a.addEventListener('click',e=>{e.preventDefault();const target=handbookTarget(anchor);if(!target)return;history.pushState(null,'','#'+encodeURIComponent(target.id));closeSidebar();window.scrollTo({top:Math.max(0,window.scrollY+target.getBoundingClientRect().top-115),behavior:'instant'});markHandbookChapter();});nav.append(a);
   }
   // The old bottom link points to logistics, which is irrelevant inside the handbook.
   const bottomBook=sidebarBottom?.querySelector('a[href="#"], a[href$="logistik/index.html"]');
   if(bottomBook){bottomBook.href='#';bottomBook.replaceChildren(...localizedText(['Indholdsfortegnelse','Table of contents','Índice']));bottomBook.addEventListener('click',e=>{e.preventDefault();history.replaceState(null,'',location.pathname+location.search);window.scrollTo({top:0,behavior:'instant'});closeSidebar();});}
   sidebarBottom?.querySelector('[data-progress-chapter]')?.setAttribute('data-progress-chapter','0');
   let scheduled=false;window.addEventListener('scroll',()=>{if(!scheduled){scheduled=true;requestAnimationFrame(()=>{scheduled=false;markHandbookChapter();});}},{passive:true});
   document.addEventListener('elev:language',()=>{for(const a of $$('[data-book-anchor]',nav))a.href='#'+a.dataset.bookAnchor+'-'+lang;requestAnimationFrame(markHandbookChapter);});
   const jumpToHash=()=>{let hash;try{hash=decodeURIComponent(location.hash.slice(1));}catch{return;}if(!hash)return;const anchor=hash.replace(/-(da|en|pt)$/,'');const target=handbookTarget(anchor);if(target){if(hash!==target.id)history.replaceState(null,'','#'+encodeURIComponent(target.id));window.scrollTo({top:Math.max(0,window.scrollY+target.getBoundingClientRect().top-115),behavior:'instant'});markHandbookChapter();}};
   window.addEventListener('hashchange',jumpToHash);window.addEventListener('popstate',jumpToHash);
   if(location.hash)requestAnimationFrame(jumpToHash);
  }else if(isLogistics){
   sidebarLabel.replaceChildren(...localizedText(bookLabels.logistik));
   $$('a[href*="programme/"]',nav).forEach(a=>a.remove());
  }else{
   sidebarLabel.replaceChildren(...localizedText(['Alle materialer','All materials','Todos os materiais']));
   const root=document.body.dataset.root||'';
   nav.replaceChildren(navLink('01',bookLabels.programme,root+'programme/index.html'),navLink('02',bookLabels.logistik,root+'logistik/index.html'));
   sidebarBottom?.querySelector('a[href$="logistik/index.html"]')?.remove();
  }
 }

 function updateComplete(el){const done=read('read:'+el.dataset.page,false);el.setAttribute('aria-pressed',String(done));el.textContent=done?'✓ '+i18n[lang].undone:i18n[lang].done;}
 $$('.complete').forEach(el=>el.addEventListener('click',()=>{write('read:'+el.dataset.page,!read('read:'+el.dataset.page,false));$$('.complete').forEach(updateComplete);updateProgress();}));
 function updateProgress(){const all=window.ELEV_INDEX||[];$$('[data-progress-chapter]').forEach(el=>{const c=el.dataset.progressChapter,items=all.filter(p=>c==='all'||p.chapter===Number(c));const n=items.filter(p=>read('read:'+p.path,false)).length;const percent=items.length?Math.round(n/items.length*100):0;el.style.width=percent+'%';el.title=`${n} / ${items.length}`;});}
 let syncLock=false;
 $$('[data-answer-key]').forEach(el=>{el.value=read('answer:'+el.dataset.answerKey,'');el.addEventListener('input',()=>{if(syncLock)return;const key=el.dataset.answerKey,value=el.value;syncLock=true;$$('[data-answer-key]').filter(e=>e.dataset.answerKey===key&&e!==el).forEach(e=>e.value=value);syncLock=false;clearTimeout(el._saveTimer);el._saveTimer=setTimeout(()=>{const ok=write('answer:'+key,value);$$(`[data-save-key="${key}"]`).forEach(e=>e.textContent=ok?i18n[lang].saved:i18n[lang].fail)},500);});});
 function flushAnswers(){const seen=new Set();$$('[data-answer-key]').forEach(el=>{if(seen.has(el.dataset.answerKey))return;seen.add(el.dataset.answerKey);write('answer:'+el.dataset.answerKey,el.value)});}
 $$('[data-review-key]').forEach(el=>{el.checked=read(el.dataset.reviewKey,false);el.addEventListener('change',()=>{write(el.dataset.reviewKey,el.checked);$$(`[data-review-key="${el.dataset.reviewKey}"]`).forEach(x=>x.checked=el.checked);});});
 $$('.copy-answers').forEach(btn=>btn.addEventListener('click',async()=>{flushAnswers();const active=$('.lang-panel:not([hidden])');const lines=[active.querySelector('h1')?.textContent||document.title,''];$$('[data-answer-key]',active).forEach(el=>{const question=el.closest('section')?.querySelector('h2')?.textContent||'';if(el.value.trim())lines.push(question,el.value.trim(),'')});const text=lines.join('\n');try{await navigator.clipboard.writeText(text);toast(i18n[lang].copied);}catch{const area=document.createElement('textarea');area.value=text;document.body.append(area);area.select();try{document.execCommand('copy');toast(i18n[lang].copied)}catch{toast(i18n[lang].unavailable)}area.remove();}}));
 function hideGuide(){document.body.classList.remove('guide-mode');}
 $$('.folio').forEach(el=>el.addEventListener('dblclick',()=>{const a=getAnchor();document.body.classList.toggle('guide-mode');restoreAnchor(a);}));
 document.addEventListener('keydown',e=>{if(e.key==='Escape'){hideGuide();stopTts();$('#selection-actions').hidden=true;$('#word-overlay').hidden=true;if($('#search-results'))$('#search-results').hidden=true;}if(e.ctrlKey&&e.shiftKey&&e.code==='KeyG'){e.preventDefault();document.body.classList.toggle('guide-mode')}});
 window.addEventListener('pagehide',()=>{hideGuide();stopTts();flushAnswers();write('position:'+page,getAnchor());});
 window.addEventListener('pageshow',e=>{if(e.persisted)hideGuide();});
 document.addEventListener('visibilitychange',()=>{if(document.hidden)flushAnswers();});
 window.addEventListener('scroll',()=>{clearTimeout(positionTimer);positionTimer=setTimeout(()=>write('position:'+page,getAnchor()),350)},{passive:true});
 const search=$('#search');search?.addEventListener('input',()=>{const results=$('#search-results'),q=search.value.toLocaleLowerCase().trim();results.replaceChildren();if(q.length<2){results.hidden=true;return;}const root=document.body.dataset.root;const matches=(window.ELEV_INDEX||[]).filter(p=>[p.title[lang],p.text[lang],p.original].some(v=>v.toLocaleLowerCase().includes(q))).slice(0,12);for(const p of matches){const a=document.createElement('a');a.href=root+p.path;a.textContent=p.title[lang];const small=document.createElement('small');small.textContent=`${String(p.chapter).padStart(2,'0')} · ${p.original}`;a.append(small);results.append(a);}if(!matches.length){const p=document.createElement('p');p.textContent=i18n[lang].none;results.append(p);}results.hidden=false;});
 document.addEventListener('click',e=>{if(!e.target.closest('.search-box')&&$('#search-results'))$('#search-results').hidden=true;});
 // One player, a generation token and short Google TTS requests.
 let generation=0,currentAudio=null,currentUtterance=null,rate=.95;
 function stopTts(){generation++;if(currentAudio){currentAudio.pause();currentAudio.onended=null;currentAudio.onerror=null;currentAudio.removeAttribute('src');currentAudio.load();currentAudio=null;}if('speechSynthesis'in window)window.speechSynthesis.cancel();currentUtterance=null;}
 function splitText(text,max=180){const chunks=[];text=String(text).replace(/\s+/g,' ').trim();while(text.length>max){let at=text.lastIndexOf(' ',max);if(at<40)at=max;chunks.push(text.slice(0,at));text=text.slice(at).trim();}if(text)chunks.push(text);return chunks;}
 function browserSpeak(text,ticket){return new Promise(resolve=>{if(ticket!==generation)return resolve();if(!('speechSynthesis'in window)){toast(i18n[lang].noVoice);return resolve();}const u=new SpeechSynthesisUtterance(text);u.lang='da-DK';u.rate=rate;const voice=speechSynthesis.getVoices().find(v=>v.lang.toLowerCase().startsWith('da'));if(voice)u.voice=voice;u.onend=u.onerror=()=>{currentUtterance=null;resolve()};currentUtterance=u;speechSynthesis.speak(u);});}
 async function playTts(text){stopTts();if(lang!=='da')return;const ticket=generation,chunks=splitText(text);for(let i=0;i<chunks.length;i++){if(ticket!==generation)return;try{await new Promise((resolve,reject)=>{const audio=new Audio();audio.referrerPolicy='no-referrer';audio.playbackRate=rate;audio.src='https://translate.google.com/translate_tts?'+new URLSearchParams({ie:'UTF-8',client:'tw-ob',tl:'da',q:chunks[i]});currentAudio=audio;audio.onended=resolve;audio.onerror=reject;audio.play().catch(reject);});}catch(e){if(ticket!==generation||e?.name==='AbortError')return;toast(i18n[lang].voice);await browserSpeak(chunks.slice(i).join(' '),ticket);return;}}currentAudio=null;}
 window.studyTts={play:playTts,stop:stopTts,configure(){}};
 $$('.section-listen').forEach(btn=>btn.addEventListener('click',()=>{const section=btn.closest('section');const text=[section.querySelector('h2')?.textContent,section.querySelector('.paragraph-text')?.textContent].join(' ');playTts(text);}));
 $$('[data-video-tts]').forEach(btn=>btn.addEventListener('click',()=>playTts(btn.dataset.videoTts)));
 $$('[data-stop]').forEach(btn=>btn.addEventListener('click',stopTts));$$('[data-speed]').forEach(el=>el.addEventListener('change',()=>{rate=Number(el.value);write('rate',rate);if(currentAudio)currentAudio.playbackRate=rate;}));
 rate=read('rate',.95);if(![.8,.95,1.1].includes(rate))rate=.95;$$('[data-speed]').forEach(el=>el.value=rate);
 setLang(lang,true);updateProgress();
 if(!location.hash)requestAnimationFrame(()=>restoreAnchor(read('position:'+page,null)));
})();
