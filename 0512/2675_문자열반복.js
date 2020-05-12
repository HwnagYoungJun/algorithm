const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let first;
rl.on("line", function(input) {
  if (first === undefined) {
    first = parseInt(input);
    console.log(first)
  } else {
    let arr = input.split(" ");
    let str = "";
    let strArr = arr[1].split("");
    for (let i = 0; i < strArr.length; i++) {
      for (let j = 0; j < parseInt(arr[0]); j++) {
        str += strArr[i];
      }
    }
    console.log(str);
  }
}).on("close", function() {
    process.exit();
});



