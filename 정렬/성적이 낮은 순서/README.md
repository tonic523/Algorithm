# 성적이 낮은 순서로 학생 출력하기

> 문제

N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
> 입력

2\
홍길동 95\
이순신 77

> 출력

이순신 홍길동

---
> 풀이1

해시 테이블 키(점수), 값(학생들<리스트>)로 만든다.
입력을 할 때 점수 값이 키에 이미 있다면 값에 학생을 추가하고 없다면 키와 학생이 담긴 리스트를 추가한다.
0~100까지 키를 호출하고 키가 있다면 학생들을 출력한다.

> 풀이2

풀이1과 비슷하게 만들지만 이번엔 리스트안의 튜플 값으로(점수,이름)을 담는다.
이 리스트를 정렬할 때 각 요소마다 튜플의 첫번째 값을 키로 정렬한다.

```python
import sys

## 첫번째 풀이 ###################
N = int(input())
grade_students = {}
for _ in range(N):
  name, grade = sys.stdin.readline().rstrip().split()
  grade = int(grade)
  if grade in grade_students:
    grade_students[grade].append(name)
  else:
    grade_students[grade] = [name]

for i in range(101):
  if i in grade_students:
    for student in grade_students[i]:
      print(student, end=" ")

## 두번째 풀이 ####################
N = int(input())
grade_students = []
for _ in range(N):
  name, grade = sys.stdin.readline().rstrip().split()
  grade = int(grade)
  grade_students.append((grade,name))

grade_students.sort(key=lambda student:student[0])

for student in grade_students:
  print(student[1], end=" ")
```