import sys

input = sys.stdin.readline

N = int(input())
graph = {}
for _ in range(N):
    v, l, r = input().rstrip().split()
    graph[v] = [l, r]

def order_traverse(parent_node, pos):
    answer = ["","",""]
    answer[pos] = parent_node
    l_v, r_v = graph[parent_node]
    if pos == 0:
        l_pos, r_pos = (1, 2)
    elif pos == 1:
        l_pos, r_pos = (0, 2)
    else:
        l_pos, r_pos = (0, 1)
    if l_v != ".":
        answer[l_pos] = order_traverse(l_v, pos)
    if r_v != ".":
        answer[r_pos] = order_traverse(r_v, pos)
    return "".join(answer)

for i in range(3):
    print(order_traverse("A", i))