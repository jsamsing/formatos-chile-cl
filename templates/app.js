(function(){
var GA='__GA4__';
function ev(n,o){if(window.gtag)gtag('event',n,o||{})}
var g=document.querySelector('[data-gen]');
if(g){var tpl=g.querySelector('[data-plantilla]').textContent.trim(),ej={};JSON.parse(g.querySelector('[data-ejemplos]').textContent).forEach(function(c){ej[c[0]]=c[2]});
var doc=g.querySelector('[data-doc]'),ins=g.querySelectorAll('input'),usado=false;
function texto(){var v={};ins.forEach(function(i){v[i.name]=i.value.trim()||ej[i.name]});return tpl.replace(/\{(\w+)\}/g,function(m,k){return v[k]!=null?v[k]:m})}
function pinta(){doc.textContent=texto()}
ins.forEach(function(i){i.addEventListener('input',function(){pinta();if(!usado){usado=true;ev('formato_start',{formato:location.pathname})}})});pinta();
g.querySelector('[data-copiar]').onclick=function(){var t=texto();(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){this.textContent='¡Copiado!'}.bind(this),function(){var r=document.createRange();r.selectNodeContents(doc);var s=getSelection();s.removeAllRanges();s.addRange(r)});ev('formato_copiar',{formato:location.pathname})};
g.querySelector('[data-word]').onclick=function(){var t=texto().replace(/&/g,'&amp;').replace(/</g,'&lt;').split('\n').map(function(l){return '<p style="margin:0 0 6pt;font-family:Arial;font-size:11pt">'+(l||'&nbsp;')+'</p>'}).join('');
var b=new Blob(['<html><head><meta charset="utf-8"></head><body>'+t+'</body></html>'],{type:'application/msword'}),a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=location.pathname.replace(/\//g,'')+'.doc';a.click();ev('formato_word',{formato:location.pathname})};
g.querySelector('[data-pdf]').onclick=function(){ev('formato_pdf',{formato:location.pathname});window.print()};}
window.ckShow=function(){document.getElementById('ck').hidden=false};
window.ckSet=function(v){try{localStorage.setItem('fo_ck',v?'g':'d')}catch(e){}document.getElementById('ck').hidden=true;if(v)ga()};
function ga(){if(!GA||location.hostname!=='formatos-chile.cl'||window.gtag)return;var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id='+GA;document.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config',GA)}
var k=null;try{k=localStorage.getItem('fo_ck')}catch(e){}
if(k==='g')ga();else if(!k&&GA)setTimeout(ckShow,1500);
document.addEventListener('click',function(e){var a=e.target.closest('[data-ev]');if(a&&window.gtag)gtag('event',a.dataset.ev,{cta_label:a.dataset.label})});
})();
