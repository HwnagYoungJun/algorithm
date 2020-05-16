// 1. 투포인터 문제
// <TIL>
// 1. 부분합 문제 같은 스타일이 아닌 투 포인터 문제는 미리 설계를 하여야 한다.
// 2. 종료조건을 생각을 많이 해줘야 한다.
// <궁금한점>
// 1. g = line 이거 왜 안먹지...

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []

solution = () => {
    let g = parseInt(input[0])
    // 투 포인터 시작.
    let r, l, result; 
    // 바로 출력할꺼라 저장리스트는 따로 만들지 않음.
    l = 1
    r = 1
    let isPossible = false // 가능한 몸무게가 있는지 판별하는 변수
    while (true) {
        result = r ** 2 - l ** 2
        // 종료 조건, r과 l의 차이가 1이지만 제곱의차가 g보다 작을 때
        if (r - l <= 1 && result > g) break
        if (result >= g) l++
        else r++
        if (result === g) {
            console.log(r)
            isPossible = true
        }
    }
    isPossible ? {} : console.log(-1)
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})