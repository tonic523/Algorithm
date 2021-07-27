> 문제

모험가 N명은 각각 공포도 X가 있습니다. 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다. 최대 몇개의 모험가 그룹을 만들 수 있을까요?

> 입력 조건

- 첫째 줄에 모험가의 수 N이 주어진다.(1 ≤ N ≤ 100000)
- 둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분한다.

> 출력 조건

- 여행을 떠날 수 있는 그룹 수의 최댓값을 출력한다.

> 예시

**입력**

- 5
- 2 3 1 2 2

**출력**

- 2

<details>
<summary>최우석</summary>
<div markdown=“1”>

```python
### 첫번째 풀이 ###
'''
가장 적은 공포도를 가진 사람들부터 최소한의 인원으로 그룹을 만든다.
오름차순으로 하고
### 재귀 함수의 로직 ###
1. 리스트와 리스트 중 가장 적은 공포도를 가진 사람의 공포도 값이 인자로 들어간다.
2. 공포도가 남은 멤버보다 크다면 팀을 만들 수 없으므로 0 반환
3. 모험가들 중에서 공포도의 값과 비교한다.
  - 작다면 다음 모험가를 비교하고 모든 모험가가 공포도보다 작다면 팀을 만들고(+1) 팀을 구성한 모험가를 제외한 모험가들과 이 중 가장 작은 공포도로 다시 1번부터 실행한다.
    - 만약 남은 모험가들이 모두 공포도보다 작다면
    팀을 만든다.(+1) 
  - 크다면 슬라이싱 하지 않고 다음으로 큰 공포도를 가진 사람의 공포를 인자로 1번부터 실행한다.
'''
import sys

def make_group(members, scare):
  if len(members) < scare:
    return 0
  for i in range(scare):
    if members[i] > scare:
      return make_group(members,members[i])
    if i == scare - 1:
      if len(members) == i+1:
        return 1
      return 1 + make_group(members[i+1:],members[i+1])

N = int(sys.stdin.readline().rstrip())
scare_members = list(map(int,sys.stdin.readline().rstrip().split()))
# sort 시간 복잡도 = NlogN
order_scare_member = sorted(scare_members)
result = 0

result = make_group(order_scare_member, order_scare_member[0])
  
print(result)

# 시간 복잡도: Nlog(N) + N
```

```python
### 동빈나 풀이 ###
'''
1. 모험가들의 공포도를 오름차순으로 정렬한다.
2. 모험가들을 팀에 추가한다.
  - 현재 포함된 팀에 인원이 모험가의 공포도 이상이라면, 그룹 결성 (+1)
'''
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0
count = 0

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)

# 시간 복잡도: Nlog(N) + N
```
  
</div>
</details>