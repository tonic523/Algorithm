# [구간 합 구하기 5](https://www.acmicpc.net/problem/11660)

## 풀이1
- 성공

> 그래프를 합으로 저장

그래프를 이전까지의 합들로 저장해 주면 됩니다.\
1. graph[i][j] += graph[i][j-1]
2. graph[i][j] += graph[i-1][j]

순회하면서 위 과정을 반복하여 그래프를 합으로 연관시킵니다.\
이 때 x1, y1, x2, y2가 들어왔을 때 답은
- graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1]
- graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1]