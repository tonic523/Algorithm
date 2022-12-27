import sys

# 1. top, down 배열로 분리해서 입력
# 2. top, down을 거꾸로 순회하며 누적합 계산
# 3. H(i) 만큼 순회하면서 top[i] + down[H-i]의 최솟값 계산
#   - 최솟값과 같을 경우 count += 1
#   - 최솟값보다 작을 경우 최솟값 갱신 and count=1로 갱신

input = sys.stdin.readline

N, H = map(int, input().rstrip().split())

top = [0] * (H+1)
down = [0] * (H+1)

# top과 down 리스트에 높이 위치에 1씩 더해준다.
# 이 때 top은 (총 높이 - 입력값 + 1)로 위치를 설정한다.
for i in range(N):
    h = int(input())
    if i % 2:
        top[H+1-h] += 1
    else:
        down[h] += 1

# top은 순서대로 누적합을 구한다.
# down은 역순으로 누적합을 구한다.
for i in range(1, H):
    top[i+1] += top[i]
    down[H-i] += down[H+1-i]

# 1~H까지 순회하면서 장애물을 구한다. (top[i] + down[i])
# 장애물이 최솟값보다 작으면 최솟값 갱신, count 갱신
# 장애물이 최솟값과 같으면 count += 1
min_obstacle = N
count = 0
for i in range(1, H+1):
    obstacle = top[i] + down[i]
    if min_obstacle > obstacle:
        min_obstacle = obstacle
        count = 1
    elif min_obstacle == obstacle:
        count += 1

print(min_obstacle, count)
