import sys

input = sys.stdin.readline


def bfs(remove_node):
    if tree[remove_node] == 'r':
        return
    for t in tree[remove_node]:
        bfs(t)
    tree[remove_node] = 'r'


N = int(input())
nodes = list(map(int, input().rstrip().split()))
remove_node = int(input())
remove_node_parent = 0
tree = [[] for _ in range(N)]
# 트리 셋팅
for node_num in range(1, len(nodes)):
    parent_node = nodes[node_num]
    tree[parent_node].append(node_num)
    if node_num == remove_node:
        remove_node_parent = parent_node

bfs(remove_node)
if remove_node == 0:
    print(0)
else:
    tree[remove_node_parent].remove(remove_node)

    # 노드 지우기 전 리프 노드 개수
    leaf_count = 0
    for t in tree:
        if len(t) == 0:
            leaf_count += 1

    print(leaf_count)
print(tree)