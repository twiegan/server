const combatArea = document.getElementById("combat-text");

function showCombat() {
    fetch('/combat', {
        body: JSON.stringify({
            info: "combat"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log(response);
        combatArea.innerHTML = response.text;
    })
}