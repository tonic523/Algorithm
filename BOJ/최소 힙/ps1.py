import sys
import heapq
input = sys.stdin.readline

def sol18870():
    arr = []
    answer = []
    for _ in range(int(input())):
        x = int(input())
        if x == 0:
            if arr:
                answer.append(str(heapq.heappop(arr)))
            else:
                answer.append('0')
        elif 0 < x:
            heapq.heappush(arr, x)

    print("\n".join(answer))

if __name__ == "__main__":
    sol18870()