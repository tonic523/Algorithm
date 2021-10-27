import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
cnt = 0
def convert_preorder_to_postorder(arr):
    size = len(arr)
    if size == 0:
        return []
    elif size == 1:
        return arr[:]
    root = arr[0]
    start = 1
    end = size - 1
    mid = start + end // 2
    while start < end:
        if arr[mid] < root:
            start = mid+1
        elif arr[mid] > root:
            end = mid
        mid = (start + end) // 2
    if arr[mid] < root:
        return convert_preorder_to_postorder(arr[1:]) + [root]
    else:
        return convert_preorder_to_postorder(arr[1:mid]) + convert_preorder_to_postorder(arr[mid:]) + [root]

preorder = []
postorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
postorder = convert_preorder_to_postorder(preorder)
for v in postorder:
    print(v)