# 국영수

문제 링크:https://www.acmicpc.net/problem/10825

> 풀이1

국어 점수는 내림차순\
영어 점수는 오름차순\
수학 점수는 내림차순\
이름은 사전 순으로 오름차순(대문자는 소문자보다 작다)\

> 실패한 첫번째 풀이
1. 아래와 같은 자료구조로 만든다.
[
  (50,60,100,'name1'),
  (80,60,50,'name2'),
  (80,70,100,'name3')
]
2. 첫 번째 for문으로 아래의 자료구조로 만든다.
{# 국어
  50:['name1'],
  80:['name2','name3']
}
3. 두 번째 for 문으로 아래의 
{# 영어
  60
}
> 답지 힌트

파이썬에서는 튜플을 원소로 하는 리스트가 있을 때, 그 리스트를 정렬하면 기본적으로 각 튜플을 구성하는 원소의 순서에 맞게 정렬된다는 특징이 있다.
예를 들어 튜플이 3개의 원소로 구성된다면 모든 원소가 첫 번째 원소의 순서에 맞게 정렬되고, 첫 번째 원소의 값이 같은 경우 두 번째 원소의 순서에 맞게 정렬되고 이와 같은 방법으로 순서대로 정렬된다는 특징이 있다.

```python
import sys
N = int(input())
students = []
for _ in range(N): # 10만
  name, ko, en, ma  = sys.stdin.readline().rstrip().split()
  ko, en, ma = map(int, [ko,en,ma])
  students.append((name,ko,en,ma))

students.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
for student in students:
  print(student[0])
```