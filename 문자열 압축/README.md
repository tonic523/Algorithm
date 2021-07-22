문제 링크 : [문자열 압축](https://programmers.co.kr/learn/courses/30/lessons/60057)

## 풀이

<details>
<summary>정운산</summary>
<div markdown=“1”>

```python
def solution(s):
    if len(s) == 1:
        return 1
    answer = [] 
    w = ""
    for i in range(1, len(s)): 
        count = 1
        word = s[:i] #문자열 길이 나누기
        for j in range(i, len(s), i): #i부터 시작해서 i만큼
            if s[j:j+i] == word:
                count += 1
            else:
                if count == 1:
                    count = ""
                w += str(count)+word
                word = s[j:j+i]
                count = 1  
            
        if count == 1:
            count = ""
        w += str(count)+word
        answer.append(len(w))
        w = ""
    return min(answer)  
```
  
</div>
</details>

[뒤로](https://github.com/knotted-developers/Algorithm)
