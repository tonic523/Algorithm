import sys

input = sys.stdin.readline

N = int(input())
a,b,c = map(int, input().rstrip().split())
max_graph = [a,b,c]
min_graph = [a,b,c]
for _ in range(1, N):
    now_g = list(map(int, input().rstrip().split()))
    pre_max_g = list(max_graph)
    pre_min_g = list(min_graph)
    for j in range(3):
        max_temp = pre_max_g[j]
        min_temp = pre_min_g[j]
        if j == 0:
            max_temp = max(max_temp, pre_max_g[1])
            min_temp = min(min_temp, pre_min_g[1])
        elif j == 1:
            max_temp = max(pre_max_g)
            min_temp = min(pre_min_g)
        else:
            max_temp = max(max_temp, pre_max_g[1])
            min_temp = min(min_temp, pre_min_g[1])
        max_graph[j] = max_temp + now_g[j]
        min_graph[j] = min_temp + now_g[j]
print(max(max_graph), min(min_graph))