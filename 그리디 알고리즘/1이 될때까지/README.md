> 문제

자연수 N이 1이 될 때까지 1을 빼거나 K로 나누기 연산을 최소 몇번 수행해야 하는지를 계산

> 입력

- 11 3

> 출력

- 4

<details>
<summary>최우석</summary>
<div markdown=“1”>

```python
'''

- 2 이상의 K로 많이 나눌 수록 최적의 해 계산

1번째 풀이의 시간복잡도:O(N)
2번째 풀이의 시간복잡도:O(logN)
'''
### 첫번째 풀이 ###
import sys
N, K = map(int,sys.stdin.readline().split())
cnt = 0
while N != 1:
  if N % K:
    N -= 1
  else:
    N = N // K
  cnt += 1

print(cnt)

### 두번째 풀이 ###
import sys
N, K = map(int,sys.stdin.readline().split())
cnt = 0
while True:

  if N < K:
    cnt += N-1
    break

  rest = N % K
  if rest:
    N -= rest
    cnt += rest

  N = N // K
  cnt += 1
``` 
  
</div>
</details>

