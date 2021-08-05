# 이진 탐색
> 리스트 내에서 데이터를 탐색하는 방법

- 순차 탐색
- 이진 탐색

## 순차 탐색
> 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

<details>
<summary>구현 코드</summary>
<div markdown=“1”>

```python
import sys

N, target = sys.stdin.readline().rstrip().split()
N = int(N)
array = sys.stdin.readline().rstrip().split()

for i in range(N):
	if array[i] == target:
    	print(array[i],i+1)
        break
```
  
</div>
</details>

## 이진 탐색
> 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.

<details>
<summary>동작 과정</summary>
<div markdown=“1”>

![](https://images.velog.io/images/tonic523/post/d3bc812a-1bee-46ae-9125-d7551c549ba6/image.png)![](https://images.velog.io/images/tonic523/post/df3bb024-747e-4d5a-bad3-d0298fc4a299/image.png)![](https://images.velog.io/images/tonic523/post/c911fe8b-1403-4d29-9662-c1cde118961c/image.png)![](https://images.velog.io/images/tonic523/post/15a45b20-82c5-44ee-917e-8bea7f003ec6/image.png)
  
</div>
</details>

<details>
<summary>소스코드</summary>
<div markdown=“1”>

```python
# 재귀함수로 구현
def binary_search(array,target,start,end):
  if start > end:
    return None
  mid = (start+end) // 2
  # 랒은 경우 중간점 인덱스 반환
  if target == array[mid]:
    return mid
  # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif target < array[mid]:
    return binary_search(array,target,start,mid-1)
  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array,target,mid+1,end)

target = 7
array = [1,3,5,7,9,11,13,15,17,19]
result = binary_search(array,target,0,len(array)-1)
if result:
  print(result+1)
else:
  print(None)
>> 4
```
```python
# 반복문으로 구현
def binary_search(array,target,start,end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid-1
    else:
      start = mid+1
  return None
target = 7
array = [1,3,5,7,9,11,13,15,17,19]
result = binary_search(array,target,0,len(array)-1)
if result:
  print(result+1)
else:
  print(None)
# >> 4
```
  
</div>
</details>

시간 복잡도 : O(logN)

### 파이썬 이진 탐색 라이브러리
- `bisect_left(a,x)`: 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- `bisect_right(a,x)`: 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

![](https://images.velog.io/images/tonic523/post/11c600ab-53ad-4120-91a4-a81ed0e1bb36/image.png)

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))
>> 2
>> 4
```

> 값이 특정 범위에 속하는 데이터 개수 구하기

```python
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
	right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))
>> 2
print(count_by_range(a, -1, 3))
>> 6
```

### 파라메트릭 서치(Parametric Search)
최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법
특정한 조건을 만족하는 가장 알맞는 값을 빠르게 찾는 최적화 문제
일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있다.





`참고 자료`\
[이코테 2021 강의 몰아보기[동빈나]](https://www.youtube.com/watch?v=94RC-DsGMLo)







