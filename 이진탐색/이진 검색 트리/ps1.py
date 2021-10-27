import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
cnt = 0
def convert_preorder_to_postorder(arr):
    if arr == []:
        return []
    elif len(arr) == 1:
        return arr[:]
    root = arr[0]
    l = []
    r = []
    for i in range(len(arr) // 2, len(arr)):
        if arr[i] > root:
            l.append(arr[i])
        else:
            r = arr[i:]
            break
    return convert_preorder_to_postorder(l) + convert_preorder_to_postorder(r) + [root]

preorder = []
postorder = []
while True:
    try:
        t = int(input())
        preorder.append(int(t))
    except:
        break
preorder = [i for i in range(10000)]
postorder = convert_preorder_to_postorder(preorder)
for v in postorder:
    print(v)