const textArea = document.getElementById("text-area");
const user = document.getElementById("user");
const infoArea = document.getElementById("game-info");
const inventoryButton = document.getElementById("button-holder-inventory");
const mapButton = document.getElementById("button-holder-map");
const statsButton = document.getElementById("button-holder-stats");
const northButton = document.getElementById("north-button");
const eastButton = document.getElementById("east-button");
const southButton = document.getElementById("south-button");
const westButton = document.getElementById("west-button");

// Info Screen Buttons
function showInventory() {
    fetch('/inventory', {
        body: JSON.stringify({
            info: "inventory"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log(response)
        if (Object.keys(response).length === 0) {
            infoArea.innerHTML = "No items";
        } else {
            infoArea.innerHTML = response;
        }
    })
}

function showMap() {
   fetch('/map', {
        body: JSON.stringify({
            info: "map"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log(response)
        let i;
        let j;
        let toPrint;
        for (i = 0; i < response.length; i++) {
            toPrint += "<br>"
            for (j = 0; j < response[i].length; j++) {
                let curr_char = response[i][j]
                if (curr_char.disc === true) {
                    toPrint += curr_char.disc_char + " ";
                } else {
                    toPrint += curr_char.undisc_char + " ";
                }
            } //for j
        } //for i
        infoArea.innerHTML = toPrint;
    })
}

function showStats() {
        fetch('/stats', {
        body: JSON.stringify({
            info: "stats"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log(response);
        let i;
        let toPrint;
        for (i = 0; i < response.length; i++) {
            toPrint += "<br>" + response[i];
            infoArea.innerHTML = toPrint;
        }
    })
}

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
    if(e.key === 'ArrowUp' || e.code === 'ArrowUp') {
        northButton.click();
    }
    else if(e.key === 'ArrowRight' || e.code === 'ArrowRight') {
        eastButton.click();
    }
    else if(e.key === 'ArrowDown' || e.code === 'ArrowDown') {
        southButton.click();
    }
    else if(e.key === 'ArrowLeft' || e.code === 'ArrowLeft') {
        westButton.click();
    }
    else if(e.key === 'i' || e.code === 'KeyI') {
        inventoryButton.click();
    }
    else if(e.key === 'm' || e.code === 'KeyM') {
        mapButton.click();
    }
    else if(e.key === 's' || e.code === 'KeyS') {
        statsButton.click();
    }
});
