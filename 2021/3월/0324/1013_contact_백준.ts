import { parse } from "node:path"

const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

function solution(): void {
    let index: number = 0
    const T: number = parseInt(input[index])
    for (let testCase: number = 0; testCase < T; testCase++) {
        console.log(testCase)
        let result: string = 'YES'
        index++
        const spread: string = input[index]
        // 1. 뒤의 두자리가 01 or 그밖
        const regex1 = /01$/
        const regex2 = /1$/
        
        if (regex1.test(spread)) {
            
        } else{
            if (regex2.test(spread)) {

            } 
        }
    }

}

let input: string[] = []

rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})