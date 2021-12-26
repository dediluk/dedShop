"use strict";

function post_view() {
    const post = document.querySelector('.post-view');

    find_parent_elem()

    function find_parent_elem() {
        let parent_elem = document.querySelector('.row');

        parent_elem.addEventListener("click", fill_text_in_post)
    }

    function fill_text_in_post(event) {
        if (event.target && (event.target.classList.contains('post-preview') ||
            event.target.classList.contains('post-preview-title') ||
            event.target.classList.contains('post-preview-text'))) {


            if (event.target.classList.contains('post-preview')) {  //если нажимать на край блока
                document.querySelector(".pop-up-window").style.backgroundColor =
                    event.target.style.backgroundColor
            } else {  //если нажимать на текст или заголовок
                document.querySelector(".pop-up-window").style.backgroundColor =
                    event.target.parentNode.parentNode.style.backgroundColor;
            }


            document.querySelector('.post-view-title').textContent =
                event.target.parentNode.querySelector('.post-preview-title').textContent
            document.querySelector('.post-view-text').textContent =
                event.target.parentNode.querySelector('.post-preview-text').getAttribute('data-post-text')
            document.querySelector('.post-date').textContent =
                event.target.parentNode.querySelector('.date').textContent
            show_post()
        }
    }


    function show_post() {
        document.body.style.overflow = 'hidden';

        post.classList.add('show')
        post.classList.remove('hide')
    }


    function close_post() {
        post.classList.add('hide')
        post.classList.remove('show')
    }

    document.addEventListener('keydown', function (event) {
        if (event.code === "Escape" && post.classList.contains('show')) close_post();
    })

    post.addEventListener('click', (e) => {
            if (e.target === post || e.target.getAttribute('data-close') == "") {
                close_post();
            }
        }
    )
}

post_view()
