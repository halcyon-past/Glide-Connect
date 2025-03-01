document.getElementById("userInputButton").addEventListener("click", getUserInput);
        
document.getElementById("userInput").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        getUserInput();
    }
});

eel.expose(addUserMsg);
eel.expose(addAppMsg);

function addUserMsg(msg) {
    const element = document.getElementById("messages");
    element.innerHTML += '<div class="message from">' + msg + '</div>';
    element.scrollTop = element.scrollHeight;
}

function addAppMsg(msg) {
    const element = document.getElementById("messages");
    element.innerHTML += '<div class="message to">' + msg + '</div>';
    element.scrollTop = element.scrollHeight;
}

function getUserInput() {
    const element = document.getElementById("userInput");
    const msg = element.value;
    if (msg.length != 0) {
        element.value = "";
        eel.getUserInput(msg);
    }
}

// Animated background
function createAnimatedBackground() {
    const shapes = document.querySelectorAll('.shape');
    shapes.forEach(shape => {
        shape.style.transform = `translate(${Math.random() * 100}px, ${Math.random() * 100}px)`;
    });
}

createAnimatedBackground();
setInterval(createAnimatedBackground, 10000);