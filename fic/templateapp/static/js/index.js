function popupToggle(){
    let popup = document.getElementById('popups');
    let baground = document.getElementById('popup__bg');
    let body = document.getElementById('body');
    body.classList.toggle('active');
    baground.classList.toggle('active');
    popup.classList.toggle('active');
}

function hambHandler(e){
    e.preventDefault();
    // Переключаем стили элементов при клике
    popup.classList.toggle("open");
    hamb.classList.toggle("active");
    body.classList.toggle("noscroll");
    renderPopup();
}

// Скрипт для бургер меню;
let hamb =document.querySelector("#hamb");
let popup = document.querySelector("#popup");
let body = document.body;


// Клонируем меню для того чтобы задать стили для мобильной версии
let menu = document.querySelector("#menu").cloneNode(1);


// При клике на меню гамбургера вызываем функцию hambHandler
hamb.addEventListener("click",hambHandler);

// описываем функцию hambHandler


// Здесь мы редерим элементы в поп ап из клона

function renderPopup(){
    popup.appendChild(menu);
}

// Код для закрытия менюпри нажатие на ссылку
let links = Array.from(menu.children);

// функци для меню вызываемая при клике

links.forEach((link)=>{
    link.addEventListener("click",closeOnClick);
});

// Закрываем попап при клике меню
 function closeOnClick(){
     popup.classList.remove("open");
     hamb.classList.remove("active");
     body.classList.remove("nonscroll");
 }