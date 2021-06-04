const infoArea = document.getElementById("game-info");
const inventoryButton = document.getElementById("button-holder-inventory");
const mapButton = document.getElementById("button-holder-map");
const statsButton = document.getElementById("button-holder-stats");

// Info Screen Buttons
function showInventory() {
    fetch('/inventory', {
        body: JSON.stringify({
            info: "inventory"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log((response))
        if (Object.keys(response).length === 0) {
            infoArea.innerHTML = "No items";
        } else {
            var table = '<table><thead><tr><th>Name</th><th>Value</th><th>Durability</th><th>Type</th><th>Damage</th><th>Defense</th></tr></thead>';
            table += '<tbody>';
            for (var i in response) {
                table += '<tr>';
                table += '<td>'+response[i]['name']+'</td>';
                table += '<td>'+response[i]['value']+'</td>';
                table += '<td>'+response[i]['durability']+'</td>';
                table += '<td>'+response[i]['type']['name']+'</td>';
                if (response[i]['damage']) {
                    table += '<td>'+response[i]['damage']+'</td>';
                } else {
                    table += '<td>---</td>';
                }
                if (response[i]['defense']) {
                    table += '<td>'+response[i]['defense']+'</td>';
                } else {
                    table += '<td>---</td>';
                }
            }
            infoArea.innerHTML = table;
        }
    })
}

function showMap() {
   fetch('/map', {
        body: JSON.stringify({
            info: "map"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
       console.log(response)
        if (Object.keys(response).length === 0) {
            infoArea.innerHTML = "No map";
        } else {
            let table = '<table><tbody>';
            for (let i in response.curr_map) {
                table += '<tr>'
                for (let j in response.curr_map[i])
                    if (response.curr_map[i][j].hasPlayer === true) {
                        table += '<td>'+response.player_char+'</td>';
                    } else if (response.curr_map[i][j].disc === true) {
                        table += '<td>'+response.curr_map[i][j].disc_char+'</td>';
                    } else {
                        table += '<td>'+response.undisc_char+'</td>';
                    }
                table += '</tr>'
            }
            infoArea.innerHTML = table;
        }
    })
}

function showStats() {
        fetch('/stats', {
        body: JSON.stringify({
            info: "stats"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log(response);
        if (Object.keys(response).length === 0) {
            infoArea.innerHTML = "No stats";
        } else {
            var table = '<table>';
            table += '<tbody>';
            for (var i in response) {
                table += '<tr><th>'+i+':</th><td>'+response[i]+'</td></tr>';
            }
            infoArea.innerHTML = table;
        }
    })
}

// Keybindings
document.addEventListener('keydown', function(e) {
    e.preventDefault();
    if(e.key === 'i' || e.code === 'KeyI') {
        inventoryButton.click();
    }
    else if(e.key === 'm' || e.code === 'KeyM') {
        mapButton.click();
    }
    else if(e.key === 's' || e.code === 'KeyS') {
        statsButton.click();
    }
});