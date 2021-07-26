문제링크: [메뉴 리뉴얼](https://programmers.co.kr/learn/courses/30/lessons/72411)

---
**키워드**
- 조합(combinations)
- Counter 객체
---
<details>
<summary>최우석</summary>
<div markdown="1">

```python

from itertools import combinations
from collections import Counter

'''
1. 코스의 숫자만큼 주문의 조합을 리스트로 만든다.
2. 모든 주문의 조합을 한 리스트에 넣는다.(이 때 주문들의 순서도 정렬한다)
3. 매 코스길이 마다 가장 많이 중복된 값만 answer에 추가한다.(answer도 정렬)
---

'''

def solution(orders, course):
    answer = []
    for course_len in course:
        combinate_order = []
        for order in orders:
            # 각 주문 별로 코스의 길이 만큼 조합을 구한다.
            combinate_order += combinations(sorted(list(order)), course_len)
        # 조합이 중복되는 수를 기준으로 내림차순으로 정렬한다.
        combinate_order = Counter(combinate_order).most_common()
        # 조합이 중복된 수가 가장 많은 조합만 answer에 추가한다.
        answer += ["".join(k) for k,v in combinate_order if v > 1 and v == combinate_order[0][1]]
        
    return sorted(answer)

```

</div>
</details>

[뒤로](https://github.com/knotted-developers/Algorithm)
