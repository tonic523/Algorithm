import sys

input = sys.stdin.readline

N = int(input())
graph = [[int(input())]]

for i in range(1, N):
    nums = list(map(int, input().rstrip().split()))
    graph.append(nums)

for i in range(1, len(graph)):
    for j in range(len(graph[i])):
        temp = []
        if 0 <= j-1:
            temp.append(graph[i-1][j-1])
        if j < len(graph[i]) - 1:
            temp.append(graph[i-1][j])
        graph[i][j] += max(temp)

print(max(graph[-1]))