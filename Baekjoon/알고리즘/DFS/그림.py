'''
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다.
그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

예제 입력 1
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
예제 출력 1
4
9
'''
import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
art = 0

width_list = []
mr = [0, 0, 1, -1]
mc = [1, -1, 0, 0]

def DFS(x, y):
    global width
    visited[x][y] = 1
    width += 1

    for k in range(4):
        nr = mr[k] + x
        nc = mc[k] + y
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and graph[nr][nc] == 1:
            DFS(nr, nc)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            width = 0
            DFS(i, j)
            width_list.append(width)
            art += 1


if len(width_list) == 0:
    print(art)
    print(0)
else:
    print(art)
    print(max(width_list))

