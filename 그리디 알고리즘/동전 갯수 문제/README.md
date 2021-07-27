> 문제

카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 갯수를 구하라.(단 N은 항상 10의 배수)

> 입력

- "1260"

> 출력

- 6

<details>
<summary>최우석</summary>
<div markdown=“1”>

```python
# 동전 갯수 문제
N = int(input())
count_coin = 0

coin_list = [500,100,50,10]

for coin in coin_list:
  count_coin += N // coin
  N %= coin

print(count_coin)
# 시간 복잡도는 O(N)
# 정당성: 큰 단위가 항상 작은 단위의 배수 형태
# 화폐의 단위가 서로 배수 형태가 아닌 무작위로 주어진 경우 그리디 알고리즘으로 해결할 수 없다.
```
  
</div>
</details>