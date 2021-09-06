import sys
import heapq

input = sys.stdin.readline

heap = []
def sol11279():
    for _ in range(int(input())):
        n = int(input())
        if n > 0:
            heapq.heappush(heap, (-n, n))
        elif n == 0:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)

if __name__ == "__main__":
	sol11279()