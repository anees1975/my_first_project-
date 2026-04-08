"use strict";

(function () {
    function showMessage() {
        const feedback = document.getElementById('feedback');
        if (!feedback) return;
        feedback.textContent = "You clicked the button!";
    }

    const btn = document.getElementById('msg-btn');
    if (btn) {
        btn.addEventListener('click', showMessage);
    }
})();