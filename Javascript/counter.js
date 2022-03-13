if (!localStorage.getItem('counter')) {

}

let counter = 0;

function count() {
    counter += 1;
    display = document.querySelector('h1');
    display.innerHTML = counter;

}
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
    setInterval(count, 1000);
});