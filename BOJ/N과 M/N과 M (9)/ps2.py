import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
numbers.sort()
sequence, visited = [], [False] * len(numbers)

# dfs 순회
def dfs(count):
    if count == M:
        print(*map(int, sequence))
        return

    t = -1
    for i in range(len(numbers)):
        # 백 트래킹을 위한 조건(순열에 포함된 수, 중복된 수)
        if visited[i] or numbers[i] == t:
            continue

        sequence.append(numbers[i])  # 순열 추가
        visited[i] = True  # 방문처리
        dfs(count + 1)
        visited[i] = False  # 방문처리 초기화
        t = sequence.pop()  # 추가됐던 노드 저장


dfs(0)