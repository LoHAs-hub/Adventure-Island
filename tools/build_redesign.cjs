// Reproducible single-file build, using Node's bundled parser (no npm install).
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const acorn=require('internal/deps/acorn/acorn/dist/acorn');
const root=path.resolve(__dirname,'..'),read=n=>fs.readFileSync(path.join(root,n),'utf8');
let html=read('game/source/baseline.html');
if(crypto.createHash('sha256').update(html).digest('hex')!=='63a018e13af27da20a7493918ecb3719faba09a1059a36fb6dd0da96529c09be')throw Error('Baseline drift');
const script=html.match(/<script>\s*([\s\S]*?)<\/script>/)[1],ast=acorn.parse(script,{ecmaVersion:'latest'}),nodes=new Map(ast.body.filter(n=>n.type==='FunctionDeclaration').map(n=>[n.id.name,n]));
for(const n of ast.body)if(n.type==='VariableDeclaration'&&n.declarations.some(d=>d.id.name==='icoImg'))nodes.set('icoImg',n);
const functions=new Map(),extra=[];
for(const name of ['assets.js','art.js','gear.js','ui.js','effects.js']){const content=read('game/redesign/'+name),tree=acorn.parse(content,{ecmaVersion:'latest'});let ranges=[];for(const n of tree.body)if(n.type==='FunctionDeclaration'&&nodes.has(n.id.name)){functions.set(n.id.name,content.slice(n.start,n.end));ranges.push([n.start,n.end])}let c=content;for(const[a,b]of ranges.reverse())c=c.slice(0,a)+c.slice(b);extra.push(c)}
const entry={render:'RUI.tick();',show:'',saveG:'',update:'',onSnap:'',onNet:'',autoStep:'',renderGrowth:''},tail={show:'RUI.shown(id);',saveG:'LiveGear.commit();',renderGrowth:'RUI.legacyChanged();'};
let edits=[];
for(const [name,n]of nodes){if(functions.has(name)){edits.push([n.start,n.end,functions.get(name)]);continue}if(entry[name])edits.push([n.body.start+1,n.body.start+1,entry[name]]);if(tail[name])edits.push([n.body.end-1,n.body.end-1,';'+tail[name]])}
let js=script;for(const[a,b,v]of edits.sort((a,b)=>b[0]-a[0]))js=js.slice(0,a)+v+js.slice(b);
const patch=(a,b)=>{const count=js.split(a).length-1;if(count!==1)throw Error('Patch expected once '+a.slice(0,100)+' got '+count);js=js.replace(a,b)};
patch('if(e.code==="Escape"&&G&&!G.over){','if(RUI.routeKey(e))return;\n  if(e.code==="Escape"&&G&&!G.over){');
// Single equipment / mutation paths remain the original, with fixed batch IDs.
patch('GR.dc=Date.now();renderGrowth();return}GR.dc=0;let d=0,g=0,n=0;const dm=SVD.dmax??3;','GR.dc=Date.now();GR.batchIds=SVD.inv.filter(x=>!x.lk&&x.anc===undefined&&x.ri<=(SVD.dmax??3)).map(x=>x.id);renderGrowth();return}GR.dc=0;let d=0,g=0,n=0;const dm=SVD.dmax??3,confirmed=new Set(GR.batchIds||[]);GR.batchIds=null;');
patch('if(x.lk||x.anc!==undefined||x.ri>dm)return true;','if(!confirmed.has(x.id)||x.lk||x.anc!==undefined||x.ri>dm)return true;');
// Wire dedicated network update packets, preserving all other message branches.
patch('case"full":status(', 'case"gearV4":LiveGear.receive(d);break;\n    case"gearAckV4":LiveGear.ack(d);break;\n    case"actorV4":LiveGear.actor(d);break;\n    case"full":status(');
patch('NET.ok=true;NET.rem=d;if(G&&!G.over&&G.net===1){const f=G.F.find(f=>f.net);if(f&&d.st&&d.st.ci===f.ci)refreshP(f,d.st)}','NET.ok=true;NET.rem=d;LiveGear.register(d);');
patch('netSend("go",{cfg,gid:Date.now()});startGame(cfg);','cfg.gearEpoch=Date.now()+"-"+Math.random().toString(36).slice(2);LiveGear.reset(cfg.gearEpoch);netSend("go",{cfg,gid:Date.now()});startGame(cfg);');
patch('const cfg=d.cfg;resetI(IN);','const cfg=d.cfg;LiveGear.reset(cfg.gearEpoch);resetI(IN);');
patch('if(f.isP&&!f.S)f.S={area:1};','if(f.isP){const authoritative=(G.cfg.stats||[])[pl];if(authoritative){f.S=authoritative;f.ap=apOfP(f.ci,authoritative.look,job,br,authoritative.vis);f.atkT=authoritative.atkT}}\n    if(f.isP&&!f.S)f.S={area:1};');
patch('f.dead=true;f.lives=0;f.hp=0;f.st="dead"','f.dead=true;f.lives=0;f.hp=0;f.st="dead";f.rt=Infinity;f.disconnected=true');
patch('function stepP(f){','function stepP(f){if(f.disconnected)return;');
// Refuse old hello updates during a live match: equipment has its own protocol.
patch('case"hello":if(NET.role!=="host")return;','case"hello":if(NET.role!=="host")return;if(G&&!G.over){if(!NET.ok)netSend("full",0);return}');
// Reuse exact original warning paths for a border pass, without duplicate labels.
patch('for(const p of G.fx)dFx(p);\n  X.restore();','for(const p of G.fx)dFx(p);\n  Art.warningTop();\n  X.restore();');
// Initialize modules before the original load/start sequence.
patch('loadSave();buildKM();offlineGain();',extra.join('\n')+'\nRUI.init();\nloadSave();buildKM();offlineGain();');
fs.writeFileSync(path.join(root,'work/redo/compiled.js'),js);acorn.parse(js,{ecmaVersion:'latest'});
html=html.replace(/<style>[\s\S]*?<\/style>/,()=>'<style>\n'+read('game/redesign/style.css')+'\n</style>');
html=html.replace(/<script>\s*[\s\S]*?<\/script>/,()=>'<script>\n'+js+'\n</script>');
fs.writeFileSync(path.join(root,'game/index.html'),html);console.log('Built original engine + redesign modules:',html.length,'characters');
