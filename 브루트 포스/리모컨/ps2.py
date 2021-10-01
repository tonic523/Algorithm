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
numbers = set(numbers)
answer = abs(int(N) - 100)

def is_in_numbers(n, numbers):
    for j in n:
        if int(j) not in numbers:
            return False
    return True

for i in range(1000000):
    i = str(i)
    if is_in_numbers(i, numbers):
        count = abs(int(i) - int(N)) + len(i)
        answer = answer if answer < count else count

print(answer)