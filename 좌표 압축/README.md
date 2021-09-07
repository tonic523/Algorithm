# 좌표 압축

- 입력한 값의 순위가 중요할 때
- 입력값의 갯수보다 입력값의 범위가 클 때 사용하는 방법

## 대표 문제
[BOJ 18870](https://www.acmicpc.net/problem/18870)

### 1번째 풀이
입력받은 값을 set으로 중복을 제거하고 리스트로 만든 후 오름차순으로 정렬합니다.\
입력받은 값을 돌면서 위 정렬된 리스트에서 해당 값의 인덱스를 호출하는 것으로 구현
```python
import sys
input = sys.stdin.readline

def sol18870():
    answer = []
    N = int(input())
    nums = list(map(int, input().split()))
    s_nums = sorted(list(set(nums)))
    for num in nums:
        answer.append(s_nums.index(num))
    for a in answer:
        print(a, end=" ")

if __name__ == "__main__":
    sol18870()
```
- 결과는 시간초과..

리스트에서 index() 메서드는 최악의 상황에서 O(N)의 시간복잡도를 가지고 있다.\
for문안에서 돌기 때문에 O(N^2)의 시간복잡도이고 N은 최대 100만개이기 때문에 시간초과가 발생했다.


### 2번째 풀이
```python
import sys
input = sys.stdin.readline

def sol18870():
    answer = []
    N = int(input())
    nums = list(map(int, input().split()))
    s_nums = sorted(list(set(nums)))
    dict = {s_num : i for i, s_num in enumerate(s_nums)}
    answer = [dict[num] for num in nums]
    for a in answer:
        print(a, end=" ")

if __name__ == "__main__":
    sol18870()
```
- 성공

리스트에서 index() 메서드를 사용하는 대신 정렬된 리스트의 값을 키, 인덱스를 값으로 하는 딕셔너리를 사용했다.\
이렇게 되면 nums를 for문을 돌 때 딕셔너리에서 해당 값의 순위를 얻기 위해선 O(1) 이 소모되므로 시간복잡도를 줄일 수 있다.