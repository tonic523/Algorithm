import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
# 트리
tree = [[] for _ in range(N+1)]

# 부모 노드 저장
parents = [0] * (N + 1)
parents[1] = 1

# 트리 구조 입력
for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

# 1부터 BFS로 리스트 초기화
queue = deque([1])
visited = [False] * (N+1)
visited[1] = True
while queue:
    now = queue.popleft()
    for i in tree[now]:
        if not visited[i]:
            parents[i] = now
            queue.append(i)
            visited[i] = True

# 출력
print("\n".join(map(str, parents[2:])))