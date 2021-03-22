function solution(number, k) {
    let lenNumber = number.length
    let canMinus = k
    let stack = []

    for (let n = 0; n < lenNumber; n++) {
        let intN = parseInt(number[n])
        while (canMinus > 0 && stack.length > 0 && intN > stack[stack.length - 1]) {
            let a = stack.pop()
            canMinus--
        }
        stack.push(intN)
    }
    if (canMinus !== 0) {
        stack = stack.slice(0, stack.length - canMinus)
    }
    let answer = stack.join('')
    return answer;
}