import sys

N,M,B = map(int, sys.stdin.readline().rstrip().split())

lands = []
for _ in range(N):
    lands += list(map(int, sys.stdin.readline().rstrip().split()))
result = [-1, 0]

for h in range(max(lands) + 1): # 256
    bag = B
    time = 0
    for land in lands: # 25000
        if land < h:
            bag -= h - land
            time += h - land
        elif land > h:
            bag += land - h
            time += 2 * (land - h)
    if bag >= 0:
        if result[0] == -1:
            result = [time, h]
        else:
            if time <= result[0]:
                result = [time, h]

print(0 if result[0] == -1 else result[0], result[1])