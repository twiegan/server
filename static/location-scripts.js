var inLocation = false;

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
            if (digit === 1) {
                view.innerHTML = "Now trading"
            } else if (digit === 2) {
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
} // showLocationInfo()