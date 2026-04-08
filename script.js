document.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('msg-btn');

    btn.addEventListener('click', function () {
        var msg = document.getElementById('feedback');
        msg.textContent = 'You clicked the button!';
    });
});