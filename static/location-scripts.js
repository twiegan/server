var inLocation = false;
var locCounter = 0;
var fEnabled = false;

function showLocation() {
    fetch('/location', {
        body: JSON.stringify({
            info: "location/show"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('showLocation(): response', response);

        if (response.location === true) {
            inLocation = true;
            canMove = false;
            // selection1
            let newSelection1Text = ``;
            let k = 1;
            for (let i in response.content.options) {
                newSelection1Text += `<p><br>${k++}. ${response.content.options[i]}</p>`;
            }
            selection1.innerHTML = newSelection1Text;

            // view
            view.innerHTML = `<br><br><br><br><p>---</p>`;

            // selection2
            selection2.innerHTML = `<br><br><br><br><p>${response.content.name}</p>`;
        }
    })
} // showView()

function selectOption(digit) {
    fetch('/location', {
        body: JSON.stringify({
            info: "location/selectOption"
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('selectOption(): response', response);

        if (response.content.name === 'Town') {
            if (digit === 1) { // Market
                if (Object.keys(response.content.market.wares).length === 0) {
                    fEnabled = false;
                } else {
                    fEnabled = true;
                }
                let table = '<table id="market-table"><thead><tr><th>Name</th><th>Cost</th></thead>';
                for (let i in response.content.market.wares) {
                    table += `<tr>`;
                    table += `<td>${response.content.market.wares[i].name}</td>`;
                    table += `<td>${response.content.market.wares[i].value}</td></tr>`;
                }
                view.innerHTML = table;
                if (Object.keys(response.content.market.wares).length !== 0) {
                    if (locCounter === Object.keys(response.content.market.wares).length) {
                        locCounter = 0;
                    }
                    document.getElementById("market-table").tBodies[0].rows[locCounter].style.color = "red";
                    locCounter++;
                }
            } else if (digit === 2) { // Leave
                view.innerHTML = "Now leaving"
                canMove = true;
            }
            // other town specific options you want here...
        } else if (response.content.name === 'City') {
            if (digit === 1) {
                view.innerHTML = "Now looting"
            } else if (digit === 2) {
                view.innerHTML = "Now leaving"
                canMove = true;
            }
            // other city specific options you want here...
        }
        // other locations you want here...
    })
} // selectOption()

function buyItem(callback, callback2) {
    fetch('/location', {
        body: JSON.stringify({
            info: "location/buy",
            slot: invCounter - 1
        }),
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        method: 'post'
    }).then(response => response.json(), err => {throw err}).then(response => {
        console.log('buyItem(): response', response);
        invCounter--;
        callback();
        callback2(1);
    })
}