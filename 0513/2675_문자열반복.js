const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let first;
rl.on("line", function(input) {
  if (first === undefined) {
    first = parseInt(input);
    // console.log(first)
  } else {
    let arr = input.split(" ");
    // console.log(arr);
    let str = "";
    // let temp = arr[0];
    // console.log(temp);
    let strArr = arr[1].split("");
    // console.log(strArr);
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



