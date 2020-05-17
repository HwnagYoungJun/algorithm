// 1. python으로는 반복문으로 풀었으므로 unionFind로 풀어봄

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []

solution = () => {
    const nm = input[0].split(" ").map((el) => parseInt(el))
    let n = nm[0]
    let m = nm[1]
    let know = input[1].split(" ").map(Number)
    if (know.length !== 1){
        know.splice(0, 1)

    }
    parrent = []
    for (let i = 0; i < n + 1; i++) {
        parrent.push(i)
    }
    for (let i = 2; i < m + 2; i++) {
        let temp = input[i].split(" ").map(Number)
        if (temp[0] === 0) continue
        let root = temp[1]
        for (let ps = 1; ps < temp.length; ps++) {
            if (root === find(temp[ps])) continue
            union(root, temp[ps])
        }
    }
    let iKnow = Array(n + 1).fill(false)
    for (i of know) {
        iKnow[find(i)] = true
    }
    result = 0
    for (let i = 2; i < m + 2; i++) {
        let temp = input[i].split(" ").map(Number)
        if (temp[0] === 0) continue
        let lie = true
        for (let j = 1; j < temp.length; j++) {
            if (iKnow[parrent[find(temp[j])]]) {
                lie = false
                break
            }
        }
        if (lie === true) {
            result += 1
        }
    }
    console.log(result)
}

find = x => {
    if (x === parrent[x]) return x;
    parrent[x] = find(parrent[x])
    return parrent[x]
}

union = (x, y) => {
    let fx = find(x)
    let fy = find(y)
    if (fx !== fy) parrent[fy] = fx
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})