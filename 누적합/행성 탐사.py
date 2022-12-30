import sys

input = sys.stdin.readline

'''
N, M 그래프
J, O, I

K개 영역 내부에 J, O, I가 각각 몇개있는지
'''

M, N = map(int, input().rstrip().split())
K = int(input())

j_graph = [[0] * (N+1) for _ in range(M+1)]
o_graph = [[0] * (N+1) for _ in range(M+1)]
i_graph = [[0] * (N+1) for _ in range(M+1)]

for a in range(1, M+1):
    line = "0" + input().rstrip()
    for b in range(1, len(line)):
        j_graph[a][b] += j_graph[a-1][b] + j_graph[a][b-1] - j_graph[a-1][b-1]
        o_graph[a][b] += o_graph[a-1][b] + o_graph[a][b-1] - o_graph[a-1][b-1]
        i_graph[a][b] += i_graph[a-1][b] + i_graph[a][b-1] - i_graph[a-1][b-1]
        if line[b] == 'J':
            j_graph[a][b] += 1
        elif line[b] == 'O':
            o_graph[a][b] += 1
        elif line[b] == 'I':
            i_graph[a][b] += 1

results = ""
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().rstrip().split())
    result = ""
    result += str(j_graph[y2][x2] - j_graph[y1-1][x2] - j_graph[y2][x1-1] + j_graph[y1-1][x1-1])
    result += " " + str(o_graph[y2][x2] - o_graph[y1-1][x2] - o_graph[y2][x1-1] + o_graph[y1-1][x1-1])
    result += " " + str(i_graph[y2][x2] - i_graph[y1-1][x2] - i_graph[y2][x1-1] + i_graph[y1-1][x1-1])
    results.append(result)

print("\n".join(results))
