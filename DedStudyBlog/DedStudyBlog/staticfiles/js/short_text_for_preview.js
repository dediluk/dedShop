"use strict";

// Укорачиваем текст поста(123 символа + ...)
function makeShortTextPreview() {
    let textElements = document.querySelectorAll('.post-preview-text')
    textElements.forEach( (element) => {
        element.textContent = element.textContent.slice(0, 122).trim() + '...'
        element.classList.remove('hide')
    })
}

makeShortTextPreview()