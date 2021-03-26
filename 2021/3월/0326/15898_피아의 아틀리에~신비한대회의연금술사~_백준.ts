const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input: string[] = []

function solution(): void {
    let index: number = 0
    const N: number = parseInt(input[index])
    const nr: number[] = [0, 0, 1, 1]
    const nc: number[] = [0, 1, 0, 1]
    let maxQuality: number = Number.MIN_VALUE

    let kiln: [number, string][][] = Array.from(Array(5), () => Array(5).fill([0, 'W']))

    for (let i: number = 0; i < N; i++) {
        let tempArray: [number, string][][] = Array.from(Array(5), () => Array(5).fill([0, '']))
        
        // 1. 시작 위치와 회전을 정한다.
        for (let startPos: number = 0; startPos < 4; startPos++) {
            for (let lotate: number = 0; lotate < 4; lotate++) {
                
            }
        }
    }

}


rl.on('line', line => input.push(line))
.on('close', () => {
    solution()
    process.exit()
})