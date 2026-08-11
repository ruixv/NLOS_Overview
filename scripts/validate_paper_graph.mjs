import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';

const require=createRequire(import.meta.url);
const Graph=require('../assets/paper-graph-data.js');
const root=path.resolve(path.dirname(new URL(import.meta.url).pathname),'..');
const read=(p)=>fs.readFileSync(path.join(root,p),'utf8');

const bibliographyCandidates=[
  'egbib.bib',
  'egbib_merged_20260711.bib',
  'egbib_20260811_learning_sampling_updates.bib'
];
const sources=bibliographyCandidates.filter(p=>fs.existsSync(path.join(root,p))).map(p=>({name:p,text:read(p)}));
if(!sources.length) throw new Error('No bibliography source files found');

const result=Graph.buildFromTexts(read('index.html'),sources);
const {graph,stats,audit}=result;
console.log(JSON.stringify({stats,audit},null,2));

const nodeById=new Map(graph.nodes.map(n=>[n.id,n]));
const top=graph.edges.slice().sort((a,b)=>b.weight-a.weight).slice(0,20).map(e=>({
  weight:e.weight,
  confidence:e.confidence,
  source:nodeById.get(e.source)?.title,
  target:nodeById.get(e.target)?.title,
  sharedAuthors:e.authors.map(k=>graph.authorMap.get(k)?.display||k)
}));
console.log('\nTop shared-author edges:');
for(const e of top) console.log(`- ${e.weight} | ${e.source} <-> ${e.target} | ${e.sharedAuthors.join('; ')}`);

if(!audit.ok){
  console.error('\nGraph integrity audit failed:');
  for(const c of audit.checks.filter(c=>!c.ok)) console.error(`- ${c.name}: ${c.detail}`);
  process.exit(1);
}
if(stats.edges<20) throw new Error(`Expected a non-trivial collaboration graph; got ${stats.edges} edges`);
if(stats.bibMatched<100) throw new Error(`Bibliography coverage unexpectedly low: ${stats.bibMatched} matched nodes`);
console.log(`\nPASS: ${stats.nodes} nodes, ${stats.bibMatched} BibTeX-matched nodes, ${stats.edges} verified co-author edges.`);
