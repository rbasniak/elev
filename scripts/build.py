#!/usr/bin/env python3
"""Generate buildless, trilingual HTML. Usage: python scripts/build.py."""
from pathlib import Path
import sys,json,re,html,os
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'content'))
from course import T,PAGES,CHAPTERS,LANGS
from review import REVIEWS,RECALL
from glossary import GLOSSARY
from videos import VIDEOS
from diagrams import supply
from beginner import GUIDES
E=html.escape
manifest=json.loads((ROOT/'sources/manifest.json').read_text())
LABEL={
'home':T('Alle kurser','All courses','Todos os cursos'),
'course':T('Logistik · første skoleophold','Logistics · first school period','Logística · primeira etapa escolar'),
'chapters':T('Kapitler','Chapters','Capítulos'),
'files':T('Materialer','Materials','Materiais'),
'review':T('Det vigtigste at huske','Key points to remember','Pontos importantes para lembrar'),
'recall':T('Genkald uden at kigge','Recall without looking','Lembre sem consultar'),
'recallintro':T('Læs punkterne. Luk derefter teksten og forklar med dine egne ord. Vend tilbage i morgen, om tre dage og om en uge.','Read the points, then explain them in your own words without looking. Return tomorrow, in three days and in a week.','Leia os pontos e depois explique com suas palavras sem consultar. Revise amanhã, em três dias e em uma semana.'),
'notes':T('Mine noter / svar','My notes / answers','Minhas anotações / respostas'),
'sources':T('Kilder og originalfil','Sources and original file','Fontes e arquivo original'),
'originals':T('Originale materialer','Original materials','Materiais originais'),
'original':T('Åbn originalfil','Open original file','Abrir arquivo original'),
'glossary':T('Fagord · tre sprog','Technical terms · three languages','Termos técnicos · três idiomas'),
'learn':T('Læs, lyt og forstå.','Read, listen and understand.','Leia, ouça e entenda.'),
'intro':T('Dit materiale til skole og praktik, samlet i overskuelige trin. Skift sprog undervejs, og brug dansk til at træne fagord.','Your school and workplace material in manageable steps. Switch languages as you read and use Danish to practise technical vocabulary.','Seu material da escola e da prática em etapas claras. Troque de idioma durante a leitura e use o dinamarquês para treinar os termos técnicos.'),
'courseintro':T('Ni kapitler om varens vej, kundens behov og samspillet mellem service og omkostninger.','Nine chapters on the movement of goods, customer needs and the balance of service and cost.','Nove capítulos sobre o caminho das mercadorias, as necessidades do cliente e o equilíbrio entre serviço e custo.'),
'previous':T('Forrige','Previous','Anterior'),
'next':T('Næste','Next','Próxima'),
'back':T('Til kapitlet','Back to chapter','Voltar ao capítulo'),
'contents':T('På denne side','On this page','Nesta página'),
'notesaved':T('Gemmes automatisk på denne enhed.','Saved automatically on this device.','Salvo automaticamente neste dispositivo.'),
'supplement':T('Supplerende studiestøtte · ingen originalfiler i denne mappe.','Supplemental study support · no original files in this folder.','Apoio complementar · esta pasta não tinha arquivos originais.'),
'read':T('Markér som læst','Mark as read','Marcar como lido'),
'copy':T('Kopiér mine svar','Copy my answers','Copiar minhas respostas'),
'listen':T('Lyt','Listen','Ouvir'),
'video':T('Videolektioner til selvstudium','Video lessons for self-study','Aulas para estudar sem assistir aos vídeos'),
'watch':T('Originalvideo (valgfri)','Original video (optional)','Vídeo original (opcional)'),
'capture':T('Bearbejdet studielektion med supplerende forklaringer og egne øveeksempler.','Adapted lesson with additional explanations and original practice examples.','Aula adaptada com explicações complementares e exemplos didáticos próprios.'),
'guide':T('Eget studiemateriale · ikke en officiel IKEA-side','Personal study material · not an official IKEA site','Material pessoal de estudo · não é site oficial da IKEA'),
'complete':T('Filer læst','Files read','Arquivos lidos')}

def ui(key,tag='span',**attrs):
 attr=' '.join(f'{E(k)}="{E(v)}"' for k,v in attrs.items())
 return ''.join(f'<{tag} data-ui-lang="{l}" {attr}{" hidden" if l!="da" else ""}>{E(LABEL[key][l])}</{tag}>' for l in LANGS)

