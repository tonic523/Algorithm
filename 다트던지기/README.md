[문제보기](https://programmers.co.kr/learn/courses/30/lessons/17682/solution_groups?language=python3)

--------
**키워드**  
문자열, 정규표현식


<details>
<summary>문성호</summary>
<div markdown=“1”>

```python
  
# 1차실패 : 옵션이 없는 경우 ' '를 추가해서, point/bonus/option을 리스트에 나눠담으려했으나 구현 실패
  
def solution(dartResult): 
    # i=2
    # for i in range(len(dartResult)):
    #     if dartResult[i].isdigit() and dartResult[i-1].isalpha():
    #         listResult=list(dartResult)
    #         listResult.insert(i,' ')
    #         dartResult=''.join(listResult)
    # print(dartResult)
    # point = [result for result in dartResult if result.isdigit()]
    # bonus = [result for result in dartResult if result.isalpha()]
    # option = [result for result in dartResult if result in ['*','#',' ']]
 
  
  -------------
 
 #2차 성공(refactoring 필요..)
  
 def solution(dartResult):
  
    while '10' in dartResult:
        dartResult = dartResult.replace('10','!') #10이 있는 경우 예외처리
    
    answer=[]
    for result in dartResult:
        
        if result=='!':  #10이 있는 경우
            temp_point=[]
            temp_point.append('10')
        if result.isdigit(): #10외 숫자인 경우
            temp_point=[]
            temp_point.append(result)
        if result.isalpha(): #SDT 인 경우
            if result == 'S':
                temp_point[0]=int(temp_point[0])
            if result == 'D':
                temp_point[0]=int(temp_point[0])**2
            if result == 'T':
                temp_point[0]=int(temp_point[0])**3
            answer.append(temp_point[0])
        if result in ['*','#'] : #옵션 있는 경우
            if result == '#':
                answer[-1]=answer[-1]*-1
            if result == '*' and len(answer)==1:
                answer[0]=answer[0]*2
            if result == '*' and len(answer)!=1:
                answer[-1]=answer[-1]*2
                answer[-2]=answer[-2]*2
    answer = sum(answer)
    
    return answer
```
  
</div>
</details>

[뒤로](https://github.com/knotted-developers/Algorithm/blob/main/README.md)
