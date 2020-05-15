// 1. MST 문제다. kruscal로 풀어보자
// 2. 도로는 같은 성별끼리는 연결할 수 없다.
// 3. 연결이 안 되어 있을 수도 있다!
// <TIL>
// 1. kruscal 구현은 역시 UnionFind
// 2. for 로 배열을 탐색할 때는 for ... of
// 3. JS로 배열정리하는 방법 (python에서 roadList.sort(key=lambda x:x[2]))랑 동일
// roadList.sort((a, b) => {
//   return a[2] < b[2] ? -1 : a[2] > b[2] ? 1 : 0})
// <궁금한점>
// 1. prim vs kruscal
// 2. JS로 input을 깔끔하게 받고 싶다.

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []

solution = () => {
    const nm = input[0].split(" ").map(el => parseInt(el)) // .map(Number)
    n = nm[0]
    m = nm[1]
    const mw = input[1].split(" ")
    roadList = []
    // 필요는 없지만 입력과 index를 맞추려고 그냥 넣었다.
    for (let i = 2; i < m + 2; i++) {
        const uvd = input[i].split(" ").map(el => parseInt(el))
        u = uvd[0]
        v = uvd[1]
        if (mw[u - 1] === mw[v - 1]) continue;
        // 만약 성별이 같다면 길을 만들어 줄 필요가 없다.
        roadList.push(uvd)
    }
    roadList.sort((a, b) => {
        return a[2] < b[2] ? -1 : a[2] > b[2] ? 1 : 0
    })
    parrent = []
    for (let i = 0; i < n + 1; i++) [
        parrent.push(i)
    ]
    let totalDistance = 0
    for (let i = 0; i < roadList.length; i++) {
        const v1v2cost = roadList[i]
        const v1 = v1v2cost[0]
        const v2 = v1v2cost[1]
        const cost = v1v2cost[2]
        if (find(v1) !== find(v2)) {
            union(v1, v2)
            totalDistance += cost
        }
    }
    let standard = find(1)
    let isRoot = true
    for (let i = 1; i < n + 1; i++) {
        if (standard !== find(i)) {
            isRoot = false
            break;
        } 
    }
    let result
    isRoot ? result = totalDistance : result = -1 
    console.log(result)
}

find = (x) => {
    if (x === parrent[x]) return x;
    parrent[x] = find(parrent[x])
    return parrent[x]
}

union = (x, y) => {
    fx = find(x)
    fy = find(y)
    if (fx !== fy) parrent[fy] = fx 
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})