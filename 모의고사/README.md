문제링크: [모의고사](https://programmers.co.kr/learn/courses/30/lessons/42840)
<details>
<summary>최우석</summary>
<div markdown="1">

```python
# 1번째 풀이
def solution(answers):
    result = []
    students = {
        0:(1,2,3,4,5),
        1:(2,1,2,3,2,4,2,5),
        2:(3,3,1,1,2,2,4,4,5,5)
    }
    students_score = [0,0,0]
    for idx, answer in enumerate(answers):
        if students[0][idx%5] == answer:
            students_score[0] += 1
        if students[1][idx%8] == answer:
            students_score[1] += 1
        if students[2][idx%10] == answer:
            students_score[2] += 1
    max_score = max(students_score)
    for student, student_score in enumerate(students_score):
        if student_score == max_score:
            result.append(student+1)
    return result
테스트 10 〉	통과 (1.57ms, 10.2MB)
테스트 11 〉	통과 (2.94ms, 10.3MB)
테스트 12 〉	통과 (2.82ms, 10.3MB)
테스트 13 〉	통과 (0.23ms, 10.3MB)
테스트 14 〉	통과 (3.11ms, 10.3MB)

# 2번째 풀이(list comprehension으로 수정)
def solution(answers):
    result = []
    students = (
        (1,2,3,4,5),
        (2,1,2,3,2,4,2,5),
        (3,3,1,1,2,2,4,4,5,5)
    )
    students_score = [0,0,0]
    for idx, answer in enumerate(answers):
        if students[0][idx%5] == answer:
            students_score[0] += 1
        if students[1][idx%8] == answer:
            students_score[1] += 1
        if students[2][idx%10] == answer:
            students_score[2] += 1
    max_score = max(students_score)
    return [student+1 for student, student_score in enumerate(students_score)
           if student_score == max_score]
테스트 10 〉	통과 (1.59ms, 10.3MB)
테스트 11 〉	통과 (3.06ms, 10.3MB)
테스트 12 〉	통과 (4.01ms, 10.3MB)
테스트 13 〉	통과 (0.22ms, 10.3MB)
테스트 14 〉	통과 (3.12ms, 10.4MB)

# 3번째 풀이(반복되는 조건문을 for 문으로 수정)
def solution(answers):
    result = []
    students = (
        (1,2,3,4,5),
        (2,1,2,3,2,4,2,5),
        (3,3,1,1,2,2,4,4,5,5)
    )
    students_score = [0,0,0]
    for idx, answer in enumerate(answers):
        for s, student in enumerate(students):
            if student[idx%len(student)] == answer:
                students_score[s] += 1
    max_score = max(students_score)
    return [student+1 for student, student_score in enumerate(students_score)
           if student_score == max_score]
테스트 10 〉	통과 (2.70ms, 10.3MB)
테스트 11 〉	통과 (5.67ms, 10.3MB)
테스트 12 〉	통과 (5.01ms, 10.3MB)
테스트 13 〉	통과 (0.98ms, 10.4MB)
테스트 14 〉	통과 (5.27ms, 10.1MB)
```

</div>
</details>
<details>
<summary>김경래</summary>
<div markdown="1">

```python
def solution(answers):
    a = [1, 2, 3, 4, 5]  # 5개 반복
    b = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개 반복
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개 반복

    a_count, b_count, c_count = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == a[i % 5]:
            a_count += 1
        if answers[i] == b[i % 8]:
            b_count += 1
        if answers[i] == c[i % 10]:
            c_count += 1
    counts = [a_count, b_count, c_count]

    answer = []
    for index, count in enumerate(counts):
        if count == max(counts):
            answer.append(index + 1)

    return answer
```

</div>
</details>

</div>
</details>
<details>
<summary>정운산</summary>
<div markdown=“1”>

```python
#첫번째 잘 못 된 풀이 answers로 나오는 배열의 개수대로 짜맞출려고하니 오류가 많이 생김
def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one = one*2
    if len(answers) <= 10:
        one_number = 0
        two_number = 0
        three_number = 0
        share = len(answers)//10 
        rest = len(answers)%10
        one = one*share + one[rest]
        two = two*share + two[rest]
        three = three*share
        for i in range(len(answers)):
            if one[i] == answers[i]:
                one_number += 1
            if two[i] == answers[i]:
                two_number += 1
            if three[i] == answers[i]:
                three_number += 1
        number = [one_number, two_number, three_number]
        answer = []
        for i in range(len(number)):
            if max(number) == number[i]:
                answer.append(i+1)
        return answer
    elif len(answers) > 10:
        one_number = 0
        two_number = 0
        three_number = 0
        for i in range(len(answers)):
            if one[i] == answers[i]:
                one_number += 1
            if two[i] == answers[i]:
                two_number += 1
            if three[i] == answers[i]:
                three_number += 1
        number = [one_number, two_number, three_number]
        answer = []
        for i in range(len(number)):
            if max(number) == number[i]:
                answer.append(i+1)

#두번째 풀이 answrs배열의 길이로 나눠 나온 나머지로 counting한다
def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_count = 0
    two_count = 0
    three_count = 0
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            one_count += 1
        if answers[i] == two[i%len(two)]:
            two_count += 1
        if answers[i] == three[i%len(three)]:
            three_count +=1
            
    count_list = [one_count, two_count, three_count]
    answer = []
    for i in range(len(count_list)):
        if count_list[i] == max(count_list):
            answer.append(i+1)
    return answer
```

</div>
</details>