terms=re.compile(r'(?<![\w])('+ '|'.join(re.escape(x) for x in sorted(GLOSSARY,key=len,reverse=True))+r')(?![\w])',re.I)
lookup={x.casefold():v for x,v in GLOSSARY.items()}
def inline(value,l):
 s=E(value)
 if l!='da':
  s=terms.sub(lambda m:f'<span class="tech-term" tabindex="0" data-meaning="{E(lookup[html.unescape(m[0]).casefold()][0 if l=="en" else 1])}" title="{E(lookup[html.unescape(m[0]).casefold()][0 if l=="en" else 1])}">{m[0]}</span>',s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
 return s

def body(text,l):
 lines=text.strip().splitlines();out=[];i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if ' | ' in line:
   rows=[]
   while i<len(lines) and ' | ' in lines[i]:rows.append([c.strip() for c in lines[i].split(' | ')]);i+=1
   out.append('<div class="table-scroll"><table><thead><tr>'+''.join('<th scope="col">'+inline(c,l)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(c,l)+'</td>' for c in row)+'</tr>' for row in rows[1:])+'</tbody></table></div>');continue
  if line.startswith('- '):
   lis=[]
   while i<len(lines) and lines[i].strip().startswith('- '):lis.append('<li>'+inline(lines[i].strip()[2:],l)+'</li>');i+=1
   out.append('<ul>'+''.join(lis)+'</ul>');continue
  out.append('<p>'+inline(line,l)+'</p>');i+=1
 return ''.join(out)

def textinput(key,l):
 safe=key.replace('/','-').replace('.','-')
 return f'<div class="answer-box"><label for="{safe}-{l}">{LABEL["notes"][l]}</label><textarea id="{safe}-{l}" data-answer-key="{safe}" spellcheck="true" aria-describedby="save-{safe}-{l}"></textarea><small class="save-state" id="save-{safe}-{l}" data-save-key="{safe}">{LABEL["notesaved"][l]}</small></div>'

def section(heading,content,l,anchor,kind='text',key=None):
 listen=f'<button class="section-listen" type="button" aria-label="Lyt til {E(heading)}">▷ Lyt</button>' if l=='da' else ''
 return f'<section class="study-section {kind}" data-anchor="{anchor}" id="{anchor}-{l}"><h2>{E(heading)}</h2>{listen}<div class="paragraph-text">{body(content,l)}</div>{textinput(key,l) if key else ""}</section>'

for p in PAGES:
 m=manifest[p['source']];p['chapter']=m['chapter'];p['path']=m['page'];p['original']=m['original']
PAGES[0]['videos']=['FD2ShcUtLkE','smzGqoS-na8']
PAGES.sort(key=lambda p:p['source'])
index=[{k:p[k] for k in ['title','chapter','path','original']}|{'text':{l:' '.join(s['heading'][l]+' '+s['body'][l] for s in p['sections'] if s['kind']!='answer') for l in LANGS}} for p in PAGES]
(ROOT/'assets/search-index.js').write_text('window.ELEV_INDEX = '+json.dumps(index,ensure_ascii=False)+';\n')

def rel(path,here):return os.path.relpath(ROOT/path,ROOT/here).replace(os.sep,'/')

