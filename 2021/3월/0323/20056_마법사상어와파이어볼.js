var __spreadArray = (this && this.__spreadArray) || function (to, from) {
    for (var i = 0, il = from.length, j = to.length; i < il; i++, j++)
        to[j] = from[i];
    return to;
};
var readline = require("readline");
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
var input = [];
function solution() {
    function moveFireball(N, fireball, checkArray, fireballQueue, overlapQueue) {
        var dr = [-1, -1, 0, 1, 1, 1, 0, -1];
        var dc = [0, 1, 1, 1, 0, -1, -1, -1];
        var nr = 0;
        var nc = 0;
        var r = fireball[0];
        var c = fireball[1];
        var m = fireball[2];
        var s = fireball[3];
        var d = fireball[4];
        nr = r + s * dr[d];
        nc = c + s * dc[d];
        if (nr < 0) {
            nr = (nr % N) + N;
        }
        if (nr >= N) {
            nr %= N;
        }
        if (nc < 0) {
            nc = (nc % N) + N;
        }
        if (nc >= N) {
            nc %= N;
        }
        if (checkArray[nr][nc].length > 0) {
            overlapQueue.push([nr, nc]);
            if (checkArray[nr][nc].length === 1) {
                var index_1 = fireballQueue.findIndex(function (el) {
                    return JSON.stringify(checkArray[nr][nc][0]) === JSON.stringify(el);
                });
                if (index_1 > -1) {
                    fireballQueue.splice(index_1, 1);
                }
            }
        }
        else {
            fireballQueue.push([nr, nc, m, s, d]);
        }
        checkArray[nr][nc] = __spreadArray(__spreadArray([], checkArray[nr][nc]), [[nr, nc, m, s, d]]);
    }
    function handleOverlap(checkArray, fireballQueue, overlapQueue) {
        var _loop_1 = function () {
            var dr = [-1, -1, 0, 1, 1, 1, 0, -1];
            var dc = [0, 1, 1, 1, 0, -1, -1, -1];
            var _a = overlapQueue.shift(), r = _a[0], c = _a[1];
            var isFitDirection = true;
            var lastDirection = -1;
            var sumMass = 0;
            var sumSpeed = 0;
            checkArray[r][c].forEach(function (el) {
                if (isFitDirection) {
                    if (lastDirection !== -1) {
                        if (lastDirection % 2 != el[4] % 2) {
                            isFitDirection = false;
                        }
                    }
                    lastDirection = el[4];
                }
                sumMass += el[2];
                sumSpeed += el[3];
            });
            var nextMass = Math.floor(sumMass / 5);
            var nextSpeed = Math.floor(sumSpeed / checkArray[r][c].length);
            if (nextMass === 0) {
                return "continue";
            }
            var nr = 0;
            var nc = 0;
            var directionArray = [];
            if (isFitDirection) {
                directionArray = [0, 2, 4, 6];
            }
            else {
                directionArray = [1, 3, 5, 7];
            }
            for (var w = 0; w < 4; w++) {
                fireballQueue.push([r, c, nextMass, nextSpeed, directionArray[w]]);
            }
        };
        while (overlapQueue.length > 0) {
            _loop_1();
        }
    }
    var index = 0;
    var NMK = input[index].split(" ");
    var N = parseInt(NMK[0]);
    var M = parseInt(NMK[1]);
    var K = parseInt(NMK[2]);
    var fireballQueue = [];
    for (var m = 0; m < M; m++) {
        index++;
        var temp = input[index].split(" ").map(function (el) { return parseInt(el); });
        temp[0] -= 1;
        temp[1] -= 1;
        fireballQueue.push(temp);
    }
    // 1. K번 만큼 이동
    for (var command = 0; command < K; command++) {
        var checkArray = Array.from(Array(N), function () { return Array(N).fill(new Array()); });
        var overlapQueue = [];
        // 2. 파이어볼 이동
        var lengthFireballQueue = fireballQueue.length;
        for (var fireball = 0; fireball < lengthFireballQueue; fireball++) {
            var posFireball = fireballQueue.shift();
            moveFireball(N, posFireball, checkArray, fireballQueue, overlapQueue);
        }
        // 3. 중첩 파이어볼 처리
        handleOverlap(checkArray, fireballQueue, overlapQueue);
    }
    // 4. 합 구하기
    var result = 0;
    fireballQueue.forEach(function (el) {
        result += el[2];
    });
    console.log(result);
}
rl.on("line", function (line) { return input.push(line); }).on("close", function () {
    solution();
    process.exit();
});
