from collections import deque

T = int(input())
results = []
for _ in range(T):
    N, M = list(map(int, input().split()))
    queue = deque(list(map(int, input().split())))
    order = 1
    while len(queue) > 0:
        max_important = max(queue)
        important = queue.popleft()
        if important == max_important:
            if M == 0:
                results.append(str(order))
                break
            else:
                order += 1
                M -= 1
        else:
            queue.append(important)
            M = (len(queue) - 1) if (M == 0) else (M - 1)
print("\n".join(results))