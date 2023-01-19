import sys

'''
- 부모 노드 부터 깊이 우선 탐색한다.
- 노드의 자식 노드가 없다면 리프 노드로 판단한다.
- 자식 노드 중 삭제될 노드가 있을 땐
  - 삭제될 노드가 유일하다면 리프 노드로 판단한다.
  - 삭제될 노드는 탐색하지 않는다.
'''

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
parent_nodes = list(map(int, input().rstrip().split()))
remove_node = int(input())
root_node = 0

for node in range(len(parent_nodes)):
    parent_node = parent_nodes[node]
    if parent_node == -1:
        root_node = node
    else:
        tree[parent_node].append(node)

leaf_node_count = 0


def dfs(node):
    global leaf_node_count

    if node == remove_node:
        return
    elif not tree[node]:
        leaf_node_count += 1
    else:
        if remove_node in tree[node] and len(tree[node]) == 1:
            leaf_node_count += 1
        else:
            for n in tree[node]:
                dfs(n)


dfs(root_node)
print(leaf_node_count)
