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
        if (response.combat === true) {
            let newText = `\n${response.player_char}    vs.    `
            for (var i in response.enemies) {
                newText += response.enemies[i].enemy_char + "    "
            }
            combatArea.innerHTML = newText
        } else {
            combatArea.innerHTML = "No combat"
        }
    })
}