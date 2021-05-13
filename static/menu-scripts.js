const newGameButton = document.getElementById("new-game-submit");
const header = document.getElementById("menu-header");

newGameButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = header.textContent;
    location.replace( "/" + username + "/game/0");
})

const resumeGameButton = document.getElementById("resume-game-submit");

resumeGameButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = header.textContent;
    location.replace( "/" + username + "/game/0");
})