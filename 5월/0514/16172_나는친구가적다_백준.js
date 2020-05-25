const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

input = []

solution = () => {
    const t_reference = input[0]
    const keyword = input[1]
    let reference = []
    for (let i = 0; i < t_reference.length; i++) {
        if (!isNaN(parseInt(t_reference[i]))) continue;
        reference.push(t_reference[i])
    }
    let pattern = Array(keyword.length).fill(0)
    makeTable(keyword, pattern)
    console.log(KMP(keyword, reference, pattern))
}

makeTable = (keyword, table) => {
    let i = 1
    let leng = 0
    while (i < keyword.length) {
        if (keyword[i] === keyword[leng]) {
            leng++
            table[i] = leng
            i++
        }
        else {
            if (leng) {
                leng = table[leng - 1]
            }
            else {
                table[i] = 0
                i++
            }
        }
    }
}

KMP = (keyword, reference, table) => {
    let cnt = 0
    let k = 0
    let r = 0
    let lenK = keyword.length
    let lenR = reference.length
    while (r < lenR) {
        if (keyword[k] === reference[r]) {
            k++
            r++
            if (k === lenK) {
                return 1
            }
        }
        else {
            if (k) {
                k = table[k - 1]
            }
            else {
                r++
            }
        }
    }
    return 0
}

rl.on('line', line => input.push(line))
.on('close', () =>{
    solution()
    process.exit()
})