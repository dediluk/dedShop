"use strict";

// Окрашиваем превью в летние цвета
function makePreviewMoreColorful() {
    let previewElements = document.querySelectorAll('.post-preview'),
        colors = ['#ECDB54', '#E94B3C', '#6F9FD8', '#944743', '#DBB1CD', '#EC9787', '#00A591', '#6B5B95', '#BC70A4',
            '#DC4C46', '#D2691E', '#006E51', '#F7CAC9', '#F7786B', '#79C753', '#CE3175']
    previewElements.forEach( (element) => {
        element.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)]
    })
}

makePreviewMoreColorful()