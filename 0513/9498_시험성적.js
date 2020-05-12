const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

var input = [];
var index = 0;

rl.on('line', function(line) {

    input.push(line);

}).on('close', function() {

    solution();
    process.exit();
})
function solution() {
    let score = parseInt(input[0]);
    let result;
    if (90 <= score && score <= 100) {
        result = 'A';
    }else if (80 <= score && score < 90) {
        result = 'B';
    }else if (70 <= score && score < 80) {
        result = 'C';
    }else if (60 <= score && score < 69) {
        result = 'D';
    }else {
        result = 'F';
    }
    console.log(result);
}