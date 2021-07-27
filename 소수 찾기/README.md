문제 링크 : [소수 찾기](https://programmers.co.kr/learn/courses/30/lessons/42839)

<details>
<summary>정운산</summary>
<div markdown=“1”>

```python
from itertools import permutations

def solution(numbers):
    numbers= list(numbers)
    answer = []
    for i in range(1, len(numbers)+1):
        answer += permutations(numbers, i)
    an = []
    for i in numbers:
        an.append(int(i))
    for i in answer:
        an.append(int("".join(i)))
    an = set(an)
    n = []
    for i in an:
        b = 0
        if i == 1 or i == 0:
            b = 1
        for j in range(2, int(i** 0.5)+1):
            if i%j == 0:
                b = 1
        if b == 0:
            n.append(i)
    return len(n)
```
  
</div>
</details>
