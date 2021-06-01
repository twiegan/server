const textArea = document.getElementById("text-area");
const northButton = document.getElementById("north-button");
const eastButton = document.getElementById("east-button");
const southButton = document.getElementById("south-button");
const westButton = document.getElementById("west-button");

// Movement Buttons
function moveNorth() {
    fetch('/move', {
        body: JSON.stringify({
            direction: "north"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log(response);
        textArea.innerHTML += 'Moved North\n';
    })
    textArea.scrollTop = textArea.scrollHeight;
}

function moveEast() {
    fetch('/move', {
        body: JSON.stringify({
            direction: "east"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log(response);
        textArea.innerHTML += 'Moved East\n';
    })
    textArea.scrollTop = textArea.scrollHeight;
}

function moveSouth() {
    fetch('/move', {
        body: JSON.stringify({
            direction: "south"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log(response);
        textArea.innerHTML += 'Moved South\n';
    })
    textArea.scrollTop = textArea.scrollHeight;
}

function moveWest() {
    fetch('/move', {
        body: JSON.stringify({
            direction: "west"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log(response);
        textArea.innerHTML += 'Moved West\n';
    })
    textArea.scrollTop = textArea.scrollHeight;
}

// Keybindings
document.addEventListener('keydown', function(e) {
    e.preventDefault();
    if (e.key === 'ArrowUp' || e.code === 'ArrowUp') {
        northButton.click();
    } else if (e.key === 'ArrowRight' || e.code === 'ArrowRight') {
        eastButton.click();
    } else if (e.key === 'ArrowDown' || e.code === 'ArrowDown') {
        southButton.click();
    } else if (e.key === 'ArrowLeft' || e.code === 'ArrowLeft') {
        westButton.click();
    }
});