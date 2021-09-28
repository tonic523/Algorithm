# [Four Squares](https://www.acmicpc.net/problem/17626)

## 풀이1

- python 으로 풀면 시간 초과
- pypy로 풀면 통과

> 풀이 과정

다이나믹 프로그래밍과 브루트 포스를 사용하여 풀이했습니다.\
점화식 : `dp[N] = min(dp[N - 1^2], dp[N - 2^2] ... ,dp[N - i^2])`\
점화식에서 i는 i^2가 N보다 작을 때까지 반복됩니다.

## 풀이2

- python 으로 풀면 시간 초과
- pypy로 풀면 통과

> 풀이 과정

브루트 포스로 3중 for문을 사용하여 풀이했습니다.