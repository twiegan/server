const continueButton = document.getElementById("continue-button");
const positionTracker = document.getElementById("position-tracker");
const inventoryButton = document.getElementById("button-holder-inventory");
const mapButton = document.getElementById("button-holder-map");
const statsButton = document.getElementById("button-holder-stats");
const user = document.getElementById("user");

continueButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    const buttonType = continueButton.value;
    if (buttonType === "Back") {
        location.replace("/" + username + "/game/" + position);
    } else {
        location.replace("/" + username + "/game/" + (position + 1));
    }
});

inventoryButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace( "/" + username + "/game/" + position + "/inventory");
})

mapButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace( "/" + username + "/game/" + position + "/map");
})

statsButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace( "/" + username + "/game/" + position + "/stats");
})