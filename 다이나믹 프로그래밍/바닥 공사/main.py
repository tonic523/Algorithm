N = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 3
for n in range(3, N+1):
    d[n] = d[n-1] + d[n-2] * 2

print(d[N])