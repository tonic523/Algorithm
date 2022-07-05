import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
list = [n for n in range(1, N + 1)]
results = []

before = 0

while (len(list) != 0):
    now = (before + (K-1)) % len(list)
    results.append(list.pop(now))
    before = now
result = ', '.join(map(str, results)).replace("[", "<").replace("]", ">")
print(f"<{result}>")
