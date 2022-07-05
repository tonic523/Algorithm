# [요세푸스 문제 0](https://www.acmicpc.net/problem/11866)

> 풀이1

점화식을 하나 구하면 쉽게 풀 수 있었다.
- `(beforeIndex + (K-1)) % list.size()`
  - 이전에 조회했던 리스트의 인덱스에 K-1을 더한 인덱스를 현재 리스트의 사이즈로 나눈 나머지
