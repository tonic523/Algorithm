import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

li = list(set(input().rstrip().split()))
li.sort(key = int)
visited_set = set()

def dfs(n, answer):
    if len(answer) == M:
        v = "".join(sorted(answer, key=int))
        if v in visited_set:
            return
        visited_set.add(v)
        print(*answer)
        return

    for i in range(n, len(li)):
        answer.append(li[i])
        dfs(i, answer)
        answer.pop()

dfs(0, [])