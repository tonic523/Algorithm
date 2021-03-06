# [피보나치 수 6](https://www.acmicpc.net/problem/11444)

## 풀이1
이 문제는 수학적인 개념도 알고 있어야 하는 문제였다.\
입력값의 수가 말도 안되게 크기 때문에 dp로 풀이하더라도 시간초과가 날 수 밖에 없었다.\
[참고](https://st-lab.tistory.com/252)

> 행렬로 풀이

- F(n+2) = F(n+1) + F(n)

위 식을 행렬 꼴로 만들어야 한다.\
아직 왜 행렬 꼴로 만들어야 하는지 잘은 모르지만 결론은 아래같은 식을 만들기 위해서 인 것 같다.
- Ax = b

참고자료를 보면 놀랍게도 아래의 식으로 n번째의 피보나치 수를 구할 수 있다.
- `U(n) = A^n * U(0)`
- U(n) -> n번째 행렬 `[[F(n+1)], [F(n)]]`
- A -> `[[1, 1], [1, 0]]`
- U(0) -> 0번째 행렬 `[[F(1)], [F(0)]] -> [[1], [0]]`

위 식은 `행렬 제곱`, `분할 정복` 방법으로 logN의 횟수로 풀이할 수 있게된다.



