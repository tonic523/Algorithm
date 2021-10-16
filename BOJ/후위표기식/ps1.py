import sys

input = sys.stdin.readline

s = input().rstrip()

PRIOR = {
    "*" : 3,
    "/" : 3,
    "+" : 2,
    "-" : 2,
    "(" : 1,
}

result = ""
stack = []

for c in s:
    if c.isalpha():
        result += c
    elif c == "(":
        stack.append(c)
    elif c == ")":
        while True:
            a = stack.pop()
            if a == "(":
                break
            result += a
    else:
        while stack and PRIOR[stack[-1]] >= PRIOR[c]:
            result += stack.pop()
        stack.append(c)

while stack:
    result += stack.pop()
print(result)