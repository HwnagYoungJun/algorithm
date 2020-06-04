const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []

solution = () => {
    const N = parseInt(input[0])
    let costArray = []
    for (let i = 1; i < N + 1; i ++) {
        var temp = input[i].split(" ").map((el) => parseInt(el))
        costArray.push(temp)
    }
    minCost = Infinity
    let memo = []
    memo.push(costArray[0])
    for (let i = 1; i < N; i ++) {
        let tt = []
        tt.push(costArray[i][0] + Math.min(memo[i - 1][1], memo[i - 1][2]))
        tt.push(costArray[i][1] + Math.min(memo[i - 1][0], memo[i - 1][2]))
        tt.push(costArray[i][2] + Math.min(memo[i - 1][0], memo[i - 1][1]))
        memo.push(tt)
    }
    let result = Infinity
    memo[N - 1].forEach(element => {
        if (result > element) {
            result = element
        }
    });
    console.log(result)
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})
