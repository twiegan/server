document.addEventListener("DOMContentLoaded", function() {
  showEquipment();
});

document.addEventListener('keyup', function(e) {
    e.preventDefault();
    if (e.key === '1' || e.code === 'Digit1') { // ~~~COMBAT/LOCATION SCRIPTS~~~
        if (inCombat) {
            showAllyStats(1);
        } else if (inLocation) {
            selectOption(1);
        }
    } else if (e.key === '2' || e.code === 'Digit2') {
        if (inCombat) {
            showAllyStats(2);
        } else if (inLocation) {
            selectOption(2);
        }
    } else if (e.key === '3' || e.code === 'Digit3') {
        if (inCombat) {
            showAllyStats(3);
        } else if (inLocation) {
            selectOption(3);
        }
    } else if (e.key === '4' || e.code === 'Digit4') {
        if (inCombat && fourEnabled) {
            calculateCombat(4);
        }
    } else if (e.key === '5' || e.code === 'Digit5') {
        if (inCombat && fiveEnabled) {
            calculateCombat(5);
        }
    } else if (e.key === '6' || e.code === 'Digit6') {
        if (inCombat && sixEnabled) {
            calculateCombat(6);
        }
    } else if (e.key === '7' || e.code === 'Digit7') {
        if (inCombat) {
            showEnemyStats(7);
        }
    } else if (e.key === '8' || e.code === 'Digit8') {
        if (inCombat) {
            showEnemyStats(8);
        }
    } else if (e.key === '9' || e.code === 'Digit9') {
        if (inCombat) {
            showEnemyStats(9);
        }
    } else if (e.key === 'ArrowUp' || e.code === 'ArrowUp') { // ~~~MOVE SCRIPTS~~~
        if (canMove) {
            moveNorth(showMap, initiateCombat, showLocation); // callbacks to guarantee order
        }
    } else if (e.key === 'ArrowRight' || e.code === 'ArrowRight') {
        if (canMove) {
            moveEast(showMap, initiateCombat, showLocation);
        }
    } else if (e.key === 'ArrowDown' || e.code === 'ArrowDown') {
        if (canMove) {
            moveSouth(showMap, initiateCombat, showLocation);
        }
    } else if (e.key === 'ArrowLeft' || e.code === 'ArrowLeft') {
        if (canMove) {
            moveWest(showMap, initiateCombat, showLocation);
        }
    } else if (e.key === 'i' || e.code === 'KeyI') { // ~~~INFO SCRIPTS~~~
        showInventory();
    }
    else if (e.key === 'm' || e.code === 'KeyM') {
        showMap();
    }
    else if (e.key === 's' || e.code === 'KeyS') {
        showStats();
    }
    else if ((e.key === 'd' || e.code === 'KeyD') && dEnabled) {
        dropItem(showInventory);
    }
    else if ((e.key === 'e' || e.code === 'KeyE') && eEnabled) {
        equipItem(showInventory, showEquipment);
    }
});