document.addEventListener('keyup', function(e) {
    e.preventDefault();
    if (e.key === '1' || e.code === 'Digit1') { // ~~~COMBAT SCRIPTS~~~
        showAllyStats(1);
    } else if (e.key === '2' || e.code === 'Digit2') {
        showAllyStats(2);
    } else if (e.key === '3' || e.code === 'Digit3') {
        showAllyStats(3);
    } else if (e.key === '4' || e.code === 'Digit4') {
        useAbility(4);
    } else if (e.key === '5' || e.code === 'Digit5') {
        useAbility(5);
    } else if (e.key === '6' || e.code === 'Digit6') {
        useAbility(6);
    } else if (e.key === '7' || e.code === 'Digit7') {
        showEnemyStats(7);
    } else if (e.key === '8' || e.code === 'Digit8') {
        showEnemyStats(8);
    } else if (e.key === '9' || e.code === 'Digit9') {
        showEnemyStats(9);
    } else if (e.key === 'ArrowUp' || e.code === 'ArrowUp') { // ~~~MOVE SCRIPTS~~~
        inCombat = false;
        moveNorth(showMap, showView); // callbacks to guarantee order
    } else if (e.key === 'ArrowRight' || e.code === 'ArrowRight') {
        inCombat = false;
        moveEast(showMap, showView);
    } else if (e.key === 'ArrowDown' || e.code === 'ArrowDown') {
        inCombat = false;
        moveSouth(showMap, showView);
    } else if (e.key === 'ArrowLeft' || e.code === 'ArrowLeft') {
        inCombat = false;
        moveWest(showMap, showView);
    } else if (e.key === 'i' || e.code === 'KeyI') { // ~~~INFO SCRIPTS~~~
        showInventory();
    }
    else if (e.key === 'm' || e.code === 'KeyM') {
        showMap();
    }
    else if (e.key === 's' || e.code === 'KeyS') {
        showStats();
    }
});