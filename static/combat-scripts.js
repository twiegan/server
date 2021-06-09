const selection1 = document.getElementById("combat-selection-1");
const view = document.getElementById("combat-view");
const selection2 = document.getElementById("combat-selection-2");

var inCombat = false;
var combatResponse = null;

function showView() {
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
        console.log('showView(): response', response);
        combatResponse = response;

        if (response.combat === true) {
            inCombat = true;
            // selection1
            let newSelection1Text = `~~~Allies~~~`;
            let j = 1;
            let k = 1;
            for (let i in response.allies) {
                newSelection1Text += `<p><br>${k++}. ${response.allies[i].type}'s stats</p>`;
            }
            selection1.innerHTML = newSelection1Text;

            // view
            let newViewText = ``;
            for (let i in response.allies) { // allies
                newViewText += `${response.allies[i].ally_char} `;
            }
            newViewText += `${response.player_char} vs. `; // player
            for (let i in response.enemies) {
                newViewText += `${response.enemies[i].enemy_char} `; // enemies
            }

            newViewText += `<p><br>4. Ability #1` +
                           `<br>5. Ability #2` +
                           `<br>6. Ability #3</p>`
            view.innerHTML = newViewText;

            // selection2
            let newSelection2Text = `~~~Enemies~~~`;
            j = 1;
            k = 7;
            for (let i in response.enemies) {
                newSelection2Text += `<p><br>${k++}. ${response.enemies[i].type}'s stats</p>`;
            }
            selection2.innerHTML = newSelection2Text;
        } else {
            selection1.innerHTML = `<br><br><br><br><p>---</p>`;
            view.innerHTML = `<br><br><br><br><p>---</p>`;
            selection2.innerHTML = `<br><br><br><br><p>---</p>`;
        }
    })
} // showView()

function makeTable(curr) {
    let table = '<table>';
    table += '<tbody>';
    table += '<tr><th>name:</th><td>'+curr.type+'</td></tr>';
    table += '<tr><th>hp:</th><td>'+curr.hp+'</td></tr>';
    table += '<tr><th>dge:</th><td>'+curr.dge+'</td></tr>';
    table += '<tr><th>spd:</th><td>'+curr.spd+'</td></tr>';
    table += '<tr><th>phy_res:</th><td>'+curr.phy_res+'</td></tr>';
    table += '<tr><th>fire_res:</th><td>'+curr.fire_res+'</td></tr>';
    table += '<tr><th>frost_res:</th><td>'+curr.frost_res+'</td></tr>';
    return table
} // makeTable()

function showAllyStats(digit) {
    if (inCombat) {
        console.log('showAllyStats(): combatResponse', combatResponse);
        let keys = Object.keys(combatResponse.allies);
        if (digit === 1 && keys.length >= 1) {
            let curr_ally = combatResponse.allies[keys[0]];
            selection1.innerHTML = makeTable(curr_ally);
        } else if (digit === 2 && keys.length >= 2) {
            let curr_ally = combatResponse.allies[keys[1]];
            selection1.innerHTML = makeTable(curr_ally);
        } else if (digit === 3 && keys.length >= 3) {
            let curr_ally = combatResponse.allies[keys[2]];
            selection1.innerHTML = makeTable(curr_ally);
        }
    }
} // showAllyStats()

function useAbility(digit) {
    if (inCombat) {
        console.log('useAbility(): combatResponse', combatResponse);
        let keys = Object.keys(combatResponse.player.abilities);
        if (digit === 4 && keys.length >= 1) {
            view.innerHTML = combatResponse.player.abilities[keys[0]];
        } else if (digit === 5 && keys.length >= 2) {
            view.innerHTML = combatResponse.player.abilities[keys[1]];
        } else if (digit === 6 && keys.length >= 3) {
            view.innerHTML = combatResponse.player.abilities[keys[2]];
        }
    }
} // useAbility()

function showEnemyStats(digit) {
    if (inCombat) {
        console.log('showEnemyStats(): combatResponse', combatResponse);
        let keys = Object.keys(combatResponse.enemies);
        if (digit === 7 && keys.length >= 1) {
            let curr_enemy = combatResponse.enemies[keys[0]];
            selection2.innerHTML = makeTable(curr_enemy);
        } else if (digit === 8 && keys.length >= 2) {
            let curr_enemy = combatResponse.enemies[keys[1]];
            selection2.innerHTML = makeTable(curr_enemy);
        } else if (digit === 9 && keys.length >= 3) {
            let curr_enemy = combatResponse.enemies[keys[2]];
            selection2.innerHTML = makeTable(curr_enemy);
        }
    }
} // showEnemyStats()