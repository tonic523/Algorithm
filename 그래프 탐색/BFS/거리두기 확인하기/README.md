문제 링크 : [거리두기 확인하기](https://programmers.co.kr/learn/courses/30/lessons/81302)

### 풀이

<details>
<summary>최우석</summary>
<div markdown=“1”>

  
```python
# 1번째 시도 실패..
# 맨해튼 거리 고려 x
# 파티션 고려 x
def validate(place):
    roles = {
        0 : [1, 2],
        1 : [0,2,3],
        2 : [0,1,3,4],
        3 : [1,2,4],
        4 : [2,3]
    }
    for r, row in enumerate(place):
        for c, column in enumerate(row):
            if column == "p":
                for role in roles[row]:
                    if place[role][c] == "p":
                        return 0
                for role in roles[column]:
                    if place[r][role] == "p":
                        return 0
    return 1
        
def solution(places):
    result = []
    for place in places:
        result.append(validate(place))
    return result
########################################################
# 2번째 시도
def around_table(place,r,c,exclude_table=False):
    around_list = [
                (r+1,c),
                (r-1,c),
                (r,c+1),
                (r,c-1)
            ]
    if exclude_table:
        around_list.remove(exclude_table)
        
    for r_, c_ in around_list:
        if 0 <= r_ <= 4 and  0 <= c_ <= 4:
            table = place[r_][c_]
            if table == "O" and not exclude_table:
                if not around_table(place, r_, c_, exclude_table=(r,c)):
                    return 0
            if table == "P":
                return 0
    return 1
                
def validate_place(place):
    for r, row in enumerate(place):
        for c, column in enumerate(row):
            if place[r][c] == "P":
                if not around_table(place,r,c):
                    return 0
    return 1

def solution(places):
    result = []
    for place in places:
        result.append(validate_place(place))
    return result
```
  
</div>
</details>

<details>
<summary>문성호</summary>
<div markdown=“1”>

```python
# 완전탐색

def solution(places):
    answer=[]
    for place in places:
        p_pos=[]
        for i,table in enumerate(place): #P가 있는 위치를 tuple로 p_pos 리스트에 담기
            index=0
            temp=[]
            while True: 
                if table.find('P', index) == -1:
                    break
                temp.append(table.find('P', index))
                index=table.find('P', index)+1
                
            p_pos.extend(list(map(lambda x:(i,x),temp)))
        
        l=len(answer)
        for j in range(len(p_pos)): 
            for pos in p_pos[j+1:]:
                dist=abs(p_pos[j][0]-pos[0])+abs(p_pos[j][1]-pos[1]) #p_pos 내 tuple끼리 맨해튼 거리 구하기
                if dist<2:  #맨해튼거리 2 미만
                    answer.append(0)
                    break
                if dist>2: #맨해튼거리 2 초과
                    continue
                if dist==2: #맨해튼거리 2인 경우의 수 3가지
                    if p_pos[j][0]==pos[0] and place[pos[0]][int((p_pos[j][1]+pos[1])/2)]=='O':
                        answer.append(0)
                        break
                    if p_pos[j][1]==pos[1] and place[int((p_pos[j][0]+pos[0])/2)][pos[1]]=='O':
                        answer.append(0)
                        break
                    if place[p_pos[j][0]][pos[1]]=='O' or place[pos[0]][p_pos[j][1]]=='O':
                        answer.append(0)
                        break
            if l != len(answer): #맨해튼거리 조건 불만족 시 answer에 0을 추가 후 break하는데, break여부는 길이l로 검증
                break
        
        if l != len(answer): #맨해튼거리 조건 불만족 시 answer에 0을 추가 후 break하는데, break여부는 길이l로 검증
            continue
        else:
            answer.append(1) #맨해튼거리 조건 불만족 시 answer에 0을 추가 후 break하는데, break안됐으면 1 추가
                
    return answer
```
  
</div>
</details>

<details>
<summary>정운산</summary>
<div markdown=“1”>
  
```python
from collections import deque

def bfs(x, y, room):
    
    queue = deque()
    queue.append([x, y])
    
    dx = [-1,1,0,0] 
    dy = [0,0,-1,1] 
    
    visited = [[0]*5 for _ in range(5)]
    distance = [[0]*5 for _ in range(5)]
    visited[x][y] = 1
    
    while queue: 
        x, y = queue.popleft() 
        
        for i in range(4): 
            nx = x + dx[i] 
            ny = y + dy[i] 

            if 0 > nx or nx >= 5:
                continue
            
            if ny < 0 or ny >= 5:
                continue
                
            if visited[nx][ny] > 0:  
                continue
            # 좌표 범위를 넘어가지 않고 인접한 좌표가 방문하지 않으면
                
            if room[nx][ny] == "O":
                visited[nx][ny] = 1
                #방문 확인
                distance[nx][ny] = distance[x][y] +1
                #거리 측정
                queue.append([nx,ny])
                #큐에 다음 수행할 좌표 넣기

            if room[nx][ny] == "P" and distance[x][y] < 2:
                # 인접한 사람이 있고 거리가 2보다 작으면 
                return False
    return True      

def solution(places):
    answer = [1]*5
    index = 0
    for room in places:
        for x in range(5):
            for y in range(5):
                if room[x][y] == "P":
                    if not bfs(x , y, room):
                        answer[index] = 0
        index += 1
        
    return answer
```   
                                                          
</div>
</details>
                                                          
[뒤로](https://github.com/knotted-developers/Algorithm)
