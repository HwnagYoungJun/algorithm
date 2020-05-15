// 1. 사실 난이도를 보면 includes를 써도 돌아갈 듯하지만 KMP 연습을 해보자
// <TIL>
// 1. KMP는 1) 테이블 만들기 2) 문자열 순회 두단계로 이루어져있다.
// 2. 참고한 url (이종우 git)
// https://github.com/jongwoo328/TIL/blob/master/Algorithm/MST/Kruskal.md
// 3. JS가 익숙하지 않아 은근히 입력 받는데 오래걸렸다. teseCase를 숫자로 주지 않아서 당황했다.
// <궁금한점>
// 1. 테이블이 소용없는 경우를 미리 알 수 있지않을까?
// 2. 보이어-무어가 더 빠른 이유는 뭘까?

const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []
index = 0

solution = () => {
    kr = input[index].split(' ')
    if (kr == '') return;
    const keyword = kr[0]
    const reference = kr[1]
    pattern = []
    makeTable(keyword, pattern)
    let isExist = findString(keyword, reference, pattern)
    let result = ''
    // 굳이 삼항연산자를 사용했다.
    isExist ? result = 'Yes' : result = 'No'
    console.log(result)
}


makeTable = (keyword, table) => {
    table.push(0)
    let i = 1
    let j = 0
    while (i < keyword.length) {
        if (keyword[j] === keyword[i]) {
            j++
            table.push(j)
            i++
        }
        else {
            if (j) j = table[j - 1];
            else {
                i++
                table.push(0)
            }
        }
    }
}

findString = (keyword, reference, table) => {
    let isExist = false
    let k = 0
    let r = 0
    let lenK = keyword.length
    let lenR = reference.length
    while (r < lenR) {
        if (keyword[k] == reference[r]) {
            k++
            r++
            if (k !== lenK) continue;
            isExist = true
            break
            // 아래는 대부분의 KMP에서는 구현하지만 이 문제에서는 갯수가 필요없으므로 구현할 필요 없다.
            // k = table[k - 1]
        }
        else r++;
        // 이 부분에서 테이블을 참조하지 않는데 KMP를 왜 썼을까라는 후회를 했다.
    }
    return isExist
}

rl.on('line', line => input.push(line))
.on('close', () => {
    t = input.length
    for (let testCase = 0; testCase < t; testCase++)
    { 
        solution()
        if (kr == '') break;
        index++
    }
    process.exit()
})