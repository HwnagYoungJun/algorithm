# Algorithm
## 1. 매일매일 알고리즘 연습 (200418 ~)
## 2. 오늘의 한가지 TIL 매일 쓰기 (200516 ~)


#### 200514
- 코드의 직관화를 위하여 변수 및 주석을 신경써서 쓰기로함

#### 200515
- 한가지 TIL 쓰기

#### 200525
- 폴더 구조 변경

#### 200604
- 매일매일은 구지 쓰지 말기 ^^

#### 200613
- 무작위로 

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
  
### 200520
- JS에서 조합짜기
```js
my_com = (k, n, r, com) => {
  if (com.length === r) {
      // 여기에서 하고싶은 것을 하자.
      // ex)console.log(com)
      return;
  }
  if (k === n) return;
  my_com(k + 1, n, r, com)
  com.push(chicken[k])
  my_com(k + 1, n, r, com)
  com.pop()  
}
```



### 200521

- C# struct 만들기

  > python에는 없는듯한 C#에서 사용하는 나만의 지정형태
  >
  > 이걸 사용하면 Queue, Stack등에서 사용하기가 편하다 

  ```c#
  static class Pos
  {
      public int x;
      public int y;
  
      public Pos(int x, int y)
      {
          this.x = x;
          this.y = y;
      }
  }
  ```




### 200522

- dijkstra 우선 순위 큐로 구현하기

  > 우선 순위 큐로 구현하면 노드의 수에 비해 간선의 수가 엄청 많지 않다면 시간이 더 빠를 가능성이 높다

  > 우선순위 큐 : ElogV , 우선순위 큐 X : V^2 + E

  ```python
  # 1. 우선 순위 큐
  def dijkstar():
      dijk = [float('inf') for _ in range(N + 1)]
      dijk[0] = 0
      p_q = []
      p_q.append((0, 0))
      heapq.heapify(p_q)
  
      while p_q:
          _, this_node = heapq.heappop(p_q)
          for cost, next_node in go_to[this_node]:
              via = cost + dijk[this_node]
              if dijk[next_node] > via:
                  dijk[next_node] = via
                  heapq.heappush(p_q, (via, next_node))
  	
      return dijk
  
  
  # 2. 우선 순위 큐 X
  def dijkstar():
       dijk = [float('inf') for _ in range(N + 1)]
       dijk[0] = 0
       visit = [0 for _ in range(N + 1)]
       visit[0] = 1
       index = 0
      
       while True:
           for next_index, cost in go_to[index]:
               if visit[next_index] == 0:
                   via = dijk[index] + cost
                   if via < dijk[next_index]:
                       dijk[next_index] = via
           visit[index] = 1
  
           min_distance = float('inf')
          
           for i in range(N + 1):
               if min_distance > dijk[i]:
                   if visit[i] == 1:
                       continue
                   index = i
                   min_distance = dijk[i]
          
           if min_distance == float('inf'):
               break
  
       return dijk
  ```

  

### 200523

- C# 빠른출력 및 List 메서드

  ```c#
  // 빠른출력을 위한 StringBuilder
  using System.Text;
  
  static StringBuilder sb;
  sb = new StringBuilder();
  sb.Append("출력");
  Console.WriteLine(sb.ToString());
  
  // List<> 메서드
  
  List.Count // 인덱스 길이를 반환 ()가 없음
  List.IndexOf('찾을것') // 찾을것의 인덱스을 반환
  List.Contains('찾을것') // 찾을것이 있는지를 bool 형식으로 반환
  ```



### 200524

- LIS(가장 긴 증가하는 부분 수열) O(NlogN)으로 설계하는 방법

  > 기본적인 동적계획법은 O(N^2)이지만 이진탐색과 아이디어를 사용한다면 O(NlogN)으로 설계 가능!

  참고한 곳 :  https://shoark7.github.io/programming/algorithm/3-LIS-algorithms

  ​					 https://www.crocus.co.kr/681

  ```python
  def lis(arr):
      C = [float('inf') for _ in range(A + 1)]
      C[0] = float('-inf')
      C[1] = arr[0]
      longest = 1
  
      def search(lo, hi, n):
          if lo == hi:
              return lo
          elif lo + 1 == hi:
              return lo if C[lo] >= n else hi
  
          mid = (lo + hi) // 2
          if C[mid] == n:
              return mid
          elif C[mid] > n:
              return search(lo, mid, n)
          else:
              return search(mid + 1, hi, n)
      
      for n in arr:
          if C[longest] < n:
              longest += 1
              C[longest] = n
          else:
              next_loc = search(0, longest, n)
              C[next_loc] = n
      
      return longest
  
  A = int(input())
  A_list = list(map(int, input().split()))
  
  print(lis(A_list))
  ```



### 200525

- LIS문제에서 수열 나타내기

  > 0524에서 적은 코드에서 C리스트는 비교를 위한 수열이지 실제 수열은 아니다.
  >
  > 실제 수열을 구하기 위해서는 다른 수열을 만들 필요가 있다.

  참고한 곳 : https://www.crocus.co.kr/681

- 코드 : https://github.com/HwnagYoungJun/Algorithm/blob/master/5%EC%9B%94/0525/14003_%EA%B0%80%EC%9E%A5%EA%B8%B4%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B45_%EB%B0%B1%EC%A4%80.py

### 200602

- 플로이드 와샬 알고리즘
  
  > 시간복잡도 n^3의 알고리즘
- 코드 : https://github.com/HwnagYoungJun/Algorithm/blob/master/5%EC%9B%94/0530/11404_%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C_%EB%B0%B1%EC%A4%80.py
```python
for mid in range(n): # 중간 경로 for문이 제일 상위로 와야 누락 되지 않는다.
    for start in range(n):
        for end in range(n):
            if start == end: # 자기 자신으로 오는 경우는 없으므로 0
                bus_list[start][end] = 0
            else:
                bus_list[start][end] = min(bus_list[start][end], bus_list[start][mid] + bus_list[mid][end])
```



### 200604

- 잘 못 구현한 다익스트라 알고리즘 저격하기

  > 기본적인 다익스트라 알고리즘도 실수가 있을 수 있다. 항상 생각하자

- http://www.secmem.org/blog/2019/01/09/wrong-dijkstra/

### 200608

- 오일러 경로 (한붓그리기)

### 200612

- 만약 모든 노드에서 모든 간선으로 갈 수 있다면 크루스칼 보다 프림이 더 빠르다. (간선이 엄청많기떄문!)
