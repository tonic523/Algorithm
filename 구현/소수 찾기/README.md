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

<details>
<summary>최우석</summary>
<div markdown=“1”>

```python
from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    com_num = []
		# numbers에서 조합할 수 있는 모든 수 구하기
    for i in range(1, 8): # 7
        com_num += list(permutations(numbers,i))
    com_num = list(map(lambda x:int(''.join(x)),com_num))
    com_num = list(set(com_num))

    # 구한 수를 모두 탐색하여 소수 찾기
		## 1.구한 수의 4~루트(수)까지 나누었을 때 모두 나머지가 있다면 소수(1673.ms)
    for c_num in com_num:
        if c_num in (0,1):
            continue
        if c_num in (2,3):
            answer += 1
            continue
        validate_max = int(c_num**(1/2))+1
        for i in range(4,validate_max):
            if not c_num % i:
                break
            if i == validate_max-1:
                answer += 1
		## 2.구한 수의 반 값까지 나누었을 때 모두 나머지가 있다면 소수(9.43ms)
		for c_num in com_num:
        if c_num in (0,1):
            continue
        if c_num in (2,3):
            answer += 1
            continue
        validate_max = int(c_num*(1/2))+1
        for i in range(4,validate_max):
            if not c_num % i:
                break
            if i == validate_max-1:
                answer += 1
    return answer
```
  
</div>
</details>

