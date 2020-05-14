const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []

solution = () => {
    const reference = input[0]
    const keyword = input[1]
    const len_k = keyword.length
    const lastWord = keyword[len_k - 1]
    
    stack = []
    for (let i = 0; i < reference.length; i++) {
        stack.push(reference[i])
        let len_s = stack.length
        if (lastWord !== reference[i] || len_s < len_k) continue;
        if (stack.slice(len_s - len_k).join("") === keyword) {
            stack.splice(len_s - len_k)
        }
    }
    if (!stack.length) console.log("FRULA")
    console.log(stack.join(""))
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})