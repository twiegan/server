const selection1 = document.getElementById("combat-selection-1");
const view = document.getElementById("combat-view");
const selection2 = document.getElementById("combat-selection-2");

var inCombat = false;
var fourEnabled = true;
var fiveEnabled = true;
var sixEnabled = true;

function initiateCombat() {
    fetch('/combat', {
        body: JSON.stringify({
            info: "combat/initiate"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('initiateCombat(): response', response);

        if (response.initiated === true) {
            inCombat = true;
            fourEnabled = true;
            fiveEnabled = true;
            sixEnabled = true;
            showCombat()
        } else {
            canMove = true;
            selection1.innerHTML = `<br><br><br><br><p>---</p>`;
            view.innerHTML = `<br><br><br><br><p>---</p>`;
            selection2.innerHTML = `<br><br><br><br><p>---</p>`;
        }
    })
} // initiateCombat()

function showCombat() {
    fetch('/combat', {
        body: JSON.stringify({
            info: "combat/show"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('showCombat(): response', response);

        // selection1
        let newSelection1Text = `~~~Allies~~~`;
        let k = 1;
        for (let i in response.allies) {
            newSelection1Text += `<p><br>${k++}. ${response.allies[i].type}'s stats</p>`;
        }
        selection1.innerHTML = newSelection1Text;

        // view
        // allies
        let newViewText = ``;
        for (let i in response.allies) {
            if (response.allies[i].isAlive === true) {
                newViewText += `${response.allies[i].ally_char} `;
            } else {
                newViewText += `${response.death_char} `;
            }
        }
        // player
        if (response.player.isAlive === true) {
            newViewText += `${response.player_char} vs. `;
        } else {
            newViewText += `${response.death_char} vs `;
        }
        // enemies
        let count = 0
        for (let i in response.enemies) {
            if (response.enemies[i].isAlive === true) {
                newViewText += `${response.enemies[i].enemy_char} `;
            } else {
                if (count === 0) {
                    console.log('switching fourEnabled')
                    fourEnabled = false;
                } else if (count === 1) {
                    console.log('switching fiveEnabled')
                    fiveEnabled = false;
                } else if (count === 2) {
                    console.log('switching sixEnabled')
                    sixEnabled = false;
                }
                newViewText += `${response.death_char} `;
            }
            count++;
        }

        newViewText += `<p><br>4. Attack Enemy #1` +
                       `<br>5. Attack Enemy #2` +
                       `<br>6. Attack Enemy #3</p>`
        view.innerHTML = newViewText;

        // selection2
        let newSelection2Text = `~~~Enemies~~~`;
        k = 7;
        for (let i in response.enemies) {
            newSelection2Text += `<p><br>${k++}. ${response.enemies[i].type}'s stats</p>`;
        }
        selection2.innerHTML = newSelection2Text;
    })
} // showCombat()

function calculateCombat(digit) {
    fetch('/combat', {
        body: JSON.stringify({
            info: "combat/calculate",
            target: digit
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('calculateCombat(): response', response);
        if (response.won === true) {
            inCombat = false;
            canMove = true;
        }
        showCombat();
    })
} // attack()

function makeTable(curr) {
    let table = '<table>';
    table += '<tbody>';
    if (curr.isAlive === true) {
        table += '<tr><th>name:</th><td>' + curr.type + '</td></tr>';
        table += '<tr><th>hp:</th><td>' + curr.hp + '</td></tr>';
        table += '<tr><th>dge:</th><td>' + curr.dge + '</td></tr>';
        table += '<tr><th>spd:</th><td>' + curr.spd + '</td></tr>';
        table += '<tr><th>phy_res:</th><td>' + curr.phy_res + '</td></tr>';
        table += '<tr><th>fire_res:</th><td>' + curr.fire_res + '</td></tr>';
        table += '<tr><th>frost_res:</th><td>' + curr.frost_res + '</td></tr>';
    } else {
        table += '<tr><th>Dead</th><td>Dead</td></tr>';
    }
    return table
} // makeTable()

function showAllyStats(digit) {
    fetch('/combat', {
        body: JSON.stringify({
            info: "combat/showAllyStats",
            target: digit
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('showAllyStats(): response', response);
        let keys = Object.keys(response);
        if (digit === 1 && keys.length >= 1) {
            let curr_ally = response[keys[0]];
            selection1.innerHTML = makeTable(curr_ally);
        } else if (digit === 2 && keys.length >= 2) {
            let curr_ally = response[keys[1]];
            selection1.innerHTML = makeTable(curr_ally);
        } else if (digit === 3 && keys.length >= 3) {
            let curr_ally = response[keys[2]];
            selection1.innerHTML = makeTable(curr_ally);
        }
    })
} // showAllyStats()

function showEnemyStats(digit) {
    fetch('/combat', {
        body: JSON.stringify({
            info: "combat/showEnemyStats",
            target: digit
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('showEnemyStats(): response', response);
        let keys = Object.keys(response);
        if (digit === 7 && keys.length >= 1) {
            let curr_enemy = response[keys[0]];
            selection2.innerHTML = makeTable(curr_enemy);
        } else if (digit === 8 && keys.length >= 2) {
            let curr_enemy = response[keys[1]];
            selection2.innerHTML = makeTable(curr_enemy);
        } else if (digit === 9 && keys.length >= 3) {
            let curr_enemy = response[keys[2]];
            selection2.innerHTML = makeTable(curr_enemy);
        }
    })
} // showEnemyStats()