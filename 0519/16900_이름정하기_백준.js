const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []

solution = () => {
    let sk = input[0].split(' ')
    let keyword = sk[0]
    let k = parseInt(sk[1]) // sk[1].map((el) => parseInt(el))

    pattern = Array(keyword.length).fill(0)
    makeTable(keyword, pattern)
    let temp = keyword.length - pattern[keyword.length - 1]
    console.log(temp * (k - 1) + keyword.length)
}

makeTable = (keyword, table) => {

    let i = 1
    let j = 0

    while(i < keyword.length) {
        if (keyword[i] === keyword[j]) {
            j++
            table[i] = j
            i++
        }
        else {
            if (j) j = table[j - 1]
            else {
                table[i] = 0
                i++
            }
        }
    }
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})