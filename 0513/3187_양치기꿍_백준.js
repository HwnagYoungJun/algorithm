const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

var input = []
var index = 1
const dr = [0, 0, -1, 1]
const dc = [-1, 1, 0, 0]

bfs = (row, col, field, visit, sr, sc) => {
    let queue = []
    queue.push([row, col])
    visit[row][col] = true
    let w = 0;
    let s = 0;
    while (queue.length) {
       let direction = queue.shift()
       let r = direction[0]
       let c = direction[1]
       if (field[r][c] === 'v') {
            w ++
        } else if (field[r][c] === 'k') {
            s ++
        }
       for (let w = 0; w < 4; w ++) {
           let nr = r + dr[w]
           let nc = c + dc[w]
           if (nr >= 0 && nr < sr && nc >= 0 && nc < sc) {
               if (field[nr][nc] !== '#' && visit[nr][nc] == false) {
                    visit[nr][nc] = true
                    queue.push([nr, nc])
               }
           }
       }
    }
    return s > w ? [s, 0] : [0, w]
}

solution = () => {
    const rc = input[0].split(" ")
    const r = parseInt(rc[0])
    const c = parseInt(rc[1])
    let wolf = 0
    let sheep = 0
    var field = []
    let visit = Array.from(Array(r), () => Array(c).fill(false))
    for (let i = index; i < r + index; i++) {
        field.push(input[i])
    }
    for (let row = 0; row < r; row ++) {
        for (let col = 0; col < c; col ++) {
            if (field[row][col] !== '#' && visit[row][col] === false) {
                let result = bfs(row, col, field, visit, r, c)
                let rs = result[0]
                let rw = result[1]
                wolf += rw
                sheep += rs
            }
        }
    }
    console.log(sheep, wolf)
}

rl.on('line', line => input.push(line))
.on('close', function(){
    solution()
    process.exit()
})
