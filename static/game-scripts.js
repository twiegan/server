const continueButton = document.getElementById("continue-button");
const positionTracker = document.getElementById("position-tracker");

continueButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);

    location.replace( "/game/" + (position + 1));
})