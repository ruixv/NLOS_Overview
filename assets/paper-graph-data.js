(function(root,factory){
  const api=factory();
  if(typeof module==='object'&&module.exports) module.exports=api;
  root.NLOSGraphData=api;
})(typeof globalThis!=='undefined'?globalThis:this,function(){
  'use strict';

  function cleanLatex(s){
    return String(s||'')
      .replace(/\\(?:textit|textbf|emph|mathrm|mathbf|operatorname|url)\s*\{([^{}]*)\}/g,'$1')
      .replace(/\\['"`^~=.uvHckrbd]\s*\{?([A-Za-z])\}?/g,'$1')
      .replace(/\\(?:ae|AE)\b/g,m=>m.includes('A')?'AE':'ae')
      .replace(/\\(?:oe|OE)\b/g,m=>m.includes('O')?'OE':'oe')
      .replace(/\\ss\b/g,'ss')
      .replace(/[{}$]/g,' ')
      .replace(/\\&/g,'&')
      .replace(/\\_/g,'_')
      .replace(/\s+/g,' ')
      .trim();
  }

  function normText(s){
    return cleanLatex(s).normalize('NFKD').replace(/[\u0300-\u036f]/g,'')
      .toLowerCase().replace(/[^a-z0-9]+/g,' ').trim().replace(/\s+/g,' ');
  }
  function normTitle(s){return normText(s);}
  function normDoi(s){
    return String(s||'').trim().toLowerCase()
      .replace(/^https?:\/\/(?:dx\.)?doi\.org\//,'')
      .replace(/[{}]/g,'').replace(/[?#].*$/,'').trim();
  }
  function doiFromUrl(url){const m=String(url||'').match(/doi\.org\/(.+)$/i);return m?normDoi(m[1]):'';}

  function extractPaperArray(source){
    const m=/const\s+papers\s*=\s*\[/.exec(source);
    if(!m) throw new Error('Could not locate const papers = [...] in index.html');
    const start=source.indexOf('[',m.index); let depth=0,quote=null,escape=false,end=-1;
    for(let i=start;i<source.length;i++){
      const ch=source[i];
      if(quote){if(escape){escape=false;continue;} if(ch==='\\'){escape=true;continue;} if(ch===quote)quote=null; continue;}
      if(ch==='"'||ch==="'"||ch==='`'){quote=ch;continue;}
      if(ch==='[') depth++; else if(ch===']'&&--depth===0){end=i;break;}
    }
    if(end<0) throw new Error('Could not parse paper array boundaries');
    return Function('"use strict";return ('+source.slice(start,end+1)+');')();
  }

  function dedupePapers(arr){
    const out=[], seen=new Set();
    for(const p of arr||[]){
      if(!p||!p.title) continue;
      const k=normTitle(p.title)+'|'+String(p.year||'');
      if(seen.has(k)) continue;
      seen.add(k);
      out.push({...p,id:'p'+out.length});
    }
    return out;
  }

  function classify(p){
    const c=String(p.cat||'').toLowerCase(), t=normText([p.title,p.key,p.venue].join(' ')), all=c+' '+t;
    if(/\b(acoustic|ultrasound|sonar|audio)\b/.test(all)) return 'acoustic';
    if(/\b(rf|radar|mmwave|millimeter wave|terahertz|thz|isac|ris|wireless|uwb|fmcw|isar|sar imaging)\b/.test(all)) return 'rf';
    if(c.split(/\s+/).includes('passive')) return 'passive';
    if(c.split(/\s+/).includes('learning')||/\b(neural|transformer|diffusion|mamba|network|deep learning|metaformer|gnn|operator learning|learnable)\b/.test(t)) return 'learning';
    if(/\b(dataset|survey|benchmark|code)\b/.test(all)) return 'resource';
    if(c.split(/\s+/).includes('active')) return 'active';
    return 'other';
  }

  function findClose(text,start,open,close){
    let depth=1,q=null,escape=false;
    for(let i=start+1;i<text.length;i++){
      const ch=text[i];
      if(q){if(escape){escape=false;continue;} if(ch==='\\'){escape=true;continue;} if(ch===q)q=null; continue;}
      if(ch==='"'){q=ch;continue;}
      if(ch===open)depth++; else if(ch===close&&--depth===0)return i;
    }
    return -1;
  }
  function topComma(s){
    let depth=0,q=false,escape=false;
    for(let i=0;i<s.length;i++){
      const ch=s[i];
      if(q){if(escape){escape=false;continue;} if(ch==='\\'){escape=true;continue;} if(ch==='"')q=false; continue;}
      if(ch==='"'){q=true;continue;} if(ch==='{')depth++; else if(ch==='}')depth=Math.max(0,depth-1); else if(ch===','&&depth===0)return i;
    }
    return -1;
  }
  function parseFields(body){
    const tags={}; let i=0;
    while(i<body.length){
      while(i<body.length&&/[\s,]/.test(body[i]))i++;
      const ns=i; while(i<body.length&&/[A-Za-z0-9_:-]/.test(body[i]))i++;
      if(i===ns){i++;continue;}
      const name=body.slice(ns,i).toUpperCase(); while(i<body.length&&/\s/.test(body[i]))i++;
      if(body[i]!=='='){while(i<body.length&&body[i]!==',')i++;continue;}
      i++; while(i<body.length&&/\s/.test(body[i]))i++;
      let val='';
      if(body[i]==='{'){
        const end=findClose(body,i,'{','}'); if(end<0)break; val=body.slice(i+1,end); i=end+1;
      }else if(body[i]==='"'){
        let j=i+1,esc=false; for(;j<body.length;j++){if(esc){esc=false;continue;} if(body[j]==='\\'){esc=true;continue;} if(body[j]==='"')break;}
        val=body.slice(i+1,j); i=j+1;
      }else{
        const st=i; while(i<body.length&&body[i]!==',')i++; val=body.slice(st,i).trim();
      }
      tags[name]=val.trim(); while(i<body.length&&body[i]!==',')i++; if(body[i]===',')i++;
    }
    return tags;
  }
  function parseBib(text,sourceName){
    const entries=[]; let i=0;
    while((i=text.indexOf('@',i))>=0){
      let j=i+1; while(j<text.length&&/\s/.test(text[j]))j++;
      const ts=j; while(j<text.length&&/[A-Za-z]/.test(text[j]))j++;
      const type=text.slice(ts,j).toLowerCase(); while(j<text.length&&/\s/.test(text[j]))j++;
      const open=text[j]; if(open!=='{'&&open!=='('){i=j+1;continue;}
      const close=open==='{'?'}':')', end=findClose(text,j,open,close); if(end<0)break;
      const body=text.slice(j+1,end), comma=topComma(body);
      if(comma>0&&!['comment','preamble','string'].includes(type)){
        entries.push({key:body.slice(0,comma).trim(),type,tags:parseFields(body.slice(comma+1)),source:sourceName||''});
      }
      i=end+1;
    }
    return entries;
  }

  function mergeBibSources(sourceTexts){
    const byKey=new Map(), entries=[];
    for(const src of sourceTexts||[]){
      const parsed=parseBib(src.text||'',src.name||'');
      for(const e of parsed){
        const doi=normDoi(e.tags.DOI||''), title=normTitle(e.tags.TITLE||''), year=String(e.tags.YEAR||'');
        const key=doi?'doi:'+doi:(title?'title:'+title+'|'+year:'key:'+String(e.key||'').toLowerCase());
        if(!key||key==='key:') continue;
        if(byKey.has(key)){
          const old=byKey.get(key), merged={...old,tags:{...old.tags,...e.tags},source:e.source||old.source,key:e.key||old.key};
          byKey.set(key,merged);
        }else byKey.set(key,e);
      }
    }
    for(const e of byKey.values()) entries.push(e);
    return entries;
  }

  function tokenJaccard(a,b){
    const A=new Set(normTitle(a).split(' ').filter(Boolean)), B=new Set(normTitle(b).split(' ').filter(Boolean));
    if(!A.size||!B.size)return 0; let inter=0; for(const x of A)if(B.has(x))inter++;
    return inter/(A.size+B.size-inter);
  }

  function buildBibIndex(entries){
    const byDoi=new Map(), byTitle=new Map(), byYear=new Map();
    for(const e of entries){
      const doi=normDoi(e.tags.DOI||''), title=normTitle(e.tags.TITLE||''), year=String(e.tags.YEAR||'');
      if(doi)byDoi.set(doi,e);
      if(title){if(!byTitle.has(title))byTitle.set(title,[]);byTitle.get(title).push(e);}
      if(year){if(!byYear.has(year))byYear.set(year,[]);byYear.get(year).push(e);}
    }
    return {byDoi,byTitle,byYear};
  }

  function matchBib(p,index){
    const doi=doiFromUrl(p.url); if(doi&&index.byDoi.has(doi)) return {entry:index.byDoi.get(doi),method:'doi'};
    const title=normTitle(p.title), exact=index.byTitle.get(title)||[];
    if(exact.length===1) return {entry:exact[0],method:'title'};
    if(exact.length>1){const same=exact.filter(e=>String(e.tags.YEAR||'')===String(p.year||'')); if(same.length===1)return {entry:same[0],method:'title+year'};}
    const pool=index.byYear.get(String(p.year||''))||[];
    let best=null,bestScore=0,second=0;
    for(const e of pool){const score=tokenJaccard(p.title,e.tags.TITLE||''); if(score>bestScore){second=bestScore;bestScore=score;best=e;}else if(score>second)second=score;}
    if(best&&bestScore>=0.94&&bestScore-second>=0.035) return {entry:best,method:'fuzzy-title',score:bestScore};
    return {entry:null,method:'none'};
  }

  function parseAuthor(raw){
    raw=cleanLatex(raw); if(!raw)return null;
    let family='',given='';
    if(raw.includes(',')){const p=raw.split(',').map(x=>x.trim());family=p.shift()||'';given=p.join(' ').trim();}
    else{const p=raw.split(/\s+/).filter(Boolean);if(p.length<2)return null;family=p.pop();given=p.join(' ');}
    const familyN=normText(family), tokens=normText(given).split(' ').filter(Boolean); if(!familyN||!tokens.length)return null;
    const initials=tokens.map(t=>t[0]).join(''), fullTokens=tokens.filter(t=>t.length>1);
    const fullCanonical=fullTokens.length?fullTokens.join(' ')+' '+familyN:'';
    const firstFull=fullTokens.length?fullTokens[0]:'';
    return {display:raw,family:familyN,tokens,initials,signature:familyN+'|'+initials,firstSignature:firstFull?familyN+'|'+firstFull:'',fullCanonical};
  }
  function splitAuthors(field){return String(field||'').split(/\s+and\s+/i).map(parseAuthor).filter(Boolean);}

  function resolveAuthorIdentities(papers){
    const sigFull=new Map(), firstFull=new Map();
    for(const p of papers)for(const a of p._rawAuthors||[]){
      if(a.fullCanonical){
        if(!sigFull.has(a.signature))sigFull.set(a.signature,new Set()); sigFull.get(a.signature).add(a.fullCanonical);
        if(a.firstSignature){if(!firstFull.has(a.firstSignature))firstFull.set(a.firstSignature,new Set()); firstFull.get(a.firstSignature).add(a.fullCanonical);}
      }
    }
    let matched=0,resolvedOccurrences=0,initialResolved=0,ambiguousInitials=0;
    for(const p of papers){
      p.fullAuthors=[];
      for(const a of p._rawAuthors||[]){
        let canonical='',confidence='';
        if(a.fullCanonical){canonical=a.fullCanonical;confidence='full-name';}
        else{
          const set=sigFull.get(a.signature);
          if(set&&set.size===1){canonical=[...set][0];confidence='unique-initial-expansion';initialResolved++;}
          else if((!set||set.size===0)&&a.initials.length>=2){
            canonical='initial:'+a.signature;confidence='exact-multi-initial';
          }else ambiguousInitials++;
        }
        if(canonical){p.fullAuthors.push({canonical,display:a.display,confidence,signature:a.signature});resolvedOccurrences++;}
      }
      const uniq=new Map();for(const a of p.fullAuthors)if(!uniq.has(a.canonical))uniq.set(a.canonical,a);p.fullAuthors=[...uniq.values()];
      p.hasVerifiedAuthors=p.fullAuthors.length>0;if(p.hasVerifiedAuthors)matched++;
    }
    return {matched,resolvedOccurrences,initialResolved,ambiguousInitials};
  }

  function enrichPapers(papers,bibEntries){
    const idx=buildBibIndex(bibEntries); let bibMatched=0; const methods={doi:0,title:0,'title+year':0,'fuzzy-title':0,none:0};
    for(const p of papers){
      p.family=classify(p); const m=matchBib(p,idx); p.bib=m.entry; p.matchMethod=m.method; methods[m.method]=(methods[m.method]||0)+1;
      p._rawAuthors=m.entry?splitAuthors(m.entry.tags.AUTHOR||''):[]; if(m.entry)bibMatched++;
    }
    const authorStats=resolveAuthorIdentities(papers);
    return {bibMatched,methods,...authorStats};
  }

  function buildGraph(papers){
    const authorMap=new Map();
    for(const n of papers)for(const a of n.fullAuthors||[]){
      if(!authorMap.has(a.canonical))authorMap.set(a.canonical,{display:a.display,confidence:a.confidence,papers:[]});
      authorMap.get(a.canonical).papers.push(n.id);
    }
    const pairs=new Map();
    for(const [author,info] of authorMap){
      const ids=[...new Set(info.papers)];
      for(let i=0;i<ids.length;i++)for(let j=i+1;j<ids.length;j++){
        const a=ids[i],b=ids[j],k=a<b?a+'|'+b:b+'|'+a;
        if(!pairs.has(k))pairs.set(k,{source:a,target:b,authors:[],confidence:'high'});
        const edge=pairs.get(k);edge.authors.push(author);
        if(String(author).startsWith('initial:'))edge.confidence='medium';
      }
    }
    const edges=[...pairs.values()].map(e=>({...e,weight:e.authors.length}));
    const degree=new Map(papers.map(n=>[n.id,0]));
    for(const e of edges){degree.set(e.source,(degree.get(e.source)||0)+1);degree.set(e.target,(degree.get(e.target)||0)+1);}
    for(const n of papers)n.degree=degree.get(n.id)||0;
    return {nodes:papers,edges,authorMap};
  }

  function findNode(nodes,title){const nt=normTitle(title);return nodes.find(n=>normTitle(n.title)===nt)||null;}
  function findEdge(graph,aTitle,bTitle){
    const a=findNode(graph.nodes,aTitle),b=findNode(graph.nodes,bTitle); if(!a||!b)return null;
    return graph.edges.find(e=>(e.source===a.id&&e.target===b.id)||(e.source===b.id&&e.target===a.id))||null;
  }
  function auditGraph(graph,stats){
    const checks=[];
    function add(name,ok,detail){checks.push({name,ok:!!ok,detail});}
    add('node-count',graph.nodes.length>=200,graph.nodes.length+' nodes');
    add('bib-coverage',stats.bibMatched>=100,stats.bibMatched+' matched nodes');
    add('edge-count',graph.edges.length>=20,graph.edges.length+' co-author edges');
    const lct='Confocal Non-Line-of-Sight Imaging Based on the Light-Cone Transform';
    const fk='Wave-Based Non-Line-of-Sight Imaging Using Fast f-k Migration';
    const velten='Recovering Three-Dimensional Shape Around a Corner using Ultrafast Time-of-Flight Imaging';
    const e1=findEdge(graph,lct,fk);add('LCT-fk-positive',!!e1&&e1.weight>=3,e1?e1.weight+' shared authors':'missing edge');
    const e2=findEdge(graph,velten,lct);add('Velten-LCT-negative',!e2,e2?'unexpected edge':'no spurious edge');
    const cm='CMFormer: Non-Line-of-Sight Imaging with a Memory-Efficient MetaFormer Network';
    const dm='Dual-Model Guided Active NLOS Imaging with Under-Scanning Measurements';
    const ncm=findNode(graph.nodes,cm),ndm=findNode(graph.nodes,dm);if(ncm&&ndm){const e=findEdge(graph,cm,dm);add('CMFormer-dual-model-positive',!!e&&e.weight>=3,e?e.weight+' shared authors':'missing edge');}
    const r1='Non-Line-of-Sight mmW Radar Imaging With Adaptive Artifact Cancellation and Target Enhancement';
    const r2='Non-Line-of-Sight mmW SAR Imaging With Equivariant Adaptive Threshold Learning';
    const nr1=findNode(graph.nodes,r1),nr2=findNode(graph.nodes,r2);if(nr1&&nr2){const e=findEdge(graph,r1,r2);add('radar-team-positive',!!e&&e.weight>=4,e?e.weight+' shared authors':'missing edge');}
    return {ok:checks.every(c=>c.ok),checks};
  }

  function buildFromTexts(indexText,bibSources){
    const papers=dedupePapers(extractPaperArray(indexText));
    const bibEntries=mergeBibSources(bibSources);
    const stats=enrichPapers(papers,bibEntries);
    const graph=buildGraph(papers);
    const audit=auditGraph(graph,stats);
    return {graph,stats:{...stats,bibEntries:bibEntries.length,nodes:graph.nodes.length,edges:graph.edges.length},audit};
  }

  return {cleanLatex,normText,normTitle,normDoi,extractPaperArray,dedupePapers,classify,parseBib,mergeBibSources,buildFromTexts,auditGraph,findNode,findEdge};
});
