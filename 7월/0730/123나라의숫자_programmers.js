const readline = require('readline')
const { PassThrough } = require('stream')
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout,
})
input = []

solution = () => {
    let n = parseInt(input[0])
    let answer = Array()
    console.log(answer)
    while (n != 0) {
        console.log(n)
        if (n % 3 === 0) {
            answer.unshift('4')
            n = n / 3 - 1
        }
        else {
            answer.unshift((n % 3).toString())
            n = parseInt(n / 3)
        }
    }
    answer = answer.join("")
    return answer
}


rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})