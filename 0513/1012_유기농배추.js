const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var index = 1;
var dr = [0, 0, -1, 1];
var dc = [-1, 1, 0, 0];
var input = [];

function solution(){
  var mnk = input[index].split(" ");
  var m = parseInt(mnk[0]);
  var n = parseInt(mnk[1]);
  var k = parseInt(mnk[2]);
  var field = Array.from(Array(n), () => Array(m).fill(0));
  for (i = index + 1; i < k + index + 1; i ++){
    var temp = input[i].split(" ");
    var col = temp[0];
    var row = temp[1];
    field[row][col] = 1;
  }
  let cnt = 0;
  for(var r = 0; r < n; r ++){
    for (var c = 0; c < m; c ++) {
      if (field[r][c] === 1) {
        cnt ++;
        dfs(r, c, field, n, m);
      }
    }
  }
  console.log(cnt);
  index = i;

}

function dfs(row, col, graph, n, m) {
  graph[row][col] = 0;
  for (let w = 0; w < 4; w ++){
    var nr = row + dr[w];
    var nc = col + dc[w];
    if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
      if(graph[nr][nc] === 1){
        dfs(nr, nc, graph, n, m);
      }
    }
  }
}

rl.on('line', function(line){
  input.push(line);
}).on('close', function(){
  
  for(var test_case = 0; test_case < input[0]; test_case ++) {
    solution();
  }
})


