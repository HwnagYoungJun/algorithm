const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []

solution = () => {
    n = parseInt(input[0])
    visit = Array.from(Array(n), () => Array(n).fill(false))
    c1 = Array(2 * n - 1).fill(false)
    c2 = Array(2 * n - 1).fill(false)
    column = Array(n).fill(false)
    cnt = 0
    for (let col = 0; col < n; col++) {
        c1[col] = true
        c2[n - col - 1] = true
        column[col] = true
        dfs(0, 1)
        c1[col] = false
        c2[n - col - 1] = false
        column[col] = false
    }
    console.log(cnt)
}

dfs = (r, k) => {
    if (k == n) {
        cnt++
        return
    }
    r++
    for (let col = 0; col < n; col++) {
        if (c1[r + col] === false && c2[r - col + n - 1] === false && column[col] === false) {
            c1[r + col] = true
            c2[r - col + n - 1] = true
            column[col] = true
            k++
            dfs(r, k)
            c1[r + col] = false
            c2[r - col + n - 1] = false
            column[col] = false
            k--
        }
    }
    r--
}


rl.on('line', line => input.push(line))
.on('close', () =>{
    solution()
    process.exit()
})