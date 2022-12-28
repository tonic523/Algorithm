import sys

input = sys.stdin.readline

"""
누적합을 활용하여 푸는 문제
단, 누적합을 구간별로 해주어야 한다.
예) 1~3을 통행한다 -> 1->2, 2->3 구간을 1씩 더해준다.
구간이 5까지 있다면?
- 4 구간에 -1을 추가해준다.
예) 1~3을 통행한다.(1~5까지 구간이 있을 때) -> 1->2, 2->3 : +1 | 3->4, 4->5 : -1
"""

N, M = map(int, input().rstrip().split())
travel = list(map(int, input().rstrip().split()))
cost = [0]

for _ in range(N - 1):
    ticket, card_cost, card = map(int, input().rstrip().split())
    cost.append([ticket, card_cost, card])

front = [0] * (N + 1)
back = [0] * (N + 1)

departure = 0
arrival = 0

for i in range(len(travel)):
    if departure == 0:
        departure = travel[i]
        continue

    arrival = travel[i]
    if arrival > departure:
        front[departure] += 1
        front[arrival] += -1
    elif arrival < departure:
        back[departure - 1] += 1
        back[arrival - 1] += -1
    departure = arrival

for i in range(N):
    front[i + 1] += front[i]
    back[N - i - 1] += back[N - i]

total_cost = 0
for i in range(1, N):
    count = front[i] + back[i]
    ticket_cost = cost[i][0] * count
    card_cost = cost[i][1] * count + cost[i][2]
    total_cost += min(ticket_cost, card_cost)

print(total_cost)