def shell(path,title,panels,chapter=0):
 here=Path(path).parent.as_posix();root=rel('',here);root='' if root=='.' else root+'/'
 nav=''
 for i,c in enumerate(CHAPTERS,1):
  nav+=f'<a href="{root}logistik/{i:02d}/index.html" class="{"active" if chapter==i else ""}"'+(' aria-current="page"' if chapter==i else '')+f'><span class="nav-number">{i:02d}</span>'+''.join(f'<span data-ui-lang="{l}"'+(' hidden' if l!='da' else '')+'>'+E(c[l])+'</span>' for l in LANGS)+'</a>'
 content=f'''<!doctype html><html lang="da"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><meta name="description" content="Trilingual logistics study material with Danish audio and vocabulary practice."><title>{E(title)} · elev</title><link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{root}assets/style.css?v=1"><script>try{{document.documentElement.dataset.preferredLang=JSON.parse(localStorage.getItem('elev:lang'))||'da'}}catch{{}}</script><style>html[data-preferred-lang=en] .lang-panel[data-lang=da],html[data-preferred-lang=pt] .lang-panel[data-lang=da]{{display:none}}</style></head><body data-lang="da" data-page="{path}" data-root="{root}">
<a class="sr-only" href="#main">Spring til indhold / Skip to content</a>
<header class="topbar"><button class="menu-toggle" type="button" aria-label="Menu" aria-expanded="false" aria-controls="sidebar">☰</button><a class="brand" href="{root}index.html"><span class="brand-icon">e</span>elev<span class="brand-sub">studie &amp; praktik</span></a><div class="search-box"><input id="search" type="search" autocomplete="off" aria-label="Søg i materialet" placeholder="Søg i materialet…"><div class="search-results" id="search-results" hidden></div></div><div class="top-spacer"></div><button class="auth-button" id="vocab-auth" data-da-only type="button">Log ind · ord</button><div class="languages" role="group" aria-label="Language / Sprog / Idioma"><button type="button" data-set-lang="da" aria-pressed="true" lang="da">DA</button><button type="button" data-set-lang="en" aria-pressed="false" lang="en">EN</button><button type="button" data-set-lang="pt" aria-pressed="false" lang="pt-BR">PT</button></div></header>
<div class="layout"><aside class="sidebar" id="sidebar"><a class="side-home" href="{root}index.html">← {ui('home')}</a><p class="sidebar-label">LOGISTIK · 01</p><nav aria-label="Kapitler">{nav}</nav><div class="sidebar-bottom"><a href="{root}logistik/index.html">{ui('course')}</a><a href="{root}glossary.html">{ui('glossary')}</a><a href="https://rbasniak.github.io/ov-dansk/" target="_blank" rel="noopener noreferrer" data-da-only>ov-dansk ↗</a>{ui('complete')}<div class="progress-track"><span data-progress-chapter="all"></span></div></div></aside><main class="main" id="main"><div class="content">{panels}<noscript><p class="noscript">JavaScript er nødvendigt for sprogskift, lyd og lokale noter. Alle tekster er statiske. JavaScript is required for language switching, audio and notes.</p></noscript><footer><span>{ui('guide')}</span><button class="folio" type="button" aria-label="Studiestøtte" aria-keyshortcuts="Control+Shift+G">{chapter:02d}</button></footer></div></main></div>
<div class="toast" role="status" aria-live="polite" id="toast" hidden></div><div class="selection-actions" role="toolbar" aria-label="Valgt dansk tekst" id="selection-actions" hidden><button type="button" id="save-selection">＋ Gem</button><button type="button" id="define-selection">Definition</button><button type="button" id="translate-selection">Oversæt</button><button type="button" id="listen-selection">Lyt</button></div><div class="word-overlay" id="word-overlay" role="dialog" aria-label="Ord og betydning" hidden></div>
<script src="{root}assets/search-index.js?v=1"></script><script src="{root}assets/app.js?v=1"></script><script src="{root}assets/vocabulary.js?v=1"></script></body></html>'''
 dest=ROOT/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(content)

def wrap(l,value):return f'<div class="lang-panel" data-lang="{l}" lang="{"pt-BR" if l=="pt" else l}"'+(' hidden' if l!='da' else '')+'>'+value+'</div>'

def crumbs(l,depth,chapter=None):
 root='../'*depth
 s=f'<div class="breadcrumbs"><a href="{root}index.html">{LABEL["home"][l]}</a><span>/</span><a href="{root}logistik/index.html">Logistik</a>'
 if chapter:s+=f'<span>/</span><a href="{root}logistik/{chapter:02d}/index.html">{E(CHAPTERS[chapter-1][l])}</a>'
 return s+'</div>'

def hero(l,title,intro,chapter=None,home=False):
 return f'<div class="hero {"hero-home" if home else ""}" data-anchor="hero"><div class="eyebrow">{"SKOLE & PRAKTIK" if not chapter else f"LOGISTIK / {chapter:02d}"}</div><h1>{E(title)}</h1><p class="intro">{inline(intro,l)}</p></div>'

