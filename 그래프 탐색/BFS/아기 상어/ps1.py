import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []

move = (
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0)
)
# 상어의 위치, 크기, 먹은양, 총 걸린 시간
shark_pos = (0,0)
shark_size = 2
shark_ate = 0
total_time = 0

# 그래프 생성
for i in range(N):
    M = list(map(int, input().rstrip().split()))
    graph.append(M)
    # 그래프 중 9인 값에 상어 위치 저장 후 해당 위치 0으로 저장
    for j in range(N):
        if M[j] == 9:
            graph[i][j] = 0
            shark_pos = (i, j)

while True:
    # 상어의 시작 위치와 걸린 시간 초기화
    queue = deque([(shark_pos[0], shark_pos[1], 0)])
    # 방문한 위치 초기화
    visited = set()
    # 현재 위치 방문 처리
    visited.add(str(shark_pos[0]) + str(shark_pos[1]))
    # 먹을 수 있는 물고기의 위치와 걸린 시간 초기화
    fish_pos = (1e9, 1e9)
    to_fish_time = 1e9
    # 상어가 이번 순회해서 먹었는지 확인하는 값도 초기화
    isAte = False
    # 순회 시작(BFS)
    while queue:
        r, c, time = queue.popleft()
        # 4방향 이동
        for m in move:
            m_r = r + m[0]
            m_c = c + m[1]
            # 그래프안에 위치이고 방문하지 않았다면
            if 0 <= m_r < N and 0 <= m_c < N and str(m_r) + str(m_c) not in visited:
                # 해당 위치가 0이 아니고 상어의 크기보다 작다면
                if 0 < graph[m_r][m_c] < shark_size:
                    # 이번 순회해서 먹을 수 있는 물고기가 있다는 것을 표시
                    isAte = True
                    # 먹을 수 있는 물고기 중 가장 가까운 물고기
                    if time + 1 < to_fish_time:
                        to_fish_time = time + 1
                        fish_pos = (m_r, m_c)
                    # 거리가 같을 때 가장 위쪽에 있는 물고기
                    elif time + 1 == to_fish_time:
                        if m_r < fish_pos[0]:
                            to_fish_time = time + 1
                            fish_pos = (m_r, m_c)
                        # 가자 위쪽의 물고기 중 가장 왼쪽에 있는 물고기
                        elif m_r == fish_pos[0]:
                            if m_c < fish_pos[1]:
                                to_fish_time = time + 1
                                fish_pos = (m_r, m_c)
                # 해당 위치가 상어의 크기와 같고 0일 때 위치 이동
                elif graph[m_r][m_c] == shark_size or graph[m_r][m_c] == 0:
                    visited.add(str(m_r) + str(m_c))
                    queue.append((m_r, m_c, time+1))
    if isAte:
        shark_pos = fish_pos
        graph[shark_pos[0]][shark_pos[1]] = 0
        total_time += to_fish_time
        shark_ate += 1
        if shark_size == shark_ate:
            shark_size += 1
            shark_ate = 0
    else:
        break

print(total_time)