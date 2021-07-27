> 문제

0과 1로만 이루어진 문자열 S가 있습니다. 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 합니다.

할 수 있는 행동은 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 방법입니다.

해야 하는 행동의 최소 횟수를 출력하세요,

> 예시

**입력**

- 0001100

**출력**

- 1

<details>
<summary>최우석</summary>
<div markdown=“1”>

```python
'''
0과 1로만 이루어진 문자열이 들어온다.
연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
101000101
101111101
111111101
111111111 총 3번

# 0과 1의 연속되지 않은 갯수를 구하고 더 적은 수를 반환한다.
시간 복잡도: O(N)
'''

import sys

S = sys.stdin.readline().rstrip()
count = {
  '0':0,
  '1':0
}
temp = S[0]
count[temp] += 1

for s in S:
  if temp != s:
    count[s] += 1
    temp = s

result = min(count.values())
print(result)
``` 
  
</div>
</details>
