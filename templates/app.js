(function(){
var GA='__GA4__';
function ev(n,o){if(window.gtag)gtag('event',n,o||{})}
var g=document.querySelector('[data-gen]');
if(g){var tpl=g.querySelector('[data-plantilla]').textContent.trim(),ej={};JSON.parse(g.querySelector('[data-ejemplos]').textContent).forEach(function(c){ej[c[0]]=c[2]});
var doc=g.querySelector('[data-doc]'),ins=g.querySelectorAll('input,textarea'),usado=false;
function texto(){var v={};ins.forEach(function(i){v[i.name]=i.value.trim()||ej[i.name]});return tpl.replace(/\{(\w+)\}/g,function(m,k){return v[k]!=null?v[k]:m})}
function pinta(){doc.textContent=texto()}
ins.forEach(function(i){i.addEventListener('input',function(){pinta();if(!usado){usado=true;ev('formato_start',{formato:location.pathname})}})});pinta();
g.querySelector('[data-copiar]').onclick=function(){var t=texto();(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){this.textContent='¡Copiado!'}.bind(this),function(){var r=document.createRange();r.selectNodeContents(doc);var s=getSelection();s.removeAllRanges();s.addRange(r)});ev('formato_copiar',{formato:location.pathname})};
g.querySelector('[data-word]').onclick=function(){var t=texto().replace(/&/g,'&amp;').replace(/</g,'&lt;').split('\n').map(function(l){return '<p style="margin:0 0 6pt;font-family:Arial;font-size:11pt">'+(l||'&nbsp;')+'</p>'}).join('');
var b=new Blob(['<html><head><meta charset="utf-8"></head><body>'+t+'</body></html>'],{type:'application/msword'}),a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=location.pathname.replace(/\//g,'')+'.doc';a.click();ev('formato_word',{formato:location.pathname})};
g.querySelector('[data-pdf]').onclick=function(){ev('formato_pdf',{formato:location.pathname});window.print()};}
var G=document.querySelector('[data-gantt]');
if(G){var T=[['Diseño y presupuesto',1,2,'Arquitecta'],['Permisos municipales',2,2,'Administración'],['Obra gruesa',4,2,'Contratista'],['Instalaciones eléctricas y sanitarias',5,2,'Contratista'],['Terminaciones y pintura',7,1,'Contratista'],['Apertura',8,1,'Dueño']],gUsado=false;
var box=G.querySelector('[data-g-tareas]'),ch=G.querySelector('[data-g-chart]'),ini=G.querySelector('[data-g-ini]'),uni=G.querySelector('[data-g-uni]'),proy=G.querySelector('[data-g-proy]');
var d0=new Date();d0.setDate(d0.getDate()+((8-d0.getDay())%7||7));ini.value=d0.toISOString().slice(0,10);
function esc(t){return String(t).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;')}
function filas(){box.innerHTML='<div class="g-h"><span>Tarea</span><span>Inicio</span><span>Duración</span><span>Responsable</span><span></span></div>'+T.map(function(t,i){return '<div class="g-f" data-i="'+i+'"><input aria-label="Tarea" value="'+esc(t[0])+'"><input aria-label="Inicio" type="number" min="1" max="60" value="'+t[1]+'"><input aria-label="Duración" type="number" min="1" max="60" value="'+t[2]+'"><input aria-label="Responsable" value="'+esc(t[3])+'"><button type="button" class="sec" aria-label="Quitar tarea">✕</button></div>'}).join('')}
function lee(){T=[].map.call(box.querySelectorAll('.g-f'),function(f){var x=f.querySelectorAll('input');return [x[0].value,Math.max(1,+x[1].value||1),Math.max(1,+x[2].value||1),x[3].value]})}
function fecha(k){var d=new Date((ini.value||d0.toISOString().slice(0,10))+'T12:00:00');d.setDate(d.getDate()+(k-1)*(+uni.value));return ('0'+d.getDate()).slice(-2)+'/'+('0'+(d.getMonth()+1)).slice(-2)}
function tabla(xls){var n=Math.max.apply(null,T.map(function(t){return t[1]+t[2]-1}).concat([1])),u=+uni.value===7?'Sem ':'Día ';
var h='<table class="tb gt"><thead><tr><th scope="col">Tarea</th><th scope="col">Responsable</th>';for(var k=1;k<=n;k++)h+='<th scope="col">'+u+k+'<br><small>'+fecha(k)+'</small></th>';h+='</tr></thead><tbody>';
T.forEach(function(t){h+='<tr><th scope="row">'+esc(t[0])+'</th><td>'+esc(t[3])+'</td>';for(var k=1;k<=n;k++){var on=k>=t[1]&&k<t[1]+t[2];h+=on?(xls?'<td bgcolor="#1f6feb" style="background:#1f6feb"></td>':'<td class="on"></td>'):'<td></td>'}h+='</tr>'});return h+'</tbody></table>'}
function pinta(){lee();ch.innerHTML='<p class="g-p">'+esc(proy.value)+'</p>'+tabla()}
filas();pinta();
G.addEventListener('input',function(){pinta();if(!gUsado){gUsado=true;ev('formato_start',{formato:location.pathname})}});
box.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;lee();T.splice(+b.parentNode.dataset.i,1);filas();pinta()});
G.querySelector('[data-g-add]').onclick=function(){lee();var f=T.length?T[T.length-1]:['',0,1,''];T.push(['Nueva tarea',f[1]+f[2],1,'']);filas();pinta()};
G.querySelector('[data-g-xls]').onclick=function(){lee();var b=new Blob(['<html><head><meta charset="utf-8"></head><body><h3>'+esc(proy.value)+'</h3>'+tabla(true)+'</body></html>'],{type:'application/vnd.ms-excel'}),a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='carta-gantt.xls';a.click();ev('formato_excel',{formato:location.pathname})};
G.querySelector('[data-g-pdf]').onclick=function(){ev('formato_pdf',{formato:location.pathname});window.print()};}
window.ckShow=function(){document.getElementById('ck').hidden=false};
window.ckSet=function(v){try{localStorage.setItem('fo_ck',v?'g':'d')}catch(e){}document.getElementById('ck').hidden=true;if(v)ga()};
function ga(){if(!GA||location.hostname!=='formatos-chile.cl'||window.gtag)return;var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id='+GA;document.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config',GA)}
var k=null;try{k=localStorage.getItem('fo_ck')}catch(e){}
if(k==='g')ga();else if(!k&&GA)setTimeout(ckShow,1500);
document.addEventListener('click',function(e){var a=e.target.closest('[data-ev]');if(a&&window.gtag)gtag('event',a.dataset.ev,{cta_label:a.dataset.label})});
})();
