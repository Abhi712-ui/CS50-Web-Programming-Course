let counter = 0;

function count() {
    counter += 1;
    display = document.querySelector('h1');
    display.innerHTML = counter;

    if (counter % 10 === 0) {
        alert(`You have reached ${counter}`)
    }
}
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
});