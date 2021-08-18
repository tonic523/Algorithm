import sys

def calculate_paint_count(row, column):
    white_black = ['W', 'B', 0]
    black_white = ['B', 'W', 0]
    for r in range(row, row+8):
        for c in range(column, column+8):
            if board[r][c] != white_black[(r+c) % 2]:
                white_black[2] += 1
                continue
            if board[r][c] != black_white[(r+c) % 2]:
                black_white[2] += 1
    return min(white_black[2], black_white[2])

N, M = map(int, input().split())
board = []
result = 2000
for idx, _ in enumerate(range(N)):
    board.append(sys.stdin.readline().rstrip())

for row in range(N):
    if row + 8 > N:
        break
    for column in range(M):
        if column + 8 > M:
            break
        temp_result = calculate_paint_count(row,column)
        result = result if result < temp_result else temp_result
print(result)