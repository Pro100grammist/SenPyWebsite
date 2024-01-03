$(document).ready(function() {
    $('.dropdown-toggle').on('click', function() {
        let $menu = $(this).next('.dropdown-menu');
        $menu.toggleClass('animated');
        $menu.find('li').toggleClass('animate');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    let clickSound = document.getElementById('clickSound');
    let button = document.querySelector('.btn-primary');

    button.addEventListener('click', function() {
        clickSound.currentTime = 0;
        clickSound.play();
    });
});
        