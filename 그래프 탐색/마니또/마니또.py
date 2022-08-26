import sys

input = sys.stdin.readline


def isChain(k):
    global visited
    visited.append(k)
    v = manitto[k]
    if v not in manitto.keys():
        return False
    if v in manitto.keys():
        if v in visited:
            return True
        return isChain(v)


testcase_num = 0
while True:
    N = int(input())
    if N == 0:
        break
    testcase_num += 1

    chain_count = 0
    manitto = {}
    for _ in range(N):
        key, value = input().rstrip().split()
        manitto[key] = value
    visited = []
    for k in manitto.keys():
        if k in visited:
            continue
        if isChain(k):
            chain_count += 1

    print(testcase_num, chain_count)