def cards(l,here):
 s='<div class="cards" data-anchor="chapters">'
 for n,c in enumerate(CHAPTERS,1):
  count=sum(p['chapter']==n for p in PAGES);desc=RECALL[n-1][l]
  s+=f'<a class="card" href="{rel(f"logistik/{n:02d}/index.html",here)}"><span class="card-number">{n:02d}<span class="arrow">↗</span></span><h3>{E(c[l])}</h3><p>{inline(desc,l)}</p><div class="card-footer"><span>{count} '+({'da':'fil','en':'file','pt':'arquivo'} if count==1 else {'da':'filer','en':'files','pt':'arquivos'})[l]+f'</span><span>DA · EN · PT</span></div><div class="progress-track"><span data-progress-chapter="{n}"></span></div></a>'
 return s+'</div>'

panels=''
for l in LANGS:
 s=hero(l,LABEL['learn'][l],LABEL['intro'][l],home=True)
 s+=f'<div class="section-head"><h2>{LABEL["home"][l]}</h2><span class="eyebrow">01 / 01</span></div><a class="card" href="logistik/index.html"><span class="card-number">01 <span class="arrow">↗</span></span><h3>{LABEL["course"][l]}</h3><p>{LABEL["courseintro"][l]}</p><div class="card-footer"><span>9 '+{'da':'kapitler · 20 filer','en':'chapters · 20 files','pt':'capítulos · 20 arquivos'}[l]+'</span><span>5 '+{'da':'videoer','en':'videos','pt':'vídeos'}[l]+'</span></div><div class="progress-track"><span data-progress-chapter="all"></span></div></a>'
 s+=section(T('Sådan bruger du materialet','How to use this material','Como usar o material')[l],T('Vælg et kapitel og læs på det sprog, du forstår bedst. Skift til dansk ved samme afsnit. Brug Lyt til at øve faglige sætninger. Markér dansk tekst for at gemme ord, slå op, oversætte eller lytte. Noter og læsemarkeringer gemmes lokalt på enheden.','Choose a chapter and read in the language you understand best. Switch to Danish at the same passage. Use Lyt to practise sentences. Select Danish text to save words, look up, translate or listen. Notes and read markers are saved locally on this device.','Escolha um capítulo e leia no idioma que entende melhor. Mude para dinamarquês no mesmo trecho. Use Lyt para treinar frases. Selecione texto dinamarquês para salvar palavras, consultar, traduzir ou ouvir. Notas e marcações ficam salvas neste dispositivo.')[l],l,'how')
 s+=section(T('Se øvelsessvar','See exercise answers','Como ver as resoluções')[l],T('Prøv øvelsen først. Dobbeltklik derefter på kapitelnummeret nederst til højre for at se de svar, der findes på siden.','Try the exercise first. Then double-click the chapter number at the bottom right to reveal any model answers on the page.','Tente a atividade primeiro. Depois dê duplo clique no número do capítulo, no canto inferior direito, para ver as resoluções disponíveis naquela página.')[l],l,'show-answers')
 s+=f'<div class="pager"><a href="source/">{LABEL["originals"][l]} ↗</a></div>'
 panels+=wrap(l,s)
shell('index.html','elev · studie & praktik',panels)
# A harmless alias accommodates the spelling used in the request.
(ROOT/'index.httml').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=index.html"><a href="index.html">elev</a>')
panels=''
for l in LANGS:
 s=crumbs(l,1)+hero(l,LABEL['course'][l],LABEL['courseintro'][l])+f'<div class="section-head"><h2>{LABEL["chapters"][l]}</h2><span class="eyebrow">01—09</span></div>'+cards(l,'logistik')
 s+=f'<div class="pager"><a href="../source/">{LABEL["originals"][l]} ↗</a></div>'
 panels+=wrap(l,s)
shell('logistik/index.html','Logistik',panels)

