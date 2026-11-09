'use strict';
(() => {
 const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
 const norm=x=>String(x||'').replace(/\s+/g,' ').trim();
 let enabled=false,started=false,loading=null,user=null,db=null,auth=null,saved=[],unsub=null,selection='',selectionTimer,ticket=0,controller=null;
 let activeMark=null,hoverPreview=false,hoverTimer,hoverSuppressed=false;
 const menu=$('#selection-actions'),overlay=$('#word-overlay'),authButton=$('#vocab-auth');
 function script(src){return new Promise((resolve,reject)=>{const s=document.createElement('script');s.src=src;s.onload=resolve;s.onerror=()=>{s.remove();reject(new Error('Firebase SDK could not load'))};document.head.append(s)})}
 async function initialise(){
  if(started)return;if(loading)return loading;
  loading=(async()=>{for(const part of ['app','auth','firestore'])if(!window.firebase||part!=='app'&&!firebase[part])await script(`https://www.gstatic.com/firebasejs/8.10.0/firebase-${part}.js`);
   const config={apiKey:'AIzaSyAmrttzr16EMpmmaNx8D7NUiwYjqo4996M',authDomain:'ov-dansk.firebaseapp.com',projectId:'ov-dansk',storageBucket:'ov-dansk.firebasestorage.app',messagingSenderId:'749643252913',appId:'1:749643252913:web:63f7c2f46815a35dfe0e90'};
   const app=firebase.apps.length?firebase.app():firebase.initializeApp(config);auth=app.auth();db=app.firestore();
   window.studyFirebase={app,auth,db,provider:new firebase.auth.GoogleAuthProvider(),user:null,signIn:()=>auth.signInWithPopup(new firebase.auth.GoogleAuthProvider()),signOut:()=>auth.signOut()};
   auth.onAuthStateChanged(u=>{user=u;studyFirebase.user=u;refreshSubscription();updateAuth();});started=true;
  })().catch(e=>{loading=null;throw e});return loading;
 }
 function updateAuth(){if(!authButton)return;authButton.textContent=user?`${user.displayName?.split(' ')[0]||'✓'} · Log ud`:'Log ind · ord';authButton.title=user?'Log ud af ov-dansk-kontoen':'Brug samme Google-konto som i ov-dansk';}
 function refreshSubscription(){unsub?.();unsub=null;saved=[];clearMarks();if(!enabled||!user||!db)return;unsub=db.collection('users').doc(user.uid).collection('customWords').onSnapshot(snap=>{saved=snap.docs.map(d=>({id:d.id,...d.data()})).filter(w=>norm(w.term)&&norm(w.meaning));highlight();},e=>window.elev.toast('Kunne ikke hente ordene. Kontrollér login og adgang.'));}
 function clearMarks(){if(activeMark)closeOverlay();$$('main mark.study-word').forEach(m=>m.replaceWith(document.createTextNode(m.textContent)));document.querySelectorAll('main .paragraph-text').forEach(e=>e.normalize());}
 function highlight(){clearMarks();if(!enabled||!saved.length)return;const words=[...saved].sort((a,b)=>b.term.length-a.term.length),lookup=new Map();for(const w of words)if(!lookup.has(norm(w.term).toLocaleLowerCase('da')))lookup.set(norm(w.term).toLocaleLowerCase('da'),w);
  const escape=s=>s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');const terms=[...lookup.keys()].map(escape).join('|');if(!terms)return;const re=new RegExp(`(?<![\\p{L}\\p{N}_])(${terms})(?![\\p{L}\\p{N}_])`,'giu');
  for(const p of $$('main .lang-panel[data-lang="da"] .paragraph-text')){const walk=document.createTreeWalker(p,NodeFilter.SHOW_TEXT,{acceptNode(n){return n.parentElement.closest('a,button,input,textarea,select,script,style,mark')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT}});const nodes=[];while(walk.nextNode())nodes.push(walk.currentNode);for(const node of nodes){re.lastIndex=0;const text=node.textContent,matches=[...text.matchAll(re)];if(!matches.length)continue;const fragment=document.createDocumentFragment();let at=0;for(const m of matches){fragment.append(document.createTextNode(text.slice(at,m.index)));const mark=document.createElement('mark');mark.className='study-word';mark.dataset.wordId=lookup.get(m[0].toLocaleLowerCase('da')).id;mark.textContent=m[0];mark.tabIndex=0;fragment.append(mark);at=m.index+m[0].length;}fragment.append(document.createTextNode(text.slice(at)));node.replaceWith(fragment);}}
 }
 function getSelection(){if(!enabled)return'';const s=window.getSelection();if(!s||s.rangeCount!==1||s.isCollapsed)return'';const r=s.getRangeAt(0),parent=n=>n.nodeType===Node.ELEMENT_NODE?n:n.parentElement;const a=parent(r.startContainer),b=parent(r.endContainer);if(!a?.closest('main .lang-panel[data-lang="da"] .paragraph-text')||!b?.closest('main .lang-panel[data-lang="da"] .paragraph-text'))return'';const value=norm(s.toString());return value.length<=500?value:'';}
 function selectionMenu(){clearTimeout(selectionTimer);selectionTimer=setTimeout(()=>{const selected=getSelection();if(selected){selection=selected;menu.hidden=false}else if(!menu.matches(':hover')){menu.hidden=true}},150);}
 ['selectionchange','mouseup','touchend'].forEach(e=>document.addEventListener(e,selectionMenu));menu.addEventListener('pointerdown',e=>e.preventDefault());
 function cancelTranslation(){ticket++;controller?.abort();controller=null;}
 function closeOverlay(restoreFocus=false){
  const mark=activeMark;
  clearTimeout(hoverTimer);
  cancelTranslation();
  // Hiding a panel can reveal a word under the pointer and fire pointerover.
  hoverSuppressed=overlay.matches(':hover')||Boolean(mark?.matches(':hover'));
  activeMark=null;
  hoverPreview=false;
  overlay.hidden=true;
  if(restoreFocus&&mark?.isConnected)mark.focus();
 }
 function showOverlay(term,meaning,mark=null,preview=false){
  clearTimeout(hoverTimer);
  cancelTranslation();
  activeMark=mark;
  hoverPreview=preview;
  overlay.replaceChildren();
  const close=document.createElement('button');
  close.type='button';
  close.className='close';
  close.textContent='×';
  close.setAttribute('aria-label','Luk');
  close.onclick=()=>closeOverlay(overlay.contains(document.activeElement));
  const strong=document.createElement('strong');
  strong.textContent=term;
  const p=document.createElement('p');
  p.textContent=meaning;
  overlay.append(close,strong,p);
  overlay.hidden=false;
  return overlay;
 }
 function action(parent,label,fn){const b=document.createElement('button');b.type='button';b.textContent=label;b.onclick=fn;parent.append(b);return b;}
 async function ensureUser(){await initialise();if(!user){const result=await studyFirebase.signIn();user=result.user;studyFirebase.user=user;}return user;}
 async function save(){if(!enabled||!selection)return;const term=norm(selection);try{const u=await ensureUser();if(!enabled||!u)return;const duplicate=saved.find(w=>norm(w.term).toLocaleLowerCase('da')===term.toLocaleLowerCase('da'));const value=window.prompt(`Betydning af:\n\n${term}`,duplicate?.meaning||'');const meaning=norm(value);if(!meaning)return;const ref=db.collection('users').doc(u.uid).collection('customWords');const now=firebase.firestore.FieldValue.serverTimestamp();if(duplicate)await ref.doc(duplicate.id).update({meaning,updatedAt:now});else await ref.doc().set({term,meaning,sourceUrl:location.href.split('#')[0],sourceTitle:document.title,createdAt:now,updatedAt:now});menu.hidden=true;window.elev.toast('Gemt · kan øves i ov-dansk → Saved Words');}catch(e){window.elev.toast(e.code==='auth/unauthorized-domain'?'Domænet skal godkendes i Firebase Authentication.':'Kunne ikke gemme ordet. Prøv igen.');}}
 $('#save-selection').onclick=save;
 $('#define-selection').onclick=()=>{if(!enabled||!selection)return;window.open('https://ordnet.dk/ddo/ordbog?query='+encodeURIComponent(selection),'_blank','noopener,noreferrer');menu.hidden=true};
 $('#listen-selection').onclick=()=>{if(enabled&&selection)window.studyTts.play(selection)};
 $('#translate-selection').onclick=async()=>{if(!enabled||!selection)return;const term=selection;const box=showOverlay(term,'Oversætter til portugisisk…');const id=ticket;controller=new AbortController();const compare=document.createElement('a');compare.href='https://translate.google.com/?'+new URLSearchParams({sl:'da',tl:'pt',text:term,op:'translate'});compare.target='_blank';compare.rel='noopener noreferrer';compare.textContent='Åbn i Google Translate';box.append(compare);try{const res=await fetch('https://translate.googleapis.com/translate_a/single?'+new URLSearchParams({client:'gtx',sl:'da',tl:'pt',dt:'t',q:term}),{signal:controller.signal});if(!res.ok)throw new Error(res.status);const data=await res.json(),translated=Array.isArray(data[0])?data[0].map(x=>Array.isArray(x)?x[0]:'').join(''):'';if(!translated)throw new Error('empty');if(id===ticket&&enabled)box.querySelector('p').textContent=translated;}catch(e){if(e.name!=='AbortError'&&id===ticket)box.querySelector('p').textContent='Oversættelse er ikke tilgængelig. Brug linket nedenfor.';}};
 function wordOverlay(mark,preview=false){if(!enabled)return;const item=saved.find(w=>w.id===mark.dataset.wordId);if(!item)return;const box=showOverlay(item.term,item.meaning,mark,preview);action(box,'Lyt',()=>studyTts.play(item.term));action(box,'Redigér',async()=>{if(!enabled||!user)return;const value=norm(window.prompt('Betydning:',item.meaning));if(!value)return;try{await db.collection('users').doc(user.uid).collection('customWords').doc(item.id).update({meaning:value,updatedAt:firebase.firestore.FieldValue.serverTimestamp()});if(activeMark===mark)closeOverlay()}catch{window.elev.toast('Kunne ikke opdatere ordet.')}});action(box,'Slet',async()=>{if(!enabled||!user||!window.confirm(`Slet “${item.term}” og øvelsesprogression?`))return;try{const u=db.collection('users').doc(user.uid),batch=db.batch();batch.delete(u.collection('customWords').doc(item.id));batch.delete(u.collection('progress').doc('custom_'+item.id));await batch.commit();if(activeMark===mark)closeOverlay()}catch{window.elev.toast('Kunne ikke slette ordet.')}});}
 document.addEventListener('pointermove',e=>{
  if(!e.target.closest?.('mark.study-word'))hoverSuppressed=false;
 });
 document.addEventListener('pointerover',e=>{
  if(e.pointerType!=='mouse')return;
  const mark=e.target.closest?.('mark.study-word');
  if(mark&&mark===activeMark){
   clearTimeout(hoverTimer);
  }else if(mark&&!hoverSuppressed&&(overlay.hidden||hoverPreview)){
   wordOverlay(mark,true);
  }
 });
 overlay.addEventListener('pointerenter',()=>clearTimeout(hoverTimer));
 document.addEventListener('pointerout',e=>{
  if(!hoverPreview||e.pointerType!=='mouse')return;
  if(!activeMark?.contains(e.target)&&!overlay.contains(e.target))return;
  if(activeMark?.contains(e.relatedTarget)||overlay.contains(e.relatedTarget))return;
  clearTimeout(hoverTimer);
  hoverTimer=setTimeout(()=>closeOverlay(),500);
 });
 document.addEventListener('click',e=>{
  if(overlay.contains(e.target))return;
  const mark=e.target.closest?.('mark.study-word');
  if(mark){
   if(mark===activeMark&&!overlay.hidden){
    clearTimeout(hoverTimer);
    hoverPreview=false;
   }else{
    wordOverlay(mark);
   }
  }else if(!overlay.hidden&&!e.target.closest?.('#selection-actions')){
   closeOverlay();
  }
 });
 document.addEventListener('keydown',e=>{
  if(e.key==='Escape'&&(activeMark||controller||!overlay.hidden)){
   closeOverlay(overlay.contains(document.activeElement));
  }
  if((e.key==='Enter'||e.key===' ')&&e.target.matches?.('mark.study-word')){
   e.preventDefault();
   wordOverlay(e.target);
   if(activeMark===e.target)overlay.querySelector('.close').focus();
  }
 },true);
 authButton.onclick=async()=>{if(!enabled)return;try{await initialise();if(user){await auth.signOut();closeOverlay();}else await ensureUser();updateAuth();}catch{window.elev.toast('Login kunne ikke gennemføres. Kontrollér domæne og Google-login.')}};
 window.vocabulary={async enable(value){const changed=enabled!==value;enabled=value;if(!enabled){menu.hidden=true;closeOverlay();unsub?.();unsub=null;clearMarks();return;}try{await initialise();if(!enabled)return;if(changed)refreshSubscription();updateAuth();highlight();}catch{window.elev.toast('Ord-integration er ikke tilgængelig. Læsning og lokale noter virker stadig.');}}};
 window.vocabulary.enable(window.elev.lang==='da');
})();
