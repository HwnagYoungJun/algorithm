var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
var input = [];
function solution() {
    var index = 0;
    var dr = [-1, 1, 0, 0];
    var dc = [0, 0, -1, 1];
    var NQ = input[index].split(" ");
    index++;
    var N = parseInt(NQ[0]);
    var Q = parseInt(NQ[1]);
    var iceArray = Array.from(Array(Math.pow(2, N)), function () { return Array(Math.pow(2, N)).fill(0); });
    for (var row = 0; row < Math.pow(2, N); row++) {
        var temp = input[index].split(" ");
        index++;
        for (var col = 0; col < Math.pow(2, N); col++) {
            iceArray[row][col] = parseInt(temp[col]);
        }
    }
    var LArray = input[index].split(" ").map(function (el) { return parseInt(el); });
    for (var step = 0; step < Q; step++) {
        // 1. 격자로 나눈다. (다음 단계의 Array를 미리 복사해둔다.)
        var copyIceArray = JSON.parse(JSON.stringify(iceArray));
        var L = LArray[step];
        var gStartRow = 0;
        var gStartCol = 0;
        // 2. 90도 회전(cw)
        if (L !== 0) {
            while (gStartRow < Math.pow(2, N)) {
                gStartCol = 0;
                while (gStartCol < Math.pow(2, N)) {
                    for (var gRow = gStartRow; gRow < gStartRow + Math.pow(2, L); gRow++) {
                        for (var gCol = gStartCol; gCol < gStartCol + Math.pow(2, L); gCol++) {
                            iceArray[(gCol - gStartCol) + gStartRow][Math.pow(2, L) - 1 - (gRow - gStartRow) + gStartCol] = copyIceArray[gRow][gCol];
                        }
                    }
                    gStartCol += Math.pow(2, L);
                }
                gStartRow += Math.pow(2, L);
            }
        }
        // 3. 얼음을 녹인다.
        var meltArray = [];
        var nr = 0;
        var nc = 0;
        var stack = 0;
        for (var mRow = 0; mRow < Math.pow(2, N); mRow++) {
            for (var mCol = 0; mCol < Math.pow(2, N); mCol++) {
                stack = 0;
                for (var w = 0; w < 4; w++) {
                    nr = mRow + dr[w];
                    nc = mCol + dc[w];
                    if (nr < 0 || nr >= Math.pow(2, N) || nc < 0 || nc >= Math.pow(2, N)) {
                        continue;
                    }
                    if (iceArray[nr][nc] > 0) {
                        stack++;
                    }
                }
                if (stack < 3) {
                    meltArray.push([mRow, mCol]);
                }
            }
        }
        meltArray.forEach(function (el) {
            if (iceArray[el[0]][el[1]] > 0) {
                iceArray[el[0]][el[1]]--;
            }
        });
    }
    // 4. 합과 덩어리를 구한다.
    function sumIce(N, array) {
        var res = 0;
        for (var row = 0; row < Math.pow(2, N); row++) {
            for (var col = 0; col < Math.pow(2, N); col++) {
                res += iceArray[row][col];
            }
        }
        return res;
    }
    function findMaxIceLand(N, array) {
        function bfs(row, col, array, visited) {
            var dr = [-1, 1, 0, 0];
            var dc = [0, 0, -1, 1];
            var res = 1;
            var queue = [];
            queue.push([row, col]);
            visited[row][col] = true;
            var nr = 0;
            var nc = 0;
            while (queue.length > 0) {
                var _a = queue.shift(), r = _a[0], c = _a[1];
                for (var w_1 = 0; w_1 < 4; w_1++) {
                    nr = r + dr[w_1];
                    nc = c + dc[w_1];
                    if (nr < 0 || nr >= Math.pow(2, N) || nc < 0 || nc >= Math.pow(2, N)) {
                        continue;
                    }
                    if (visited[nr][nc]) {
                        continue;
                    }
                    if (array[nr][nc] === 0) {
                        continue;
                    }
                    res++;
                    visited[nr][nc] = true;
                    queue.push([nr, nc]);
                }
            }
            return res;
        }
        var maxIceLand = 0;
        var iceLand = 0;
        var visited = Array.from(Array(Math.pow(2, N)), function () { return Array(Math.pow(2, N)).fill(false); });
        for (var row = 0; row < Math.pow(2, N); row++) {
            for (var col = 0; col < Math.pow(2, N); col++) {
                if (visited[row][col]) {
                    continue;
                }
                if (array[row][col] === 0) {
                    continue;
                }
                iceLand = bfs(row, col, array, visited);
                if (iceLand > maxIceLand) {
                    maxIceLand = iceLand;
                }
            }
        }
        return maxIceLand;
    }
    var result1 = sumIce(N, iceArray);
    var result2 = findMaxIceLand(N, iceArray);
    console.log(result1);
    console.log(result2);
}
rl.on('line', function (line) { return input.push(line); })
    .on('close', function () {
    solution();
    process.exit();
});