for n,c in enumerate(CHAPTERS,1):
 items=[p for p in PAGES if p['chapter']==n];panels=''
 for l in LANGS:
  s=crumbs(l,2)+hero(l,c[l],RECALL[n-1][l],n)
  if not items:s+=section(T('Supplerende kapitel','Supplemental chapter','Capítulo complementar')[l],LABEL['supplement'][l],l,'empty','notice')
  else:
   s+=f'<div class="section-head"><h2>{LABEL["files"][l]}</h2><span class="eyebrow">{len(items):02d}</span></div><div class="lesson-list" data-anchor="files">'
   for i,p in enumerate(items,1):s+=f'<a class="lesson-row" href="{Path(p["path"]).name}"><span class="file-number">{i:02d}</span><span><h3>{E(p["title"][l])}</h3><small>{E(p["original"])}</small></span><span class="arrow">↗</span></a>'
   s+='</div>'
  s+=section(LABEL['review'][l],REVIEWS[n-1][l],l,'remember','review')
  s+=section(LABEL['recall'][l],LABEL['recallintro'][l]+'\n'+RECALL[n-1][l],l,'recall','text',f'recall-{n}')
  s+='<div class="review-schedule">'
  for day,labels in [(0,T('I dag','Today','Hoje')),(1,T('I morgen','Tomorrow','Amanhã')),(3,T('Om 3 dage','In 3 days','Em 3 dias')),(7,T('Om 7 dage','In 7 days','Em 7 dias'))]:s+=f'<label><input type="checkbox" data-review-key="review-{n}-{day}">{labels[l]}</label>'
  s+='</div>'
  if n<9:s+=f'<div class="pager"><a href="../{n+1:02d}/index.html">{LABEL["next"][l]} → {E(CHAPTERS[n][l])}</a></div>'
  panels+=wrap(l,s)
 shell(f'logistik/{n:02d}/index.html',c['da'],panels,n)

for pos,p in enumerate(PAGES):
 n=p['chapter'];panels='';m=manifest[p['source']]
 for l in LANGS:
  s=crumbs(l,2,n)+hero(l,p['title'][l],p['intro'][l],n)
  s+='<div class="toolbar">'
  if l=='da':s+='<button type="button" data-stop>■ Stop</button><label class="toolbar-label">Tempo <select data-speed aria-label="Talehastighed"><option value="0.8">0,8×</option><option value="0.95" selected>0,95×</option><option value="1.1">1,1×</option></select></label>'
  s+=f'<button type="button" class="copy-answers">{LABEL["copy"][l]}</button><button type="button" class="complete" data-page="{p["path"]}" aria-pressed="false">{LABEL["read"][l]}</button></div>'
  s+=f'<details class="section-toc"><summary>{LABEL["contents"][l]}</summary>'
  guide=GUIDES.get(p['source'])
  if guide:
   s+=f'<a href="#beginner-{l}">{E(T(*guide[0])[l])}</a>'
  for i,sec in enumerate(p['sections']):
   if sec['kind']!='answer':s+=f'<a href="#s{i}-{l}">{E(sec["heading"][l])}</a>'
  for vid in p.get('videos', []):
   s+=f'<a href="#video-{vid}-{l}">{E(VIDEOS[vid]["title"])}</a>'
  s+='</details>'
  if guide:
   s+=section(T(*guide[0])[l],T(*guide[1])[l],l,'beginner')
  for i,sec in enumerate(p['sections']):
   s+=section(sec['heading'][l],sec['body'][l],l,f's{i}',sec['kind'],f'{p["path"]}-{sec.get("answer_index",i)}' if sec['kind']=='task' else None)
   if p.get('chart',{}).get('section')==i:
    names=T(['Materialer','Produktion','Udgående','Marketing','Service'],['Materials','Production','Outbound','Marketing','Service'],['Materiais','Produção','Saída','Marketing','Serviço'])[l]
    s+='<div class="study-section answer chart-bars" data-anchor="chart" role="img" aria-label="'+E(T('Omkostningsfordeling: 300, 200, 40, 20 og 10 kroner','Cost distribution: 300, 200, 40, 20 and 10 kroner','Distribuição de custos: 300, 200, 40, 20 e 10 coroas')[l])+'">'
    for name,val in zip(names,p['chart']['values']):s+=f'<div class="chart-bar"><span>{name}</span><div class="bar"><span style="width:{val/300*100}%"></span></div><span>{val} DKK</span></div>'
    s+='</div>'
  if p.get('videos'):
   s+=f'<section class="study-section" data-anchor="videos"><h2>{LABEL["video"][l]}</h2>'
   for vid in p['videos']:
    v=VIDEOS[vid]
    s+=f'<article class="video" id="video-{vid}-{l}" data-anchor="video-{vid}"><h3>{E(v["title"])}</h3>'
    s+=f'<div class="paragraph-text">{body(v["summary"][l],l)}</div>'
    for i,(heading,lesson) in enumerate(v['topics']):
     s+=f'<div data-anchor="video-{vid}-{i}"><h4>{E(heading[l])}</h4>'
     if l=='da':
      speech=lesson[l].replace('- ', '')
      s+=f'<button type="button" class="video-listen" aria-label="Lyt til {E(heading[l])}" data-video-tts="{E(speech)}">▷ Lyt</button>'
     s+=f'<div class="paragraph-text">{body(lesson[l],l)}</div></div>'
    s+=f'<div class="video-links"><a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener noreferrer">▶ {LABEL["watch"][l]}</a>'
    for ts,label in v['timestamps']:
     mm,ss=map(int,ts.split(':'));s+=f'<a href="https://www.youtube.com/watch?v={vid}&amp;t={mm*60+ss}" target="_blank" rel="noopener noreferrer">{ts}</a>'
    if v.get('transcript'):
     label=T('Transskription', 'Transcript', 'Transcrição')[l]
     s+=f'<a href="{E(v["transcript"])}" target="_blank" rel="noopener noreferrer">{label}</a>'
    s+=f'</div><p class="video-status">{LABEL["capture"][l]}</p></article>'
   s+='</section>'
  if p['source'] in [8,15,17]:s+=supply(l,'supply')
  if p['source']==17:s+=supply(l,'order')
  s+=f'<details class="sources" data-anchor="sources"><summary>{LABEL["sources"][l]}</summary><ul><li><a href="../../{m["asset"]}" target="_blank" rel="noopener noreferrer">{LABEL["original"][l]} · {E(m["original"])}</a></li>'
  for link in m.get('links',[]):s+=f'<li><a href="{E(link["url"])}" target="_blank" rel="noopener noreferrer">{E(link["url"])}</a> — {E(link["status"][l])}</li>'
  s+='</ul></details><div class="pager">'
  if pos>0:s+=f'<a href="{rel(PAGES[pos-1]["path"],str(Path(p["path"]).parent))}">← {LABEL["previous"][l]}</a>'
  s+=f'<a href="index.html">{LABEL["back"][l]}</a>'
  if pos<len(PAGES)-1:s+=f'<a href="{rel(PAGES[pos+1]["path"],str(Path(p["path"]).parent))}">{LABEL["next"][l]} →</a>'
  s+='</div>';panels+=wrap(l,s)
 shell(p['path'],p['title']['da'],panels,n)

