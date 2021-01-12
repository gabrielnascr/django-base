
// Only testing the javascript link in html for look if are correct
function changeColor() {
    var randomColor = Math.floor(Math.random()*16777215).toString(16);
    const h1 = document.getElementById('text');

    h1.style.color = `#${randomColor}`;
}

var button = document.getElementById('button');
button.addEventListener('click', changeColor);
