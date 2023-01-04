import sys

input = sys.stdin.readline

'''
재귀 함수와 백트래킹 기법으로 풀이
'''


def dfs(sum):
    global answer, count
    if sum == n:
        count += 1
        if count == k:
            answer = '+'.join(stack)
        return

    for i in range(1, 4): # 1 ~ 4 순회
        if sum + i <= n:
            stack.append(str(i)) # 스택에 현재 추가한 값을 넣는다.
            dfs(sum + i) # 다음 단계로 넘어간다.
            stack.pop() # 스택에 현재 추가한 값을 뺀다.


n, k = map(int, input().rstrip().split())

stack = []
answer = "-1"
count = 0
dfs(0)

print(answer)