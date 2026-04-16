document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.flash').forEach(function (el) {
        setTimeout(function () { el.remove(); }, 4000);
    });
});

function togglePw(btn) {
    var input = btn.closest('.input-wrap').querySelector('input');
    input.type = input.type === 'password' ? 'text' : 'password';
}
