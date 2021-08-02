### 미로 탈출
> 문제\
N * M 크기의 직사각형 형태의 미로에 갇혀 있다.\
미로에는 여러 마리의 고물이 있어 이를 피해 탈출해야한다. 나의 위치는 (1,1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다. 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시되었을 때 내가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.

> 조건\
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

> 입력\
5 6
101010
111111
000001
111111
111111

> 출력\
10

<details>
<summary>최우석</summary>
<div markdown=“1”>

```python
# 첫 번째 풀이
import sys

def bfs(maze,r,c):
  maze[r][c] = 0
  for move in moves:
    r += move[0]
    c += move[1]
    if r == M-1 and c == N-1:
      return 1
    elif 0 <= r < N and 0 <= c < M:
      if maze[r][c]:
        return 1+bfs(maze,r,c)
  return 0

N,M = map(int,sys.stdin.readline().rstrip().split())
maze = []
for _ in range(N):
  maze.append(list(sys.stdin.readline().rstrip()))
moves = [
  (1,0),
  (-1,0),
  (0,1),
  (0,-1)
]
print(1 + bfs(maze,0,0))
```
```python
# 두 번째 풀이
import sys
from collections import deque

def bfs(maze,r,c):
  dq = deque()
  dq.append((r,c))
  # 큐가 없을 때까지 반복
  while dq:
    r,c = dq.popleft()
    # 4방향 검사
    for move in moves:
      nr = r + move[0]
      nc = c + move[1]
      # 미로 바깥으로 나갔을 때
      if 0>nr or N <= nr or 0>nc or M <= nc:
        continue
      # 벽(0)을 만났을 때
      if maze[nr][nc] == 0:
        continue
      # 1 일때 지나온 경로의 값을 저장하고 큐에 추가
      if maze[nr][nc] == 1:
        maze[nr][nc] = maze[r][c] + 1  
        dq.append((nr,nc))
  return maze[N-1][M-1]

N,M = map(int,sys.stdin.readline().rstrip().split())
maze = []
for _ in range(N):
  maze.append(list(map(int,sys.stdin.readline().rstrip())))
moves = [
  (1,0),
  (-1,0),
  (0,1),
  (0,-1)
]
print(bfs(maze,0,0))
```

</div>
</details>
