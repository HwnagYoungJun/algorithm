const readline = require("readline");
const { listenerCount } = require("process");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

input = [];

function solution(priorities, location) {
  var answer = 0;
  let priorityArray = Array(9).fill(0);
  let tempArray = Array(priorities.length);

  for (let i = 0; i < priorities.length; i++) {
    tempArray[i] = i;
  }
  priorities.forEach((el) => {
    priorityArray[el] += 1;
  });
  while (true) {
    const thisNum = priorities.shift();
    if (thisNum === 9) {
      answer += 1;
      if (tempArray[0] === location) {
        break;
      } else {
        tempArray.shift();
      }
    } else {
      let isPossible = true;
      for (let i = thisNum + 1; i < 10; i++) {
        if (priorityArray[i] !== 0) {
          isPossible = false;
          break;
        }
      }
      if (isPossible) {
        if (tempArray[0] == location) {
          break;
        } else {
          tempArray.shift();
        }
      } else {
        tempArray.push(tempArray[0]);
        tempArray = tempArray.slice(1);
        priorities.push(thisNum);
      }
    }
    answer++;
    priorityArray[thisNum]--;
  }
  return answer;
}

rl.on("line", (line) => input.push(line)).on("close", () => {
  const pl = input[0].split(",");
  console.log(pl)
  const priorities = pl[0];
  const location = parseInt(pl[1]);
  console.log(priorities, location)
  solution(priorities, location);
  process.exit();
});
