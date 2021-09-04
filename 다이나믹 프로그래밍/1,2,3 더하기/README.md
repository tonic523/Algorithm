# [1,2,3 더하기](https://www.acmicpc.net/problem/9095)

> 풀이1

다이나믹 프로그래밍으로 풀이\
점화식: f(n) = f(n-1) + f(n-2) + f(n-3)

> 풀이2

위의 점화식을 다르게 풀이하면\
`list[n] = sum(list[-3:n])`