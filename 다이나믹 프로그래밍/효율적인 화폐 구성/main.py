import sys

N, M = map(int, input().split())
money_type = []
for _ in range(N):
    money_type.append(int(sys.stdin.readline().rstrip()))

d = [-1] * M+1
d[0] = 0
for m in range(1, M+1):
    temp_arr = []
    for mt in money_type:
        if m-mt < 0:
            continue
        elif d[m-mt] == -1:
            continue
        else:
            temp_arr.append(d[m-mt]+1)
    if temp_arr:
        d[m] = min(temp_arr)
    else:
        d[m] = -1
print(d[M])