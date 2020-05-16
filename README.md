# Algorithm
## 1. 매일매일 알고리즘 연습
## 2. 오늘의 한가지 TIL 매일 쓰기 (200516 ~)

#### 200515
- 코드의 직관화를 위하여 변수 및 주석을 신경써서 쓰기로함

#### 200516
- 한가지 TIL 쓰기

## 

## < TIL >
### 200516
  - JS로 배열정리하는 방법 (python에서 roadList.sort(key=lambda x:x[2])랑 동일)
    ```js 
    roadList.sort((a, b) => {
      return a[2] < b[2] ? -1 : a[2] > b[2] ? 1 : 0
    })
    ```

### 200517

- 투 포인터 알고리즘

  > 부분 합 구할 때 사용하는 알고리즘으로 시간복잡도가 O(n)으로 간단하지만 효율적이다.

  ```python
  # 2003 수들의합 백준
  left = 0
  right = 0
  S = 0
  count = 0
  
  while True:
      if S >= M:
          S -= A[left]
          left += 1
      else:
          if right == N:
              break
          S += A[right]
          right += 1
  
      if S == M:
          count += 1
  ```

  

