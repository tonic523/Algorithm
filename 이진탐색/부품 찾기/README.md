# 부품 찾기
> 문제

동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
> 입력 조건
* 첫째 줄에 정수 N이 주어진다.(1<= N <= 1000000)
* 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.
이때 정수는 1보다 크고 1000000이하이다.
* 셋째 줄에는 정수 M이 주어진다.(1<= M <= 100000)
* 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다.
이때 정수는 1보다 크고 1000000이하이다.
>입력

5\
8 3 7 9 2\
3\
5 7 9
>출력

no yes yes

```python
# 이진 탐색 -> O(NlogN)
def binary_search(array, target):
  start = 0
  end = len(array)
  while(start <= end):
    mid = (start+end)//2
    if array[mid] == target:
      return True
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return False


N = int(input())
store = list(map(int, input().split()))
M = int(input())
request = list(map(int, input().split()))
store.sort()

for item in request:
  if binary_search(store,item):
    print("yes", end=" ")
  else:
    print("no", end=" ")
```
```python
# 계수 정렬 -> O(N)
array = [0] * 10000001

N = int(input())
store = list(map(int, input().split()))
M = int(input())
requests = list(map(int, input().split()))

for item in store:
  array[item] = 1

for request in requests:
  if array[request]:
    print("yes", end=" ")
  else:
    print("no", end=" ")
```
```python
# 집합 자료형 사용 -> 집합 자료형에서 특정 원소 찾는 시간 복잡도(in) = O(n)
N = int(input())
store = set(list(map(int, input().split())))
M = int(input())
requests = list(map(int, input().split()))

for request in requests:
  if request in store:
    print("yes", end=" ")
  else:
    print("no", end=" ")
```