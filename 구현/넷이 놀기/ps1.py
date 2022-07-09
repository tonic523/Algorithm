import sys

input = sys.stdin.readline

def check(li, list):
    for i in list:
        # f = [a,0]
        s = str.format("{} {}", x + i[0], y + i[1])
        if s not in li:
            return False
    return True

N = int(input())
A, B = map(int, input().rstrip().split())
li = set()

result = 0

finds = [
    [[A,0], [0,B], [A,B]],
    [[-A,0], [0,B], [-A,B]],
    [[A,0], [0,-B], [A,-B]],
    [[-A,0], [0,-B], [-A,-B]]
]

for i in range(N):
    li.add(input().rstrip())

while len(li) != 0:
    now = li.pop().split()
    x, y = map(int, now)
    for find in finds:
        # find = [[A,0], [0,B], [A,B]]
        if check(li, find):
            result += 1
print(result)
