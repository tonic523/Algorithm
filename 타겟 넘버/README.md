문제 링크 : [타겟넘버](https://programmers.co.kr/learn/courses/30/lessons/43165)

<details>
<summary>정운산</summary>
<div markdown=“1”>
  
```python

from collections import deque
    
def solution(numbers, target):
    queue = deque()
    queue.append([0, -1])
    answer = 0
    while queue:
        number, idx = queue.popleft()
        idx += 1
        if idx < len(numbers):    
            queue.append([number+numbers[idx],idx])
            queue.append([number-numbers[idx],idx])
        else:
            if number == target:
                answer += 1
    return answer
```                              

</div>
</details>
