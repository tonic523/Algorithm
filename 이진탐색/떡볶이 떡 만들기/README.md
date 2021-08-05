# 떡볶이 떡 만들기
> 문제

동빈이네 떡볶이 떡은 떡의 길이가 일정하지 않다.\
대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.\
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다.\
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.\
예를 들어 19,14,10,17인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 잘린 떡의 길이는 차례대로 4,0,0,2이다. 손님은 6만큼의 길이를 가져간다.\
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해\
절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요.

> 입력
- 떡의 개수 N, 요청한 떡의 길이 M
- (1<=N<1000000,1<=M<=2000000000)
- 둘째 줄에는 떡의 개별 높이가 주어진다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.\
4 6\
19 15 10 17

> 출력

15

---
> 풀이1

적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정합니다.
'현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤 조건의 만족 여부에 따라서 탐색 범위를 좁혀서 해결할 수 잇습니다.
절단기의 높이는 0~10억까지의 정수 중 하나입니다.
이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 합니다.

1. 배열을 오름차순으로 정렬합니다.
2. start=가장작은값, end=가장큰값 으로 인자를 받습니다.
3. 중간값(mid) = 큰값+작은값 // 2
4. 중간값으로 잘랐을 때 총 합이 M 과 같다면 중간값을 반환
4-1. 중간값으로 잘랐을 때 총 합이 M보다 크다면 start=mid
4-2. 중간값으로 잘랐을 때 총 합이 M보다 작다면
end = mid
5. 3~4번을 반복하다가 중간값을 구할 때 start와 값이 갔다면 중간값을 반복합니다.
```python
def binary_search(array,M,start,end):
  while True:
    mid = (start+end)//2
    # 중간값이 시작점과 같다면 중간값 출력
    if mid == start:
      return mid
    result = 0
    # 중간값으로 떡을 잘랐을 때 총 길이 계산
    for a in array:
      if a-mid > 0:
        result += a-mid
    # 떡의 총 길이가 요구하는 길이와 같다면 출력
    if result == M:
      return mid
    # 떡의 길이가 요구하는 것보다 크다면 시작점을 중간값으로
    elif result > M:
      start = mid
    # 작다면 중간값을 끝점으로
    else:
      end = mid

N,M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
H = binary_search(array,M,array[0],array[-1])
print(H)
```

> 풀이2
1. start = 0, end = 배열 가장 큰 값
2. start와 end의 중간값을 높이로 해서 떡길이를 구한다.
2-1. 떡길이가 크면 결과에 높이값을 넣고 start를 중간값+1로 넣고 2번을 반복한다.
2-2. 떡길이가 적다면 end에 중간값-1로 넣고 다시 2번부터 반복한다.
```python
def binary_search(array,M,start,end):
  result = 0
  while(start <= end):
    total = 0
    mid = (start+end)//2
    # 중간값으로 떡을 잘랐을 때 총 길이 계산
    for a in array:
      if a-mid > 0:
        total += a-mid
    # 떡의 총 길이가 요구하는 길이보다 작을 때
    if total < M:
      end = mid - 1
    # 떡의 총 길이가 요구하는 길이가 같거나 클 때
    else:
      result = mid
      start = mid + 1
  return result

N,M = map(int,input().split())
array = list(map(int,input().split()))
start = 0
end = max(array)
H = binary_search(array,M,start,end)
print(H)
```