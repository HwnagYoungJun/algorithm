const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


input = []
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
possible = 0

solution = () => {
    classRoom = []
    for (let i = 0; i < 5; i++) {
        const temp = input[i].split("")
        classRoom.push(temp)
    }
    q = []
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            q.push([row, col])
        }
    }
    console.log(q)
    myCom(0, [])
}

myCom = (k, target) => {

    if (target.length === 7) {
        bfs(q)
        return
    }
    if (k >= 25) return;

    myCom(k + 1, target)
    target.push(q[k])

    myCom(k + 1, target)
    target.pop()
    

}

bfs = (q) => {

    let row = q[0][0]
    let col = q[0][1]
    while (q.length) {

        for (let w = 0; w < 4, w++) {
            nr = row + dr[w]
            nc = col + dc[w]
            if (nr < 0 || nr >= 5 || nc < 0 || nc >= 5) continue;
            for (let i = 0; i < 7, i++){

            }
        }

    }
} 

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})