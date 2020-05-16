// 1. 투 포인터 기초 문제
// <TIL>

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})
input = []

solution = () => {
    const nm = input[0].split(" ").map((el) => parseInt(el))
    const n = nm[0]
    const m = nm[1]
    const numbers = input[1].split(" ").map((el) => parseInt(el))

    let r, l, sum, min // right, left, 부분합, 최소길이
    r = l = sum = 0
    min = Infinity

    while (true) {
        if (sum >= m) {
            if (r - l < min) {
                min = r - l
            }
            sum -= numbers[l]
            l++
        }
        else {
            if (r === n) break;
            sum += numbers[r]
            r++
        }
    }
    min === Infinity ? min = 0 : {}
    console.log(min)
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})