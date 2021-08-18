import sys

N = int(sys.stdin.readline().rstrip())
n = 666
while N:
    s = str(n)
    if '666' in s:
        N -= 1
    n += 1
print(s, end="")