const positionTracker = document.getElementById("position-tracker");
const user = document.getElementById("user");
const backButton = document.getElementById("back-button");

backButton.addEventListener("click", (e) => {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    location.replace("/" + username + "/game/" + position);
})

// Keybindings
document.addEventListener('keydown', function(e) {
    e.preventDefault();
    const position = parseInt(positionTracker.textContent);
    const username = user.textContent;
    if(e.key === 'Enter' || e.code === 'Enter') {
        backButton.click();
    }
});