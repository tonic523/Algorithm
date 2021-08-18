import sys
for t in range(int(input())):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    golds = map(int, sys.stdin.readline().rstrip().split())
    dp = [0] * M
    n = 0
    for n in range(N):
        for m in range(M):
            temp = m * M + n
            temp_list = [0]
            if 0 <= temp-1:
                temp_list.append(golds[temp-1])
            if 0 <= temp-5:
                temp_list.append(golds[temp-5])
            if 0 <= temp+3 <= N*M-1:
                temp_list.append(golds[temp+3])
