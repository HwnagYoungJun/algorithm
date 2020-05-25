// 1. 최단경로 문제랑 비슷하다고 생각 -> 다익스트라로 설계
// 2. O(n^2)의 복잡도를 가지는 다익스트라 (125^2)
// <TIL>
// 1. 2차원배열의 다익스트라
// 2. JS의 스코프 숙련도 상승 (여러군데 쓸꺼면 선언하지 않고 쓰자)
// 3. `${testCase}` 백틱과 $로 python의 f스트링 처럼 사용할 수 있다.
// <알아볼점>
// 1. 입력을 좀 더 깔끔하게 받을 수 없을까?
// 2. 예외제거와 continue를 쓰는게 직관성이 높을까? 아니면 맞는경우를 파고 들어가는게 직관성이 높을까?

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

testCase = 0
input = []
index = 0
const dr = [0, 0, -1, 1]
const dc = [-1, 1, 0, 0]

solution = () => {
    cave = []
    for (let i = index; i < n + index; i++) {
        const temp = input[i].split(" ").map(Number)
        cave.push(temp)
    }
    index += n
    result = dijkstra()
    console.log(`Problem ${testCase}: ${result}`)
}

dijkstra = () => {
    let dijk = Array.from(Array(n), () => Array(n).fill(Infinity))
    dijk[0][0] = cave[0][0]
    let visit = Array.from(Array(n), () => Array(n).fill(false))
    visit[0][0] = true
    let currentRow = 0
    let currentCol = 0
    while (true) {
        for (let w = 0; w < 4; w++) {
            let nr = currentRow + dr[w]
            let nc = currentCol + dc[w]
            if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue;
            if (visit[nr][nc]) continue;
            let via = dijk[currentRow][currentCol] + cave[nr][nc]
            if (dijk[nr][nc] <= via) continue;
            dijk[nr][nc] = via
        }
        visit[currentRow][currentCol] = true
        let minCost = Infinity
        for (let row = 0; row < n; row++) {
            for (let col = 0; col < n; col++) {
                if (minCost <= dijk[row][col] || visit[row][col]) continue;
                minCost = dijk[row][col]
                currentRow = row
                currentCol = col
            }
        }
        if (minCost === Infinity) break;
    }  
    return dijk[n - 1][n - 1]
}

rl.on('line', line => input.push(line))
.on('close', () => {
    while (true) {
        n = parseInt(input[index])
        if (n === 0) break;
        index++
        testCase++
        solution()
    }
    process.exit()
})