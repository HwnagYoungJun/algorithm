const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []
result = -1
dr = [0, 0, 1]
dc = [-1, 1, 0]
solution = () => {
    const nmh = input[0].split(" ")
    n = parseInt(nmh[0])
    m = parseInt(nmh[1])
    h = parseInt(nmh[2])
    ladder = Array.from(Array(h + 2), () => Array(n + 1).fill(false))
    for (let i = 1; i < m + 1; i++) {
        const ab = input[i].split(" ")
        a = parseInt(ab[0])
        b = parseInt(ab[1])
        ladder[a][b] = true
    }
    q = []
    for (let row = 1; row <= h; row++) {
        for (let col = 1; col <= n - 1; col++) {
            if (ladder[row][col] === true ) continue;
            if (ladder[row][col + 1] === true) continue;
            if (col != 1) {
                if (ladder[row][col - 1] == true) continue;
            }
            q.push([row, col])
        }
    }
    
    for (let j = 1; j <= 3; j++){
        if (result !== -1) break;
        for (let i = 0; i < q.length - j + 1; i++){
            comVisit = Array(q.length).fill(false)
            chk = false
            my_com(q, i, 1, [q[i]], j)
            if (chk){
                result = j
            }
            break
        }
    }
    console.log(q)
    console.log(result)
}
my_com = (list, index, k, target, c) => {
    comVisit[index] = true
    if (k === c) {
        for (const rowcol of target) {
            ladder[rowcol[0]][rowcol[1]] = true
        }
        console.log(target)
        // console.log(ladder)
        for (let col = 1; col <= n; col++){
            visit = Array.from(Array(h + 2), () => Array(n + 1).fill(false))
            check = false
            dfs(1, col, col)
            // console.log(check)
            console.log('---------')
            if (!check) return;
        }
        chk = true
        // console.log('chk', chk)
        return
    }
    for (let i = index; i < q.length; i++) {
        if (comVisit[i]) continue;
        const qr = q[i][0]
        const qc = q[i][1]
        console.log([qr, qc])
        console.log([qr, qc - 1])
        console.log(target)
        console.log(target.includes([qr, qc - 1]))
        if (target.includes([qr, qc + 1]) || target.includes([qr, qc - 1])) continue;
        k ++
        comVisit[i] = true
        target.push(q[i])
        my_com(list, i, k, target, c)
        k --
        comVisit[i] = false
        target.pop()
    }
}

dfs = (row, col, destination) => {
    visit[row][col] = true
    // console.log(row, col, destination)
    if (row === h + 1) {
        if (destination === col) {
            check = true
            return     
        }
        return
    }
    for (let w = 0; w < 3; w++){
        let nr = row + dr[w]
        let nc = col + dc[w]
        // console.log(nr, nc)
        // console.log(visit[nr][nc])
        // console.log(w)
        if (nr > h + 1 || nc < 0 || nc > n) continue;
        if (visit[nr][nc] === true) continue;
        if (w === 0) {
            // console.log(ladder)
            // console.log(ladder[nr][nc])
            // console.log('*******')
            if (ladder[nr][nc] === false) continue;
        } else if(w === 1) {
            // console.log(ladder)
            // console.log(ladder[row][col])
            // console.log('*******')
            if (ladder[row][col] === false) continue;
        }
        // console.log('?')
        dfs(nr, nc, destination)
        break
    }
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})