panels=''
for l in LANGS:
 s=hero(l,LABEL['originals'][l],T('De 20 kursusfiler, ordnet efter kapitel.','The 20 course files, grouped by chapter.','Os 20 arquivos do curso, organizados por capítulo.')[l])
 for n,chapter in enumerate(CHAPTERS,1):
  items=[m for m in manifest if m['chapter']==n]
  if not items:
   continue
  s+=f'<section class="study-section" data-anchor="chapter-{n}"><h2>{n:02d} · {E(chapter[l])}</h2><ul>'
  for m in items:
   s+=f'<li><a href="../{E(m["asset"])}">{E(m["original"])}</a> · <a href="../{E(m["page"])}">{LABEL["learn"][l]}</a></li>'
  s+='</ul></section>'
 panels+=wrap(l,s)
shell('source/index.html','Originale materialer',panels)

panels=''
for l in LANGS:
 s=crumbs(l,0)+hero(l,LABEL['glossary'][l],T('Lær ordene i sammenhæng. Markér et dansk ord for at gemme din egen betydning i ov-dansk.','Learn words in context. Select Danish text to save your own meaning in ov-dansk.','Aprenda no contexto. Selecione texto em dinamarquês para salvar seu significado no ov-dansk.')[l])+'<div class="dictionary">'
 for i,(term,meanings) in enumerate(sorted(GLOSSARY.items(),key=lambda x:x[0].casefold())):
  s+=f'<div class="dictionary-item" data-anchor="term{i}"><div class="paragraph-text"><strong>{E(term)}</strong><p>'+('EN: '+E(meanings[0])+'<br>PT: '+E(meanings[1]) if l=='da' else E(meanings[0 if l=='en' else 1]))+'</p></div>'+(f'<button type="button" data-video-tts="{E(term)}" class="video-listen">▷ Lyt</button>' if l=='da' else '')+'</div>'
 s+='</div>';panels+=wrap(l,s)
shell('glossary.html','Fagord',panels)
(ROOT/'.nojekyll').touch()
print(f'Built {len(PAGES)} material pages, {len(CHAPTERS)} chapter pages, 4 navigation, sources and glossary pages; {len(GLOSSARY)} terms; 5 self-study video lessons.')
