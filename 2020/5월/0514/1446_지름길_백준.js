const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})
input = []

solution = () => {
    let nd = input[0].split(" ")
    n = parseInt(nd[0])
    d = parseInt(nd[1])
    load = []
    for (let i = 1; i < d + 2; i++) {
        load.push([[i, 1]])
    }
    load[d] = []
    for (let i = 1; i < n + 1; i++) {
        let sec = input[i].split(" ")
        s = parseInt(sec[0])
        e = parseInt(sec[1])
        c = parseInt(sec[2])
        if (e > d) continue;
        load[s].push([e, c])
    }
    console.log(dijkstra())
}

dijkstra = () => {
    let dijk = Array(d + 1).fill(Infinity)
    dijk[0] = 0
    let visit = Array(d + 1).fill(false)
    index = 0
    while (true) {
        for (let i = 0; i < load[index].length; i++) {
            let ni = load[index][i][0]
            let cost = load[index][i][1]
            if (visit[ni]) continue;
            let via = dijk[index] + cost
            if (via < dijk[ni]) {
                dijk[ni] = via
            }
        }
        visit[index] = true
        let minCost = Infinity
        for (let i = 0; i < d + 1; i++) {
            if (visit[i]) continue;
            if (minCost > dijk[i]) {
                minCost = dijk[i]
                index = i
            }
        }
        if (minCost === Infinity) {
            break
        }
    }
    return dijk[d]
}



rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})