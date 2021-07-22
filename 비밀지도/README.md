문제 링크: [비밀지도](https://programmers.co.kr/learn/courses/30/lessons/17681)

### 카테고리
- 이진법
- 문자열 포맷팅

### 풀이
<details>
<summary>최우석</summary>
<div markdown=“1”>

 ```python
  # 이진법과 문자열 다루기
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        string1 = bin(arr1[i])[2:].zfill(n)
        string2 = bin(arr2[i])[2:].zfill(n)
        answer_string=""
        for j in range(n):
            if string1[j] == "1" or string2[j] == "1":
                answer_string += "#"
            else:
                answer_string += " "
        answer.append(answer_string)
    return answer

# 두번째 - zip(2개의 배열을 한번에 for문으로),
# 이진수에 or, and 메서드 활용
# rjust(문자열 길이를 지정하여 부족한 부분 pading),
# replace 메서드로 이진수를 원하는 지도값으로 변경
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        string = bin(i|j)[2:].rjust(n,"0")
        answer_string = string.replace("1","#")
        answer_string = answer_string.replace("0"," ")
        answer.append(answer_string)
    return answer
```
  
</div>
</details>
