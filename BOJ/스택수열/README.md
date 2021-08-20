# 스택수열

> 문제

[스택 수열](https://www.acmicpc.net/problem/1874)

> 풀이

만들기 위한 수열을 리스트에 순서대로 저장한다.
수열을 첫번째 값(target)부터 꺼내어서 아래의 조건을 실행한다.
- 스택 리스트의 마지막 원소가 target이랑 같다면 pop 실행
- 아니라면
  - target 까지 순차적으로 값을 스택에 넣고 target에 해당하는 값은 pop(이 때 순차적인 순서가 target보다 크다면 "NO"를 출력)