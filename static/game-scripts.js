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
    /*
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace( "/" + username + "/game/" + position + "/inventory");

     */
    let inventory = '<table id="inventory-table">' +
                        '<tr><td>1</td></tr>' +
                        '<tr><td>2</td></tr>' +
                        '<tr><td>3</td></tr>' +
                        '<tr><td>|4|</td></tr>' +
                     '</table>';
    infoArea.innerHTML = inventory;
}

function showMap() {
    /*
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace( "/" + username + "/game/" + position + "/map");
    */
    let map = '<table id="map-table">' +
                '<tr><td>|@@@@|</td></tr>' +
                '<tr><td>|%%%%|</td></tr>' +
                '<tr><td>|^^^^|</td></tr>' +
                '<tr><td>|0000|</td></tr>' +
              '</table>';
    infoArea.innerHTML = map;
}

function showStats() {
    /*
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace( "/" + username + "/game/" + position + "/stats");

     */
    let stats = '<table id="stats-table">' +
                    '<tr><td>1s</td></tr>' +
                    '<tr><td>2s</td></tr>' +
                    '<tr><td>3s</td></tr>' +
                    '<tr><td>4s</td></tr>' +
                '</table>';
    infoArea.innerHTML = stats;
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
