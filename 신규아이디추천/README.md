문제링크 : [신규아이디추천](https://programmers.co.kr/learn/courses/30/lessons/72410)

</div>
</details>
<details>
<summary>정운산</summary>
<div markdown=“1”>

  ```python
def solution(new_id):
    new_id = new_id.lower() #1단계 소문자 치환
    
    for i in "~!@#$%^&*()=+[{]}:?,<>/":# 2단계 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
        new_id = new_id.replace(i, "")
    
    a = [] 
    a.append(new_id[0])

    for i in range(1,len(new_id)): #3단계
        a.append(new_id[i])
        if new_id[i] == new_id[i-1] and new_id[i] == ".":
             a.pop(-1)  

    try:
        if a[-1] == ".": #4단계
            a.pop(-1)
        if a[0] == ".":#elif xx
            a.pop(0)
    except IndexError:
        pass
    if a == []: #5단계 빈 문자열이면 "a"를 대입
        a += "a"

    b = []
    if len(a) >= 16: #6단계 new_id 길이가 16자 이상이면 첫 15개까지 문자만 남긴다
        for i in range(0, 15):
                b.append(a[i])
    elif len(a) < 16:
        b = a
        if len(a) <= 2: #7단계 new_id의 길이가 2자 이하라면, 마지막 문자를 3자가 될 떄까지 반복해서 붙인다
            while len(a) < 3:
                a += a[len(a)-1]
    
    for i in reversed(range(len(b))): #만약 제거 후 마침표가 끝에 위치한다면 마침표를 제거한다
        if b[i] == ".":
            b.pop(i)
        elif b[i] != ".":
            break   
    answer = "".join(b)
    
    return answer
```
                             

</div>
</details>

</div>
</details>
<details>
<summary>최우석</summary>
<div markdown=“1”>

```python
import re

def exclude_invalid_char(str):
    # match 사용 고려
    return ''.join(re.compile('[a-z0-9-_.]').findall(str))
    
def remove_duplicate_point(str):
    return re.sub('\.{2,}', '.', str.strip('.'))
    
def solution(new_id):
    #1단계
    new_id = new_id.lower()
    #2단계
    new_id = exclude_invalid_char(new_id)
    #3,4단계
    new_id = remove_duplicate_point(new_id)
    #5,6,7단계
    if new_id: # 모듈화
        if len(new_id) >= 16:
            new_id = new_id[:15].rstrip('.')
        elif len(new_id) <= 2:
            while len(new_id) != 3:
                new_id += new_id[-1]
        return new_id
    else:
        return "aaa"
```

</div>
</details>

</div>
</details>
<details>
<summary>문성호</summary>
<div markdown=“1”>

```python
def exclude(new_id): #isalpha(),isdigit(),isalnum()
    answer=''
    for string in new_id:
        if string.isalnum() or string in ['-','_','.']:
            answer+=string
    return answer

def successive(new_id): 
    answer=''
    temp=''
    for i,string in enumerate(new_id):
        if string=='.' and not temp: #string보다는 char, 변수명은 길더라도 분명하게
            temp+=string
            answer+=string
            continue
        if string=='.' and temp:
            continue
        temp=''
        answer+=string
    return answer

def reachthree(new_id):
    while len(new_id)<3:
        new_id+=new_id[-1] #문자열 끝단, #new_id[:-1] 
    return new_id
    
def solution(new_id):

    #1
    new_id=new_id.lower()
    #2
    new_id=exclude(new_id)
    #3
    new_id=successive(new_id)
    #4
    new_id=new_id.strip('.')
    #5
    new_id='a' if not new_id else new_id
    #6
    new_id=new_id[:15] if len(new_id)>15 else new_id
    new_id= new_id.rstrip('.')
    #7
    new_id=reachthree(new_id)
    
    return new_id
```
  
</div>
</details>
