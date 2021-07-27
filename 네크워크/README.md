문제 링크 : [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)

<details>
<summary>정운산</summary>
<div markdown=“1”>

```python
from collections import deque

def bfs(idx, computers, n, visited):
    queue = deque([idx])
    
    while queue:
        idx = queue.popleft()
        if not visited[idx]:
            visited[idx] = 1
            for i in range(n):
                if i == idx:
                    continue
                elif computers[idx][i] == 0:
                    continue    
                if not visited[i]:
                    queue.append(i)


def solution(n, computers):
    perfect = [1]*n
    for computer in computers:
        if perfect == computer:
            return 1
        
    for i in range(n):
        computers[i][i] = 0
        
    answer = 0
    visited = [0]*n
    for idx in range(n):
        if not visited[idx]:
            bfs(idx, computers, n, visited)
            answer += 1
            
    return answer
 ``` 
  
</div>
</details>

