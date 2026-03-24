'use strict';

document.addEventListener('DOMContentLoaded', function () {
    const btn = document.getElementById('msgBtn');
    if (btn) {
        btn.addEventListener('click', function () {
            alert('You clicked the button!');
        });
    }
});
