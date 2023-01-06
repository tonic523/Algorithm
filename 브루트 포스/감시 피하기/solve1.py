import sys

'''
25P3 = 13800
25C3 = 2300

장애물을 놓을 수 있는 최대 경우의 수: 36 * 36 * 36 = 46656
감시를 피할 수 있는지 알 수 있는 경우의 수: 5 * 10 
'''

input = sys.stdin.readline
N = int(input())

# 그래프 및 선생님 위치 조회
graph = []
teachers = []
emptys = []
for i in range(N):
    line = list(input().rstrip().split())
    for j in range(len(line)):
        if line[j] == 'T':
            teachers.append((i,j))
        if line[j] == 'X':
            emptys.append((i, j))
    graph.append(line)

# 장애물이 필요한 위치에 설치하면서 감시를 피할 수 있는지
answer = False
move = (
    (1, 0), (-1, 0), (0, 1), (0, -1)
)


def is_avoidable():
    for teacher in teachers:
        for m in move:
            t_r = teacher[0]
            t_c = teacher[1]
            while True:
                t_r += m[0]
                t_c += m[1]
                if not (0<=t_r<N and 0<=t_c<N):
                    break
                if graph[t_r][t_c] in ('O', 'T'):
                    break
                if graph[t_r][t_c] == 'X':
                    continue
                elif graph[t_r][t_c] == 'S':
                    return False
    return True


def obtacles_case():
    for i in range(len(emptys)):
        graph[emptys[i][0]][emptys[i][1]] = 'O'
        for j in range(i+1, len(emptys)):
            graph[emptys[j][0]][emptys[j][1]] = 'O'
            for k in range(j+1, len(emptys)):
                graph[emptys[k][0]][emptys[k][1]] = 'O'
                if is_avoidable():
                    return "YES"
                graph[emptys[k][0]][emptys[k][1]] = 'X'
            graph[emptys[j][0]][emptys[j][1]] = 'X'
        graph[emptys[i][0]][emptys[i][1]] = 'X'
    return "NO"


print(obtacles_case())
