# 정렬된 배열에서 특정 수의 개수 구하기
> 문제

 N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.
 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
 
> 입력 조건

* 1 <= N =< 1000000
* -10^9 <= x <= 10^9
* -10^9 <= 각 원소의 값 <= 10^9

> 입력

7 2\
1 1 2 2 2 2 3

> 출력

4

---
## 풀이

```python
# bisect 라이브러리를 활용해서 풀이
from bisect import bisect_left,bisect_right

x, N = list(map(int, input().split()))
array = list(map(int, input().split()))

left_index = bisect_left(array,N)
right_index = bisect_right(array,N)
result = right_index - left_index
print(result)
```