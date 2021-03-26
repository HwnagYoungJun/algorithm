const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input: string[] = [];

function solution() {
  function moveFireball(
    N: number,
    fireball: number[],
    checkArray: any[][],
    fireballQueue: number[][],
    overlapQueue: [number, number][]
  ): void {
    const dr: number[] = [-1, -1, 0, 1, 1, 1, 0, -1];
    const dc: number[] = [0, 1, 1, 1, 0, -1, -1, -1];
    let nr: number = 0;
    let nc: number = 0;
    const r: number = fireball[0];
    const c: number = fireball[1];
    const m: number = fireball[2];
    const s: number = fireball[3];
    const d: number = fireball[4];
    nr = r + s * dr[d];
    nc = c + s * dc[d];
    if (nr < 0) {
      nr = (nr % N) + N;
    }
    if (nr >= N) {
      nr %= N;
    }
    if (nc < 0) {
      nc = (nc % N) + N;
    }
    if (nc >= N) {
      nc %= N;
    }
    if (checkArray[nr][nc].length > 0) {
      overlapQueue.push([nr, nc]);
      if (checkArray[nr][nc].length === 1) {
        const index: number = fireballQueue.findIndex((el) => {
          return JSON.stringify(checkArray[nr][nc][0]) === JSON.stringify(el);
        });
        if (index > -1) {
          fireballQueue.splice(index, 1);
        }
      }
    } else {
      fireballQueue.push([nr, nc, m, s, d]);
    }
    checkArray[nr][nc] = [...checkArray[nr][nc], [nr, nc, m, s, d]];
  }

  function handleOverlap(
    checkArray: any[][],
    fireballQueue: number[][],
    overlapQueue: [number, number][]
  ): void {
    while (overlapQueue.length > 0) {
      const dr: number[] = [-1, -1, 0, 1, 1, 1, 0, -1];
      const dc: number[] = [0, 1, 1, 1, 0, -1, -1, -1];
      const [r, c]: [number, number] = overlapQueue.shift();
      let isFitDirection: boolean = true;
      let lastDirection: number = -1;
      let sumMass: number = 0;
      let sumSpeed: number = 0;
      checkArray[r][c].forEach((el) => {
        if (isFitDirection) {
          if (lastDirection !== -1) {
            if (lastDirection % 2 != el[4] % 2) {
              isFitDirection = false;
            }
          }
          lastDirection = el[4];
        }
        sumMass += el[2];
        sumSpeed += el[3];
      });
      let nextMass: number = Math.floor(sumMass / 5);
      let nextSpeed: number = Math.floor(sumSpeed / checkArray[r][c].length);
      if (nextMass === 0) {
        continue;
      }
      let nr: number = 0;
      let nc: number = 0;
      let directionArray: number[] = [];
      if (isFitDirection) {
        directionArray = [0, 2, 4, 6];
      } else {
        directionArray = [1, 3, 5, 7];
      }
      for (let w: number = 0; w < 4; w++) {
        fireballQueue.push([r, c, nextMass, nextSpeed, directionArray[w]]);
      }
    }
  }

  let index: number = 0;
  const NMK: string[] = input[index].split(" ");
  const N: number = parseInt(NMK[0]);
  const M: number = parseInt(NMK[1]);
  const K: number = parseInt(NMK[2]);
  let fireballQueue: number[][] = [];
  for (let m: number = 0; m < M; m++) {
    index++;
    let temp: number[] = input[index].split(" ").map((el) => parseInt(el));
    temp[0] -= 1;
    temp[1] -= 1;
    fireballQueue.push(temp);
  }
  // 1. K번 만큼 이동
  for (let command: number = 0; command < K; command++) {
    let checkArray: any[][] = Array.from(Array(N), () =>
      Array(N).fill(new Array())
    );
    let overlapQueue: [number, number][] = [];
    // 2. 파이어볼 이동
    const lengthFireballQueue: number = fireballQueue.length;
    for (let fireball = 0; fireball < lengthFireballQueue; fireball++) {
      const posFireball = fireballQueue.shift();
      moveFireball(N, posFireball, checkArray, fireballQueue, overlapQueue);
    }
    // 3. 중첩 파이어볼 처리
    handleOverlap(checkArray, fireballQueue, overlapQueue);
  }
  // 4. 합 구하기
  let result: number = 0;
  fireballQueue.forEach((el) => {
    result += el[2];
  });
  console.log(result);
}

rl.on("line", (line) => input.push(line)).on("close", () => {
  solution();
  process.exit();
});
