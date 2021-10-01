import sys

input = sys.stdin.readline

N = input().rstrip()
M = int(input())
numbers = []
li = []
if M:
    li = list(map(int, input().rstrip().split()))
for i in range(10):
    if i not in li:
        numbers.append(i)

ma = max(numbers)
mi = min(numbers)

numbers = set(numbers)
answer = []
if int(N) == 100:
    print(0)
else:
    for i in range(len(N)):
        now = int(N[i])
        ten_n = len(N) - i - 1
        if now in numbers:
            continue
        else:
            j = 1
            while now + j < 10:
                if now + j in numbers:
                    answer.append(int(str(now + j) + (str(mi) * ten_n)) - int(N[i:]))
                    break
                j += 1
            j = 1
            while now - j <= 10:
                if now - j in numbers:
                    answer.append(int(N[i:]) - int(str(now - j) + (str(ma) * ten_n)))
                    break
                j -= 1
    answer.append((int(N) - 100 if int(N) > 100 else 100 - int(N)) - len(N))
    print(min(answer) + len(N))