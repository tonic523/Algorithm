# [N과 M (8)](https://www.acmicpc.net/problem/15657)

## 첫 번째 풀이

N과 M (4) 와의 차이점이 있다면 주어진 숫자들을 직접 입력한다는 것이다.\
(4) 에서는 N이 주어졌을 때 1~N의 숫자여서 python에서는 range를 통해 구현했다.\
구현은 크게 달라지는 것은 없었는데 입력된 숫자를 리스트로 만들고 내림차순으로 정렬해준다.\
그리고 조합을 만들 때 range를 통해 숫자 리스트에 하나씩 접근하는 방법으로 (4)의 구현을 수정하면 된다.

```python
for i in range(n, N+1):
    temp = list(sequence)
    temp.append(i)
    solve(i, temp)
```

```python
for i in range(n, N):
    temp = list(sequence)
    temp.append(numbers[i])
    solve(i, temp)
```