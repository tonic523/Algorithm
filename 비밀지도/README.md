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

<details>
<summary>문성호</summary>
<div markdown=“1”>

 ```python
 def binary(n,num): #10진수 -> 2진수 변환 함수
    temp=[]
    while True:
        temp.append(num%2)
        if num==1 or num==0:
            break
        num=num//2
    while len(temp)!=n:
        temp.append(0)
    temp = temp[::-1]
    temp = list(map(str,temp))
    binary_num = ''.join(temp)
    return binary_num

def solution(n, arr1, arr2):
    
    binary_arr1=[]
    for num in arr1:
        binary_arr1.append(binary(n,num)) #arr1을 이진수로 변환
        
    binary_arr2=[]
    for num in arr2:
        binary_arr2.append(binary(n,num))
    
    bin_all = list(zip(binary_arr1,binary_arr2)) #arr2를 이진수로 변환
    
    answer=['']*n
    for i,v in enumerate(bin_all):
        for j in range(n):
            if v[0][j]=='1' or v[1][j]=='1': #arr1과 arr2를 비교하여 answer 완성
                answer[i]+='#'
            else: answer[i]+=' ' #문자열에 빈 칸 더할 때 주의
                
    return answer
 
 ```
  
</div>
</details>
