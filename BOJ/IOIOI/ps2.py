import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()
cnt = 0
p_n = 2 * N + 1
temp = []
start = False
io = ""
result = 0

for s in S:
    if start:
        if s == io:
            cnt += 1
            io = "I" if io == "O" else "O"
        else:
            if s == "I":
                start = True
                io = "O"
                temp.append(cnt)
                cnt = 1
            else:
                start = False
                temp.append(cnt - 1)
                cnt = 0

    elif s == "I":
        start = True
        io = "O"
        cnt += 1

if io == "O":
    temp.append(cnt)
else:
    temp.append(cnt - 1)

for t in temp:
    if t >= p_n:
        result += (t - p_n) // 2 + 1

print(result)