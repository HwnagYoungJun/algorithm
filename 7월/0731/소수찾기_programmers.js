var answer = 0

function solution(text) {
  const textLength = text.length
  let visit2 = {}
  for (let i=1; i < textLength + 1; i++) {
    let visit = Array(textLength).fill(false)
    myPerm(text, textLength, i, 0, [], visit, visit2)
  }
  return answer
}

function myPerm(text, textLength, r, k , target, visit, visit2) {
  if (k === r) {
    var targetInt = parseInt(target.join(""))
    if (visit2[targetInt] === undefined) {
      visit2[targetInt] = true
      if (chkPrime(targetInt)) {
        answer++
      }
    }
  }
  
  for (let i= 0; i < textLength; i++){
    if (visit[i]) continue;
    visit[i] = true
    target.push(text[i])
    myPerm(text, textLength, r, k + 1, target, visit, visit2)
    visit[i] = false
    target.pop()
  }
}

function chkPrime(num) {
  if (num < 2) return false;
  if (num === 2) return true;
      for (var i = 2; i <= Math.sqrt(num); i++) {
          if (num%i===0) return false;
      }
  return true;
}