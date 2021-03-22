const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input : string[] = [];

function solution(): void {
    let index: number = 0
    const dr: number[] = [-1, 1, 0, 0]
    const dc: number[] = [0, 0, -1, 1]
    const NQ: string[] = input[index].split(" ")
    index++
    const N: number = parseInt(NQ[0])
    const Q: number = parseInt(NQ[1])
    let iceArray: number[][] = Array.from(Array(2 ** N), () => Array(2 ** N).fill(0))
    for (let row: number = 0; row < 2 ** N; row++) {
        const temp: string[] = input[index].split(" ")
        index++
        for (let col: number = 0; col < 2 ** N; col++) {
            iceArray[row][col] = parseInt(temp[col])
        }
    }
    let LArray: number[] = input[index].split(" ").map(el => parseInt(el))
    for (let step: number = 0; step < Q; step++) {
        // 1. 격자로 나눈다. (다음 단계의 Array를 미리 복사해둔다.)
        const copyIceArray = JSON.parse(JSON.stringify(iceArray))
        const L: number = LArray[step]
        let gStartRow: number = 0;
        let gStartCol: number = 0;
        // 2. 90도 회전(cw)
        if (L !== 0) {
            while (gStartRow < 2 ** N) {
                    gStartCol = 0
                    while (gStartCol < 2 ** N) {
                        for (let gRow = gStartRow; gRow < gStartRow + 2 ** L; gRow++) {
                            for (let gCol = gStartCol; gCol < gStartCol + 2 ** L; gCol++) {
                                iceArray[(gCol - gStartCol) + gStartRow][2 ** L - 1 - (gRow - gStartRow) + gStartCol] = copyIceArray[gRow][gCol]
                            }
                        }
                        gStartCol += 2 ** L
                    }
                gStartRow += 2 ** L
            }
        }
        // 3. 얼음을 녹인다.
        let meltArray: Array<number[]> = []
        let nr: number = 0
        let nc: number = 0
        let stack: number = 0
        for (var mRow: number = 0; mRow < 2 ** N; mRow++) {
            for (var mCol: number = 0; mCol < 2 ** N; mCol++) {
                stack = 0
                for (var w: number = 0; w < 4; w++) {
                    nr = mRow + dr[w]
                    nc = mCol + dc[w]
                    if (nr < 0 || nr >= 2 ** N || nc < 0 || nc >= 2 ** N) {
                        continue
                    }
                    if (iceArray[nr][nc] > 0) {
                        stack++
                    }  
                }
                if (stack < 3) {
                    meltArray.push([mRow, mCol])
                }
            }
        }
        meltArray.forEach(el => {
            if (iceArray[el[0]][el[1]] > 0) {
                iceArray[el[0]][el[1]]--
            }
        })
    }
    // 4. 합과 덩어리를 구한다.
    function sumIce(N: number, array: number[][]): number {
        let res: number = 0
        for (let row = 0; row < 2 ** N; row++) {
            for (let col = 0; col < 2 ** N; col++) {
                res += iceArray[row][col]
            }
        }
        return res
    }

    function findMaxIceLand(N: number, array: number[][]): number {

        function bfs(row: number, col: number, array: number[][], visited: boolean[][]): number {
            const dr: number[] = [-1, 1, 0, 0]
            const dc: number[] = [0, 0, -1, 1]
            let res: number = 1
            let queue: Array<number[]> = []
            queue.push([row, col])
            visited[row][col] = true
            let nr: number = 0
            let nc: number = 0
            while (queue.length > 0) {
                let [r, c]: number[] = queue.shift();
                for (let w = 0; w < 4; w++) {
                    nr = r + dr[w]
                    nc = c + dc[w]
                    if (nr < 0 || nr >= 2 ** N || nc < 0 || nc >= 2 ** N) {
                        continue
                    }
                    if (visited[nr][nc]) {
                        continue
                    }
                    if (array[nr][nc] === 0) {
                        continue
                    }
                    res++
                    visited[nr][nc] = true
                    queue.push([nr, nc])
                }
            }

            return res
        }

        let maxIceLand: number = 0;
        let iceLand: number = 0
        let visited: boolean[][] = Array.from(Array(2 ** N), () => Array(2 ** N).fill(false))
        for (let row = 0; row < 2 ** N; row++) {
            for (let col = 0; col < 2 ** N; col++) {
                if (visited[row][col]) {
                    continue
                }
                if (array[row][col] === 0) {
                    continue
                }
                iceLand = bfs(row, col, array, visited)
                if (iceLand > maxIceLand) {
                    maxIceLand = iceLand
                }
            }
        }
        return maxIceLand
    }

    const result1 = sumIce(N, iceArray)
    const result2 = findMaxIceLand(N, iceArray)
    console.log(result1)
    console.log(result2)
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})