const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []

solution = () => {
    const temp = input[0].split(" ").map((el) => parseInt(el))
    n = temp[0]
    m = temp[1]
    
    let city = []
    for (let i = 1; i < n + 1; i++) {
        city.push(input[i].split(' ').map(Number))
    }
    house = []
    len_h = 0
    chicken = []
    let len_c = 0
    for (let row = 0; row < n; row++) {
        for (let col = 0; col < n; col++) {
            if (city[row][col] === 1) {
                house.push([row, col])
                len_h++                
            } else if (city[row][col] === 2) {
                chicken.push([row, col])
                len_c++
            }
        }
    }
    result = Infinity
    my_com(0, len_c, m, [])
    console.log(result)
}

my_com = (k, n, r, com) => {
    if (com.length === r) {
        let total = 0
        let isOK = true
        for (let i = 0; i < len_h; i++) {
            total += shortCut(house[i], com)
            if (result < total) {
                isOK = false
                break
            }
        }
        if (isOK) {
            result = total
        }
        return;
    }
    if (k === n) return;

    my_com(k + 1, n, r, com)
    com.push(chicken[k])
    my_com(k + 1, n, r, com)
    com.pop()
    
}

distance = (n1, n2) => {
    let r1 = n1[0]
    let r2 = n2[0]
    let c1 = n1[1]
    let c2 = n2[1]
    return Math.abs(r2 - r1) + Math.abs(c2 - c1)
}

shortCut = (n, c) => {
    let short = Infinity
    c.forEach(element => {
        let d = distance(element, n)
        if (short > d) {
            short = d
        }
    })
    return short
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})