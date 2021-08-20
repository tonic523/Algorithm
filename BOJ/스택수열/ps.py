import sys
input = sys.stdin.readline

n = int(input())
targets = []
stack = []
number = 1
command = ""

for _ in range(n):
    targets.append(int(input()))

for target in targets:
    while target >= number:
        stack.append(number)
        number += 1
        command += "+\n"
    if stack and target == stack[-1]:
        stack.pop()
        command += "-\n"
    else:
        command = "NO"
print(command)