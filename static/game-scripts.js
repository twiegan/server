const positionTracker = document.getElementById("position-tracker");
const user = document.getElementById("user");
const inventoryButton = document.getElementById("button-holder-inventory");
const mapButton = document.getElementById("button-holder-map");
const statsButton = document.getElementById("button-holder-stats");
const northButton = document.getElementById("north-button");
const eastButton = document.getElementById("east-button");
const southButton = document.getElementById("south-button");
const westButton = document.getElementById("west-button");

// Info Screen Buttons
inventoryButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace( "/" + username + "/game/" + position + "/inventory");
});

mapButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace( "/" + username + "/game/" + position + "/map");
});

statsButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace( "/" + username + "/game/" + position + "/stats");
});

// Movement Buttons
northButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace("/" + username + "/game/" + (position+1));
});

eastButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace("/" + username + "/game/" + (position+1));
});

southButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace("/" + username + "/game/" + (position+1));
});

westButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace("/" + username + "/game/" + (position+1));
});

// Keybindings
document.addEventListener('keydown', function(e) {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
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
