N = int(input())

li = list(map(int, input().split()))
li.sort()
result = 0
for n in range(N):
    if n != 0:
        li[n] += li[n-1]
    result += li[n]
print(result)