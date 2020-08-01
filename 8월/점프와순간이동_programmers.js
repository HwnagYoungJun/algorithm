function solution(n) {
  let ans = 0;
  while (n !== 0) {
    console.log(n);
    if (!(n % 2)) {
      n /= 2;
    } else {
      n--;
      ans++;
    }
  }
  return ans;
}
