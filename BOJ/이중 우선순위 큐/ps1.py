import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    # 최대 힙, 최소 힙
    max_heap = []
    min_heap = []
    # 입력 값 주소 저장 리스트
    data = [0] * 1000000
    for j in range(int(input())):
        command, num = input().split()
        num = int(num)
        # 입력할 때 최대 힙, 최소 힙에 추가 (값, 입력한 순서 인덱스 값)
        if command == "I":
            heapq.heappush(min_heap, (num, j))
            heapq.heappush(max_heap, (-num, j))
            data[j] = 1
        elif command == "D":
            # 최소값이면 최소 힙에서 pop, 인덱스 리스트에 1을 0으로 초기화
            if num == -1:
                if min_heap:
                    data[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
            # 최대값이면 최대 힙에서 pop, 인덱스 리스트에 1을 0으로 초기화
            else:
                if max_heap:
                    data[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
            # 인덱스 리스트를 기준으로 최대 힙과 최소 힙 동기화 과정
            while min_heap and data[min_heap[0][1]] == 0:
                heapq.heappop(min_heap)

            while max_heap and data[max_heap[0][1]] == 0:
                heapq.heappop(max_heap)
    # 최대값, 최소값 출력, 리스트가 없다면 empty 반환
    if min_heap and max_heap:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
    else:
        print("EMPTY")