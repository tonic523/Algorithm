import sys
from collections import deque

input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    command = input().rstrip()
    N = int(input())
    in_arr = input().lstrip("[").rstrip().rstrip("]")
    if N == 0:
        queue = []
    else:
        queue = deque(map(int, in_arr.split(",")))
    is_reverse = False
    is_error = False
    for c in command:
        if c == "R":
            is_reverse = not is_reverse
        elif c == "D":
            if len(queue) != 0:
                if is_reverse:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                answer.append("error")
                is_error = True
                break
    if not is_error:
        if is_reverse:
            queue.reverse()
        answer.append(list(queue))
for a in answer:
    print(str(a).replace(" ", ""))