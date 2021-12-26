'use strict';

var f = document.querySelector('.row');
f.addEventListener('click', (event) => {
    console.log(document.documentElement.clientWidth, event.target.clientWidth)
    if (event.target && (event.target.classList.contains('post-preview'))){

        event.target.style.transform = 'translateY(' + (((parseInt(document.documentElement.clientHeight / 2, 10)))
        - (parseInt(event.target.clientHeight / 2, 10))) + 'px)';
        event.target.style.transform += 'translateX(' + (((parseInt(document.documentElement.clientWidth / 2, 10)))
            - (parseInt(event.target.clientWidth / 2, 10))) + 'px)';
        console.log(document.documentElement.clientWidth / 2, event.target.clientWidth/2)
    }
})

// f.addEventListener('click', function(ev){
//     console.log(ev.target)
//     ev.target.style.transform = 'translateY('+(((parseInt(document.documentElement.clientHeight /2, 10))) - (parseInt(ev.target.clientWidth / 2, 10)))+'px)';
//     ev.target.transform += 'translateX('+(((parseInt(document.documentElement.clientWidth / 2, 10))) - (parseInt(ev.target.clientWidth / 2, 10)))+'px)';
// },false);


// let vid = document.querySelector('.red_block')
// vid.addEventListener('click', (e) => {
//     let x = ((parseInt(document.documentElement.clientHeight / 2, 10)) - (parseInt(vid.clientHeight / 2, 10))) + 'px',
//     y = ((parseInt(document.documentElement.clientWidth / 2, 10)) - (parseInt(vid.clientWidth / 2, 10))) + 'px';
//
//     // while(true){
//     //     vid.style.top += 1
//     // }
// })
// console.log(vid.height)
//
//
// let scrollHeight = Math.max(
//     document.body.scrollHeight, document.documentElement.scrollHeight,
//     document.body.offsetHeight, document.documentElement.offsetHeight,
//     document.body.clientHeight, document.documentElement.clientHeight
// );
