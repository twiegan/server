const menuButton = document.getElementById("menu-form-submit");

menuButton.addEventListener("click", (e) => {
    e.preventDefault();
    location.replace( "/game/0");
})