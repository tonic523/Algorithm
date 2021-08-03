# 두 배열의 원소 교체
> 문제

두 개의 배열 A와 B를 가지고 있습니다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수입니다.\
동빈이는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말합니다.\
동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것입니다.\
N,K 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하세요.

> 입력

5 3\
1 2 5 4 3\
5 5 6 6 5

---

> 풀이1(선택 정렬)

A에서 가장 작은 수와 B에서 가장 큰 수를 비교한다.\
B가 더 크면 바꾸고 다음으로 작은 수와 큰 수를 비교한다.(K번까지 반복)\
작다면 바꾸지않고 그대로 A의 합을 출력한다.\
약 400억(4N * K)

> 풀이2(python 라이브러리 활용)

A와 B를 정렬한다.
A는 오름차순
B는 내림차순
A와 B 각각 첫 번째 인덱스부터 접근하고 두 수를 비교하여 A가 더 클 때까지 혹은 K번 반복이 끝날 때 까지 스위칭한다.
약 3천만(NlogN + K + N)

```python
## 첫번째 풀이 #########################################
import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

A = list(map(int,sys.stdin.readline().rstrip().split()))
B = list(map(int,sys.stdin.readline().rstrip().split()))

switch_sum = 0
for _ in range(K):
  min_a = min(A) # N
  max_b = max(B) # N
  if min_a < max_b:
    switch_sum += max_b
    A.remove(min_a) # N
    B.remove(max_b) # N
  else:
    break
print(switch_sum + sum(A))

## 두번째 풀이 #########################################
import sys

N, K = map(int,sys.stdin.readline().rstrip().split())

A = list(map(int,sys.stdin.readline().rstrip().split()))
B = list(map(int,sys.stdin.readline().rstrip().split()))

A.sort() # NlogN
B.sort(reverse=True)

for i in range(K): # K
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]
  else:
    break

print(sum(A))
```