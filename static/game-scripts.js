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
            inventory: true,
            map: false,
            stats: false
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
            inventory: false,
            map: true,
            stats: false
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        let i;
        let j;
        let toPrint;
        for (i = 0; i < response.length; i++) {
            toPrint += "<br>"
            for (j = 0; j < response.length; j++) {
                toPrint += response[i][j];
            }
        }
        infoArea.innerHTML = toPrint;
    })
}

function showStats() {
        fetch('/stats', {
        body: JSON.stringify({
            inventory: false,
            map: false,
            stats: true
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
    textArea.innerHTML += 'Moved North\n';
    textArea.scrollTop = textArea.scrollHeight;
}

function moveEast() {
    textArea.innerHTML += 'Moved East\n';
    textArea.scrollTop = textArea.scrollHeight;
}

function moveSouth() {
    textArea.innerHTML += 'Moved South\n';
    textArea.scrollTop = textArea.scrollHeight;
}

function moveWest() {
    textArea.innerHTML += 'Moved West\n';
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
