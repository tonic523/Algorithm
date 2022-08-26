import sys
from collections import deque
input = sys.stdin.readline

def sol7576():
    # 그래프 길이 입력
    C, R = map(int, input().split())
    graph = []
    # 그래프 초기화
    for _ in range(R):
        graph.append(list(map(int, input().split())))
    queue = deque()
    # 모든 토마토가 익는 시간
    time = 0
    # 4방향
    move = (
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    )
    # 처음 1인 토마토 위치 저장
    for r in range(R):
        for c in range(C):
            if graph[r][c] == 1:
                queue.append((r,c))
    # 큐가 있을 때까지
    while queue:
        r, c = queue.popleft()
        # 큐를 순회할 때마다 최대 걸리는 시간 갱신
        time = time if time > graph[r][c] else graph[r][c]
        # 큐에 저장된 위치의 4방향 중 0인 값 검사
        for m in move:
            m_r = r + m[0]
            m_c = c + m[1]
            if 0 <= m_r < R and 0 <= m_c < C:
                # 0 이라면 현재 순회중인 위치의 값+1 저장
                if graph[m_r][m_c] == 0:
                    graph[m_r][m_c] = graph[r][c]+1
                    queue.append((m_r, m_c))
    # 모든 토마토가 익었는지 검사
    for r in range(R):
        for c in range(C):
            # 하나라도 안익었다면 -1 출력
            if graph[r][c] == 0:
                print(-1)
                return
    # 다 익었다면 최대 걸리는 시간 - 1 출력
    print(time - 1)

if __name__ == "__main__":
    sol7576()