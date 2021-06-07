const textArea = document.getElementById("text-area");

// Movement Buttons
function moveNorth(callback) {
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
        if (response.xpos === -1 && response.ypos === -1) {
            textArea.innerHTML += 'Forbidden\n\n'
        } else {
            textArea.innerHTML += 'Moved North...\n';
            textArea.innerHTML += response.description + "\n\n";
        }
        textArea.scrollTop = textArea.scrollHeight;
        callback();
    })
}

function moveEast(callback) {
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
        console.log(response);if (response.xpos === -1 && response.ypos === -1) {
            textArea.innerHTML += 'Forbidden\n\n'
        } else {
            textArea.innerHTML += 'Moved East...\n';
            textArea.innerHTML += response.description + "\n\n";
        }
        textArea.scrollTop = textArea.scrollHeight;
        callback();
    })
}

function moveSouth(callback) {
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
        if (response.xpos === -1 && response.ypos === -1) {
            textArea.innerHTML += 'Forbidden\n\n'
        } else {
            textArea.innerHTML += 'Moved South...\n';
            textArea.innerHTML += response.description + "\n\n";
        }
        textArea.scrollTop = textArea.scrollHeight;
        callback();
    })
}

function moveWest(callback) {
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
        if (response.xpos === -1 && response.ypos === -1) {
            textArea.innerHTML += 'Forbidden\n\n'
        } else {
            textArea.innerHTML += 'Moved West...\n';
            textArea.innerHTML += response.description + "\n\n";
        }
        textArea.scrollTop = textArea.scrollHeight;
        callback();
    })
}

// Keybindings
document.addEventListener('keydown', function(e) {
    e.preventDefault();
    if (e.key === 'ArrowUp' || e.code === 'ArrowUp') {
        moveNorth(showMap); // callbacks to guarantee order
        showCombat();
    } else if (e.key === 'ArrowRight' || e.code === 'ArrowRight') {
        moveEast(showMap);
        showCombat();
    } else if (e.key === 'ArrowDown' || e.code === 'ArrowDown') {
        moveSouth(showMap);
        showCombat();
    } else if (e.key === 'ArrowLeft' || e.code === 'ArrowLeft') {
        moveWest(showMap);
        showCombat();
    }
});