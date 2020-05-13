const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})
var input = []

solution = () => {
    let ap = input[0].split(" ")
    var a = ap[0]
    var p = parseInt(ap[1])
    var numbers = [a]
    si = 0
    // 만약 선언되지 않은 변수에 값을 할당하면, 자동적으로 전역변수로 바뀐다.
    make_number(numbers, a, p)
    console.log(si)
}
make_number = (numbers, before_number, p) => {
    let num_list = before_number.split('')
    let total = 0;
    for (let i = 0; i < num_list.length; i ++) {
        total += parseInt(num_list[i]) ** p
    }
    let total_string = String(total)
    let index = numbers.indexOf(total_string)
    if (index !== -1){
        si = index
    }
    else {
        numbers.push(total_string)
        make_number(numbers, total_string, p)
    }
}

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})
