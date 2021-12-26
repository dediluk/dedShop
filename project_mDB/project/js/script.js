/*

5) Фильмы должны быть отсортированы по алфавиту */

'use strict';

const movieDB = {
    movies: [
        "Логан",
        "Лига справедливости",
        "Ла-ла лэнд",
        "Одержимость",
        "Скотт Пилигрим против..."
    ]
};

const adv = document.querySelectorAll('.promo__adv img'),
    poster = document.querySelector('.promo__bg'),
    genre = poster.querySelector('.promo__genre'),
    movieList = document.querySelector('.promo__interactive-list');

adv.forEach(item => {
    item.remove();
});

genre.textContent = 'драма';

poster.style.backgroundImage = 'url("img/bg.jpg")';


movieDB.movies.sort();


function addMoviesToPage() {
    movieList.innerHTML = "";
    movieDB.movies.forEach((film, i) => {
        if (film.length > 21) {
            movieList.innerHTML += `
            <li class="promo__interactive-item">${i + 1} ${(film.slice(0,21)) + '...'}
                <div class="delete"></div>
            </li>`;
        } else {
            movieList.innerHTML += `
            <li class="promo__interactive-item">${i + 1} ${film}
                <div class="delete"></div>
            </li>`;
        }

    });
}

const test2 = document.querySelector('.promo__interactive');
test2.addEventListener('click', (event) => {
    console.log(event.currentTarget);
});
addMoviesToPage();

const test = document.querySelector('form > button');
test.addEventListener('click', (event) => {
    console.log(event.currentTarget);
});





const inputButton = document.querySelector('.add'),
        deleteButtons = document.querySelectorAll('.delete');


deleteButtons.forEach((item) => {
    item.addEventListener('click', () => {
        console.log(item.parentElement);
        item.parentElement.remove();
    });
});


inputButton.addEventListener('submit', (event) => {
    event.preventDefault();

    movieDB.movies.push(document.querySelector('.adding__input').value);
    movieDB.movies.sort();

    event.target.reset();

    if (document.querySelector('.yes').previousElementSibling.checked) {
        console.log('Добавляем любимый фильм');
    }

    addMoviesToPage();
    // event.target.reset();
});