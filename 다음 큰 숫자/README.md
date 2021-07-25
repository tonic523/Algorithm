문제 링크 : [다음 큰 숫자](https://programmers.co.kr/learn/courses/30/lessons/12911)

### 풀이

<details>
<summary>정운산</summary>
<div markdown=“1”>
  
```python

  def solution(n):
    bin_number = bin(n)[2:]
    bin_ = "0b1" + bin_number
    for i in range(n+1, int(bin_, 2)+1):
        if bin(i)[2:].count("1") == bin_number.count("1"):
            return i
            break
```
  
</div>
</details>
