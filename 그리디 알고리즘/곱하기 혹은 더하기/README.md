> 문제

각 자리가 숫자로만 이루어진 문자열 S가 주어졌을 때, 
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 
숫자 사이에 'X'혹은 '+' 연산자를 넣어
결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.

> 입력
- "123"

> 출력
- 9
<details>
<summary>최우석</summary>
<div markdown=“1”>

```python
import sys

S = sys.stdin.readline().strip()
result = 0
for idx, n in enumerate(S):
  n = int(n)
  if result <= 1:
    result += n
  else:
    if n != 1:
      result *= n
    else:
      result += n
print(result)
``` 
  
</div>
</details>
