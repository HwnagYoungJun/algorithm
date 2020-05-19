# Algorithm
## 1. 매일매일 알고리즘 연습
## 2. 오늘의 한가지 TIL 매일 쓰기 (200516 ~)

#### 200514
- 코드의 직관화를 위하여 변수 및 주석을 신경써서 쓰기로함

#### 200515
- 한가지 TIL 쓰기

## 

## < TIL >
### 200515
  - JS로 배열정리하는 방법 (python에서 roadList.sort(key=lambda x:x[2])랑 동일)
    ```js 
    roadList.sort((a, b) => {
      return a[2] < b[2] ? -1 : a[2] > b[2] ? 1 : 0
    })
    ```

### 200516

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




### 200517

- C # basic

  > ​	https://github.com/HwnagYoungJun/language_basic/tree/master/C%23



### 200518

- 특별히 배운게 없는것 같다.



### 200519

- heapq의 기초 사용법

  > 우선순위 큐, dijkstra등의 알고리즘을 풀 때 유용하게 쓸 수 있는 것

  ```python
  import heapq
  
  h = []
  heapq.heappush(h, (우선순위, Data)) # 첫번째 인자는 넣을 리스트, 두번째 인자의 첫번째는 우선순위 두번째는 데이터이다
  heapq.heappop() # 우선순위가 낮은거 부터 뺴서 리턴한다.
  heapq.heapify(리스트) # 리스트를 힙으로 만들어줍니다.
  ```

  