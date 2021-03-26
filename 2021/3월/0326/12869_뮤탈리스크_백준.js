var __spreadArray = (this && this.__spreadArray) || function (to, from) {
    for (var i = 0, il = from.length, j = to.length; i < il; i++, j++)
        to[j] = from[i];
    return to;
};
var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
var input = [];
function solution() {
    function bfs(hpArray) {
        var permutationArray = [[-9, -3, -1], [-9, -1, -3], [-3, -9, -1], [-3, -1, -9], [-1, -3, -9], [-1, -9, -3]];
        var deque = [];
        var flag = false;
        var turn = 0;
        var visited = new Array(hpArray[0] + 1);
        for (var i = 0; i < hpArray[0] + 1; i++) {
            visited[i] = new Array(hpArray[1] + 1);
            for (var j = 0; j < hpArray[1] + 1; j++) {
                visited[i][j] = new Array(hpArray[2] + 1);
                for (var k = 0; k < hpArray[2] + 1; k++) {
                    visited[i][j][k] = false;
                }
            }
        }
        deque.push(__spreadArray(__spreadArray([], hpArray), [1]));
        while (true) {
            var SCV = deque.shift();
            var scv1 = SCV[0];
            var scv2 = SCV[1];
            var scv3 = SCV[2];
            var thisturn = SCV[3];
            for (var i_1 = 0; i_1 < 6; i_1++) {
                var newScv1 = scv1 + permutationArray[i_1][0];
                var newScv2 = scv2 + permutationArray[i_1][1];
                var newScv3 = scv3 + permutationArray[i_1][2];
                if (newScv1 < 0) {
                    newScv1 = 0;
                }
                if (newScv2 < 0) {
                    newScv2 = 0;
                }
                if (newScv3 < 0) {
                    newScv3 = 0;
                }
                if ((newScv1 + newScv2 + newScv3) === 0) {
                    flag = true;
                    turn = thisturn;
                    break;
                }
                else {
                    if (visited[newScv1][newScv2][newScv3]) {
                        continue;
                    }
                    visited[newScv1][newScv2][newScv3] = true;
                    deque.push([newScv1, newScv2, newScv3, thisturn + 1]);
                }
            }
            if (flag) {
                break;
            }
        }
        return turn;
    }
    var N = parseInt(input[0]);
    var hpArray = input[1].split(" ").map(function (el) { return parseInt(el); });
    var turn = 0;
    if (N < 3) {
        if (N === 1) {
            hpArray.push(0);
            hpArray.push(0);
        }
        if (N === 2) {
            hpArray.push(0);
        }
    }
    if (N === 1) {
        console.log(Math.ceil(hpArray[0] / 9));
    }
    else {
        var result = bfs(hpArray);
        console.log(result);
    }
}
rl.on('line', function (line) { return input.push(line); })
    .on('close', function () {
    solution();
    process.exit();
});
