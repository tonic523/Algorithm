import sys

input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))

def isEqual(r_s, c_s, v, length):
    for r in range(length):
        for c in range(length):
            if graph[r_s+r][c_s+c] != v:
                return False
    return True

def quard_tree(r_s, c_s, length):
    v = graph[r_s][c_s]
    if isEqual(r_s, c_s, v, length):
        return v
    else:
        n_length = length // 2
        temp = []
        temp.append(quard_tree(r_s, c_s, n_length))
        temp.append(quard_tree(r_s , c_s + n_length, n_length))
        temp.append(quard_tree(r_s + n_length, c_s, n_length))
        temp.append(quard_tree(r_s + n_length, c_s + n_length, n_length))
        return "(" + "".join(temp) + ")"

print(quard_tree(0,0,N))