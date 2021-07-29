
# 음료수 얼려 먹기
> 문제

N * M 크기의 얼음 틀이 있다.
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이 때 얼음 틀의 모양이 주여졌을 때 생성되는 총 아이스크림의 갯수를 구하는 프로그램을 작성하시오.
> 입력

00110
00011
11111
00000
> 출력

3

---

<details>
<summary>최우석</summary>
<div markdown=“1”>

```python
import sys

def is_hole(graph,y,x):
	for move in moves:
		x_m = x + move[1]
		y_m = y + move[0]
		if 0 <= x_m < M and 0 <= y_m < N and graph[y_m][x_m] == "0":
			graph[y_m][x_m] = "1"
			is_hole(graph,y_m,x_m)

N,M = map(int,sys.stdin.readline().rstrip().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]   
moves = [
  (1,0),
  (0,1),
  (-1,0),
  (0,-1)
]
result = 0

for r,row in enumerate(graph):
  for c,col in enumerate(row):
    if col == "0":
      graph[r][c] = "1"
      is_hole(graph,r,c)
      result += 1

print(result)
```
  
</div>
</details>