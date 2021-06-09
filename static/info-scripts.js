const infoArea = document.getElementById("info");

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
        console.log('showInventory(): response', response);
        if (Object.keys(response).length === 0) {
            infoArea.innerHTML = "No items";
        } else {
            let table = '<table><thead><tr><th>Name</th><th>Value</th><th>Durability</th><th>Type</th><th>Damage</th><th>Defense</th></tr></thead>';
            table += '<tbody>';
            for (let i in response) {
                table += '<tr>';
                table += '<td>'+response[i]['name']+'</td>';
                table += '<td>'+response[i]['value']+'</td>';
                table += '<td>'+response[i]['durability']+'</td>';
                table += '<td>'+response[i]['type']+'</td>';
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
        console.log('showMap(): response', response);
        if (Object.keys(response).length === 0) {
            infoArea.innerHTML = "No map";
        } else {
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
        console.log('showStats(): response', response);
        if (Object.keys(response).length === 0) {
            infoArea.innerHTML = "No stats";
        } else {
            let table = '<table>';
            table += '<tbody>';
            for (let i in response) {
                table += '<tr><th>'+i+':</th><td>'+response[i]+'</td></tr>';
            }
            infoArea.innerHTML = table;
        }
    })
}