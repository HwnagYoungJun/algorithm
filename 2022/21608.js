const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let input = []
rl.on('line', (line) => {
    input.push(line)
}).on('close', () => {
    solution();
    process.exit();
})

function solution() {
    const dr = [-1, 1, 0, 0]
    const dc = [0, 0, -1, 1]
    const chooseFavoriteSeat = (classRoom, inputs) => {
        const checkSeat = (classRoom, seatList, status, favoriteList) => {
            let result = []
            let flag = 0
            for (const seat of seatList) {
                const row = seat[0]
                const col = seat[1]
                let count = 0
                for (let w = 0; w < 4; w++) {
                    let nr = dr[w] + row
                    let nc = dc[w] + col
                    if (nr >= N || nr < 0 || nc >= N || nc < 0) continue;
                    switch (status) {
                        case 1:
                            if (favoriteList.includes(classRoom[nr][nc])) {
                                count += 1
                            }
                            break;
                        case 2:
                            if (classRoom[nr][nc] === null) {
                                count += 1
                            }
                            break;
                        default:
                            console.log('error')
                            break;
                    }
                }
                if (count < flag) continue;
                else if (count === flag) {
                    result.push([row, col])
                } else {
                    result = [[row, col]]
                    flag = count
                }
            
            }
            return result
        }

        for (const input of inputs) {
            let seatList = []
            for (const row in classRoom) {
                for (const col in classRoom) {
                    if (classRoom[row][col] === null) {
                        // 왜 row, col string ?
                        seatList.push([parseInt(row), parseInt(col)])
                    }
                }
            }
            seatList = checkSeat(classRoom, seatList, 1, input)
            if (seatList.length === 1) {
                classRoom[seatList[0][0]][seatList[0][1]] = input[0]
                continue;
            }
            seatList = checkSeat(classRoom, seatList, 2)
            if (seatList.length === 1) {
                classRoom[seatList[0][0]][seatList[0][1]] = input[0]
                continue;
            }
            classRoom[seatList[0][0]][seatList[0][1]] = input[0]
        }

    }
    const N = parseInt(input[0]);
    const inputs = input.slice(1).map(el => el.split(' ').map(el => parseInt(el)))
    const inputsObject = {}
    inputs.forEach((input) => {
        inputsObject[input[0]] = [...input.slice(1)]
    })
    const classRoom = Array.from(Array(N), () => Array(N).fill(null));
    chooseFavoriteSeat(classRoom, inputs)
    let satisfaction = 0
    for (let row = 0; row < N; row++){
        for (let col = 0; col < N; col++){
            let score = 0;
            const posStudent = classRoom[row][col]
            for (let w = 0; w < 4; w++) {
                let nr = dr[w] + row
                let nc = dc[w] + col
                if (nr >= N || nr < 0 || nc >= N || nc < 0) continue;
                if (inputsObject[posStudent].includes(classRoom[nr][nc])) {
                    score += 1
                }
            }
            if (score === 0) continue
            satisfaction += 10 ** (score - 1)
        }
    }
    console.log(satisfaction)
}