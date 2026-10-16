<!doctype html> <html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#05050b">
<title>KODEX — Оформление заявки</title>
<style>
:root{--bg:#05050b;--panel:#0c1020;--muted:#9ba5c4;--pink:#ff00b8;--purple:#7b2cff;--blue:#00d9ff;--line:#25304e}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 80% 10%,#17103a 0,transparent 35%),radial-gradient(ellipse at 10% 80%,#170b32 0,transparent 32%),var(--bg);color:#f8f9ff;font-family:Inter,system-ui,-apple-system,Segoe UI,Arial,sans-serif;min-height:100vh}
body:before{content:"";position:fixed;inset:0;pointer-events:none;opacity:.24;background-image:radial-gradient(#ff00b8 1px,transparent 1.5px),radial-gradient(#00d9ff 1px,transparent 1.5px);background-size:22px 22px,29px 29px;background-position:0 0,12px 15px;mask-image:linear-gradient(120deg,black,transparent 35%,transparent 70%,black)}
.wrap{width:min(100%,720px);margin:auto;padding:24px 18px 40px;position:relative}
.brand{display:flex;align-items:center;justify-content:center;gap:12px;margin:8px 0 26px}.mark{width:48px;height:48px;position:relative;flex:none}.mark:before{content:"";position:absolute;inset:2px 20px 2px 0;background:linear-gradient(145deg,#ff168d,#7b2cff);clip-path:polygon(0 0,100% 0,35% 42%,100% 100%,48% 100%,0 57%)}.mark:after{content:"";position:absolute;right:0;bottom:1px;width:24px;height:20px;background:linear-gradient(135deg,#168bff,#00e4ff);clip-path:polygon(0 0,100% 100%,25% 100%)}.brand-name{font-size:clamp(23px,5vw,34px);font-weight:900;letter-spacing:2px}.brand-sub{font-size:10px;letter-spacing:4px;color:#00cfff;font-weight:800;margin-top:1px}
.card{border:1px solid #29304d;border-radius:26px;background:linear-gradient(145deg,rgba(14,17,34,.96),rgba(5,7,16,.97));box-shadow:0 0 45px #6a13ff14;padding:clamp(20px,5vw,36px);overflow:hidden}
.kicker{text-transform:uppercase;letter-spacing:2px;color:#aab3d0;font-size:12px;font-weight:800}.step{margin-top:8px;color:#aab3d0;font-weight:700}.step strong{color:#ff26c4}.track{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin:18px 0 28px}.dot{height:5px;border-radius:9px;background:#28324e}.dot.done{background:linear-gradient(90deg,var(--pink),var(--blue));box-shadow:0 0 10px #8b2cff88}
h1{font-size:clamp(27px,6vw,42px);line-height:1.1;margin:0 0 10px;letter-spacing:-.7px} .gradient{background:linear-gradient(90deg,#ff19b9,#8a43ff,#00d9ff);-webkit-background-clip:text;background-clip:text;color:transparent}.hint{color:var(--muted);line-height:1.55;margin:0 0 25px;font-size:15px}
label{display:block;color:#dce1f7;font-weight:650;margin:0 0 9px;font-size:14px}input,textarea{width:100%;border:1px solid #3d4267;border-radius:15px;padding:17px 16px;background:#090d1a;color:#fff;font:inherit;outline:none;transition:.2s}input:focus,textarea:focus{border-color:#9a43ff;box-shadow:0 0 0 3px #8b2cff26,0 0 20px #00d9ff12}textarea{min-height:125px;resize:vertical}::placeholder{color:#727d9c}.field{margin:22px 0}
.options{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:11px}.option{border:1px solid #303957;border-radius:15px;padding:15px 12px;background:#0a0e1d;color:#e7eaff;text-align:left;cursor:pointer;min-height:74px;font:inherit;transition:.18s}.option span{display:block;font-size:12px;color:#8995b7;margin-top:5px}.option.selected{border-color:#b13cff;background:linear-gradient(130deg,#5d0e7940,#006b9740);box-shadow:inset 0 0 0 1px #00d9ff55}
.actions{display:flex;gap:12px;margin-top:28px}.btn{border:0;border-radius:15px;padding:16px 20px;font:inherit;font-weight:800;cursor:pointer}.primary{flex:1;color:#fff;background:linear-gradient(100deg,#ec00c8,#722cff 52%,#00cfff);box-shadow:0 8px 26px #8b2cff35}.secondary{background:#151a2d;color:#dbe2ff;border:1px solid #303957}.btn:disabled{opacity:.4;cursor:not-allowed}
.review{display:grid;gap:0;border:1px solid #2c3452;border-radius:15px;overflow:hidden;margin-top:22px}.review-row{padding:13px 15px;border-bottom:1px solid #252d48;display:grid;grid-template-columns:120px 1fr;gap:12px}.review-row:last-child{border:0}.review-row .key{color:#96a1c0;font-size:13px}.review-row .val{overflow-wrap:anywhere}.success{text-align:center;padding:28px 4px}.success-icon{width:70px;height:70px;border-radius:50%;margin:0 auto 20px;display:grid;place-items:center;font-size:32px;background:linear-gradient(135deg,#c400df,#00cfff);box-shadow:0 0 35px #782bff55}
.foot{text-align:center;color:#687493;font-size:12px;margin-top:18px}.hidden{display:none!important}
@media(max-width:440px){.wrap{padding:16px 12px 28px}.brand{margin:8px 0 18px}.card{border-radius:21px}.options{grid-template-columns:1fr}.option{min-height:62px}.review-row{grid-template-columns:95px 1fr}.actions .btn{padding:15px 13px}}
</style>
</head>
<body>
<main class="wrap">
  <header class="brand" aria-label="KODEX Media Group">
    <div class="mark"></div><div><div class="brand-name">KODEX</div><div class="brand-sub">MEDIA GROUP</div></div>
  </header>
  <section class="card" id="app">
    <div class="kicker">Оформление заявки</div>
    <div class="step" id="stepLabel">ШАГ <strong>1</strong> ИЗ 7</div>
    <div class="track" id="track"></div>
    <div id="screen"></div>
  </section>
  <div class="foot">KODEX MEDIA GROUP · Ваши идеи — наши технологии</div>
</main>
<script>
const services=[
 ["AI-видео","Ролики, реклама, визуальные истории"],
 ["Чат-бот","Telegram-боты и автоматизация общения"],
 ["ИИ-агенты","Умные помощники для задач бизнеса"],
 ["Автоматизация","Оптимизация рабочих процессов"],
 ["Сайт или приложение","Цифровые продукты и интерфейсы"],
 ["Другое","Опишите, что вам нужно"]
];
const data={name:"",project:"",service:"",task:"",budget:"",deadline:"",contact:""};
let step=1,finished=false;
const screen=document.getElementById("screen"),stepLabel=document.getElementById("stepLabel"),track=document.getElementById("track");
function renderTrack(){track.innerHTML="";for(let i=1;i<=7;i++){let d=document.createElement("div");d.className="dot"+(i<=step?" done":"");track.appendChild(d)}}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}
function field(label,key,placeholder,type="text",optional=false){return `<div class="field"><label for="${key}">${label}${optional?' <span style="color:#8b96b8;font-weight:400">(необязательно)</span>':''}</label><input id="${key}" name="${key}" type="${type}" placeholder="${placeholder}" value="${escapeHtml(data[key])}" ${optional?'':'required'} autocomplete="off"></div>`}
function render(){
 renderTrack();stepLabel.innerHTML=`ШАГ <strong>${step}</strong> ИЗ 7`;
 let content="";
 if(step===1)content=`<h1>Давайте начнём<br><span class="gradient">с начала</span></h1><p class="hint">Как к вам обращаться?</p>${field("Ваше имя","name","Введите ваше имя")}`;
 if(step===2)content=`<h1>Ваш проект</h1><p class="hint">Расскажите, для какой компании или идеи нужна услуга.</p>${field("Название компании или проекта","project","Введите название или напишите «Нет»")}`;
 if(step===3)content=`<h1>Выберите <span class="gradient">услугу</span></h1><p class="hint">Что вы хотите создать или улучшить?</p><div class="options">${services.map(([n,d])=>`<button type="button" class="option ${data.service===n?'selected':''}" data-service="${n}">${n}<span>${d}</span></button>`).join("")}</div>`;
 if(step===4)content=`<h1>Расскажите о задаче</h1><p class="hint">Что нужно сделать и какой результат вы хотите получить?</p><div class="field"><label for="task">Описание задачи</label><textarea id="task" placeholder="Например: ИИ-видео длительностью 15 секунд для рекламы продукта" required>${escapeHtml(data.task)}</textarea></div>`;
 if(step===5)content=`<h1>Ваш <span class="gradient">бюджет</span></h1><p class="hint">Укажите примерную сумму. Это поможет предложить подходящее решение.</p>${field("Планируемый бюджет","budget","Например: 50000 ₸")}<button type="button" class="option ${!data.budget?'selected':''}" id="skipBudget">Пропустить<span>Пока не определился(-ась)</span></button>`;
 if(step===6)content=`<h1>Когда нужен результат?</h1><p class="hint">Укажите желаемый срок выполнения.</p>${field("Желаемый срок","deadline","Например: за 7 дней или до 1 ноября")}<button type="button" class="option ${!data.deadline?'selected':''}" id="skipDeadline">Пропустить<span>Срок пока не определён</span></button>`;
 if(step===7)content=`<h1>Оставьте <span class="gradient">контакт</span></h1><p class="hint">Куда с вами связаться по заявке?</p>${field("Telegram или номер телефона","contact","@username или +7 700 000-00-00")}<p class="hint" style="font-size:12px;margin:10px 0 0">Не отправляйте пароли или коды подтверждения.</p>`;
 screen.innerHTML=content+`<div class="actions">${step>1?'<button class="btn secondary" id="back">Назад</button>':''}<button class="btn primary" id="next">${step===7?'Проверить заявку':'Продолжить'} →</button></div>`;
 screen.querySelectorAll("[data-service]").forEach(b=>b.onclick=()=>{data.service=b.dataset.service;render()});
 const b=document.getElementById("back");if(b)b.onclick=()=>{saveCurrent();step--;render()};
 document.getElementById("next").onclick=()=>{if(!saveCurrent())return;if(step<7){step++;render()}else review()};
 const sb=document.getElementById("skipBudget");if(sb)sb.onclick=()=>{data.budget="";step++;render()};
 const sd=document.getElementById("skipDeadline");if(sd)sd.onclick=()=>{data.deadline="";step++;render()};
}
function saveCurrent(){
 if(step===3){if(!data.service){alert("Пожалуйста, выберите услугу.");return false}return true}
 const el=document.getElementById(["","name","project","","task","budget","deadline","contact"][step]);
 if(!el)return true;
 const value=el.value.trim();
 if(step===1&&!value){alert("Введите, пожалуйста, ваше имя.");el.focus();return false}
 if(step===2&&!value){alert("Введите название проекта или напишите «Нет».");el.focus();return false}
 if(step===4&&!value){alert("Опишите задачу несколькими словами.");el.focus();return false}
 if(step===7&&!value){alert("Укажите Telegram или номер телефона для связи.");el.focus();return false}
 data[el.id]=value;return true;
}
function review(){
 stepLabel.textContent="ПОСЛЕДНИЙ ШАГ · ПРОВЕРКА";track.innerHTML='<div class="dot done" style="grid-column:span 7"></div>';
 const rows=[["Имя",data.name],["Компания / проект",data.project||"Нет"],["Услуга",data.service],["Задача",data.task],["Бюджет",data.budget||"Не указан"],["Срок",data.deadline||"Не указан"],["Контакт",data.contact]];
 screen.innerHTML=`<h1>Проверьте <span class="gradient">заявку</span></h1><p class="hint">Убедитесь, что всё указано верно.</p><div class="review">${rows.map(([k,v])=>`<div class="review-row"><div class="key">${k}</div><div class="val">${escapeHtml(v)}</div></div>`).join("")}</div><div class="actions"><button class="btn secondary" id="edit">Изменить</button><button class="btn primary" id="submit">Подтвердить заявку →</button></div><p class="hint" style="font-size:12px;margin:15px 0 0">Это демонстрационный прототип: пока заявка не отправляется на сервер и не приходит администратору.</p>`;
 document.getElementById("edit").onclick=()=>{step=1;render()};
 document.getElementById("submit").onclick=()=>{screen.innerHTML=`<div class="success"><div class="success-icon">✓</div><h1>Отлично!</h1><p class="hint">Вы прошли все шаги формы KODEX. В этой демонстрационной версии отправка заявки отключена. После подключения сервера заявки можно будет получать в Telegram.</p><button class="btn primary" id="restart">Заполнить новую заявку</button></div>`;stepLabel.textContent="ПРОТОТИП";track.innerHTML="";document.getElementById("restart").onclick=()=>{Object.keys(data).forEach(k=>data[k]="");step=1;render()}}
}
render();
</script>
</body>
</html>
