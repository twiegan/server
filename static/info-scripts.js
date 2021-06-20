const infoArea = document.getElementById("info");
const equipmentArea = document.getElementById("equipment");
var invCounter = 0;
var eEnabled = false;
var dEnabled = false;
var rEnabled = false;


function setInventoryButtons(onOrOff) {
    eEnabled = onOrOff;
    dEnabled = onOrOff;
    rEnabled = onOrOff;
} // setInventoryButtons()


function showEquipment() {
    fetch('/info', {
        body: JSON.stringify({
            info: "info/equipment"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('showEquipment(): response', response);
        let newText = '<p>'+response.weapon.name+'<br>Dmg: '+response.weapon.damage+'<br>Dur: '+response.weapon.durability+'</p>';
        // Hardcoded equipment for correct ordering
        for (let i in response['armour']) {
            if (response['armour'][i] === null) {
                newText += `<p>${i}: ---<br>Dfs: ---<br>Dur: ---</p>`;
            } else {
                newText += `<p>${i}: ` + response['armour'][i].name + '<br>Dfs: ' + response['armour'][i].defense + '<br>Dur: ' + response['armour'][i].durability + '</p>';
            }
        }
        equipmentArea.innerHTML = newText;
    })
} // showEquipment()

function showInventory() {
    fetch('/info', {
        body: JSON.stringify({
            info: "info/inventory"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('showInventory(): response', response);
        if (Object.keys(response['inventory']).length === 0) {
            setInventoryButtons(false);
        } else {
            setInventoryButtons(true);
        }
        let table = '<table id="inventory-table"><thead><tr><th>'+response['player']['name']+'</th><th>$: '+response['player']['money']+'</th><th>Lbs: '+response['player']['weight']+'/'+response['player']['max_weight']+'</th></tr></thead>' +
        '<tbody><tr><td></td><td>Value</td><td>Durability</td><td>Type</td><td>Damage</td><td>Defense</td></tr>';
        for (let i in response['inventory']) {
            table += '<tr>';
            table += '<td>'+response['inventory'][i]['name']+'</td>';
            table += '<td>'+response['inventory'][i]['value']+'</td>';
            table += '<td>'+response['inventory'][i]['durability']+'</td>';
            table += '<td>'+response['inventory'][i]['type']+'</td>';
            if (response['inventory'][i]['damage']) {
                table += '<td>'+response['inventory'][i]['damage']+'</td>';
            } else {
                table += '<td>---</td>';
            }
            if (response['inventory'][i]['defense']) {
                table += '<td>'+response['inventory'][i]['defense']+'</td>';
            } else {
                table += '<td>---</td>';
            }
        }
        infoArea.innerHTML = table;
        if (Object.keys(response['inventory']).length !== 0) {
            if (invCounter === Object.keys(response['inventory']).length) {
                invCounter = 0;
            }
            invCounter++;
            document.getElementById("inventory-table").tBodies[0].rows[invCounter].style.color = "red";
        }
    })
} // showInventory()

function showMap() {
   fetch('/info', {
        body: JSON.stringify({
            info: "info/map"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
   }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('showMap(): response', response);
        setInventoryButtons(false);
        let table = '<table><tbody>';
        for (let i in response.curr_map) {
            table += '<tr>';
            for (let j in response.curr_map[i])
                if (response.curr_map[i][j].hasPlayer === true) {
                    table += '<td>'+response.player_char+'</td>';
                } else if (response.curr_map[i][j].disc === true) {
                    if (response.curr_map[i][j].location != null) {
                        table += '<td>'+response.curr_map[i][j].location.loc_char+'</td>';
                    } else {
                        table += '<td>'+response.curr_map[i][j].disc_char+'</td>';
                    }
                } else {
                    table += '<td>'+response.undisc_char+'</td>';
                }
            table += '</tr>';
        }
        infoArea.innerHTML = table;
   })
} // showMap()

function showStats() {
    fetch('/info', {
        body: JSON.stringify({
            info: "info/stats"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('showStats(): response', response);
        setInventoryButtons(false);
        let table = '<table>';
        table += '<tbody>';
        for (let i in response) {
            table += '<tr><th>'+i+':</th><td>'+response[i]+'</td></tr>';
        }
        infoArea.innerHTML = table;
    })
} // showStats()

function dropItem(callback) {
    fetch('/info', {
        body: JSON.stringify({
            info: "info/inventory/drop",
            slot: invCounter - 1
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('dropItem(): response', response);
        invCounter--;
        callback();
    })
} // dropItem()

function equipItem(callback, callback2) {
    fetch('/info', {
        body: JSON.stringify({
            info: "info/inventory/equip",
            slot: invCounter - 1
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('equipItem(): response', response);
        invCounter--;
        callback();
        callback2();
    })
} // equipItem()

function sellItem(callback, callback2) {
    fetch('/info', {
        body: JSON.stringify({
            info: "info/inventory/sell",
            slot: invCounter - 1
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('sellItem(): response', response);
        invCounter--;
        callback();
        callback2(2);
    })
} // sellItem()