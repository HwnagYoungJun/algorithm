const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input : string[] = [];

function solution(): void {

    function bfs(hpArray: number[]): number {
        let permutationArray: number[][] = [[-9, -3, -1], [-9, -1, -3], [-3, -9, -1], [-3, -1, -9], [-1, -3, -9], [-1, -9, -3]]
        let deque: number[][] = []
        let flag: boolean = false
        let turn: number = 0
        let visited: boolean[][][] = new Array(hpArray[0] + 1)
        for (var i: number = 0; i < hpArray[0] + 1; i++) {
            visited[i] = new Array(hpArray[1] + 1)
            for (var j: number = 0; j < hpArray[1] + 1; j++) {
                visited[i][j] = new Array(hpArray[2] + 1)
                for (var k: number = 0; k < hpArray[2] + 1; k++) {
                    visited[i][j][k] = false
                }
            }
        }
        deque.push([...hpArray, 1])

        while (true) {
            const SCV: number[] = deque.shift()
            let scv1: number = SCV[0]
            let scv2: number = SCV[1]
            let scv3: number = SCV[2]
            let thisturn: number = SCV[3]
            
            for (let i: number = 0; i < 6; i++) {
                let newScv1 = scv1 + permutationArray[i][0]
                let newScv2 = scv2 + permutationArray[i][1]
                let newScv3 = scv3 + permutationArray[i][2]
                if (newScv1 < 0) {
                    newScv1 = 0
                }
                if (newScv2 < 0) {
                    newScv2 = 0
                }
                if (newScv3 < 0) {
                    newScv3 = 0
                }
                if ((newScv1 + newScv2 + newScv3) === 0) {
                    flag = true
                    turn = thisturn
                    break
                } else {
                    if (visited[newScv1][newScv2][newScv3]) {
                        continue
                    }
                    visited[newScv1][newScv2][newScv3] = true
                    deque.push([newScv1, newScv2, newScv3, thisturn + 1])
                }
            }
            if (flag) {
                break
            }
        }
        return turn
    }

    const N: number = parseInt(input[0])
    const hpArray: number[] = input[1].split(" ").map(el => parseInt(el))
    let turn: number = 0
    if (N < 3) {
        if (N === 1){
            hpArray.push(0)
            hpArray.push(0)
        }
        if (N === 2) {
            hpArray.push(0)
        }
    }
    if (N === 1) {
        console.log(Math.ceil(hpArray[0] / 9))
    } else {
        const result: number = bfs(hpArray)
        console.log(result)
    }
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})