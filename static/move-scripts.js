const textArea = document.getElementById("text-area");

// Movement Buttons
function moveNorth(callback, callback2) {
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
        console.log('moveNorth(): response', response);
        if (response.xpos === -1 && response.ypos === -1) {
            textArea.innerHTML += 'Forbidden\n\n'
        } else {
            textArea.innerHTML += 'Moved North...\n';
            textArea.innerHTML += response.description + "\n\n";
            callback();
            callback2();
        }
        textArea.scrollTop = textArea.scrollHeight;
    })
} // moveNorth()

function moveEast(callback, callback2) {
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
        console.log('moveEast(): response', response);
        if (response.xpos === -1 && response.ypos === -1) {
            textArea.innerHTML += 'Forbidden\n\n'
        } else {
            textArea.innerHTML += 'Moved East...\n';
            textArea.innerHTML += response.description + "\n\n";
            callback();
            callback2();
        }
        textArea.scrollTop = textArea.scrollHeight;
    })
} // moveEast()

function moveSouth(callback, callback2) {
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
        console.log('moveSouth(): response', response);
        if (response.xpos === -1 && response.ypos === -1) {
            textArea.innerHTML += 'Forbidden\n\n'
        } else {
            textArea.innerHTML += 'Moved South...\n';
            textArea.innerHTML += response.description + "\n\n";
            callback();
            callback2();
        }
        textArea.scrollTop = textArea.scrollHeight;
    })
} // moveSouth()

function moveWest(callback, callback2) {
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
        console.log('moveWest(): response', response);
        if (response.xpos === -1 && response.ypos === -1) {
            textArea.innerHTML += 'Forbidden\n\n'
        } else {
            textArea.innerHTML += 'Moved West...\n';
            textArea.innerHTML += response.description + "\n\n";
            callback();
            callback2();
        }
        textArea.scrollTop = textArea.scrollHeight;
    })
} // moveWest()