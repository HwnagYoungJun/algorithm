const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []
dx = [1, -1]
solution = () => {
    let temp = input[0].split(' ').map((el) => parseInt(el))
    let subin = temp[0]
    let sister = temp[1]
    if (subin === sister) {
        console.log(0)
        console.log(1)
    } else if (subin > sister) {
        console.log(subin - sister)
        console.log(1)
    } else {
        let tteemmpp = findSister(subin, sister)
        console.log(tteemmpp[0])
        console.log(tteemmpp[1])
    }
}

findSister = (subin, sister) => {
    q = []
    q.push([subin, 0])
    limit = 2 * sister
    visit = Array(limit + 1).fill(-1)
    visit[subin] = 0
    minTime = Infinity
    cnt = 0
    while (q.length) {
        let temp = q.shift()
        let witch = temp[0]
        let time = temp[1]
        if (time > minTime) continue;
        if (witch === sister) {
            if (time === minTime) {
                cnt++
            } else {
                minTime = time
                cnt = 1
            }
        }
        let dx = [1, -1, witch]
        for (let w = 0; w < 3; w++) {
            nr = dx[w] + witch
            if (w === 0) {
                if (nr > limit) continue;
            } else if (w === 1) {
                if (nr < 0) continue;
            }
            else {
                if (nr > limit) continue;
            }
            if (visit[nr] == -1 || time + 1 <= visit[nr]) {
                q.push([nr, time + 1])
                visit[nr] = time + 1
            }
        }
    }
    return [minTime, cnt]
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})