'''
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1
5
28
0
'''
from collections import deque


def BFS(a, b):
    mr = [2, 2, -2, -2, 1, 1, -1, -1]
    mc = [1, -1, 1, -1, 2, -2, 2, -2]
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for k in range(8):
            nr = mr[k] + x
            nc = mc[k] + y
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = visited[x][y] + 1
                q.append((nr, nc))


T = int(input())

for tc in range(T):
    N = int(input())  # 체스판 크기
    chess = [[0] * N for _ in range(N)]  # 체스판
    visited = [[0] * N for _ in range(N)]
    x1, y1 = map(int, input().split())  # 체스말의 현재 위치
    x2, y2 = map(int, input().split())  # 체스말이 이동하려는 위치
    BFS(x1, y1)
    if x1 == x2 and y1 == y2:
        print(0)
    else:
        print(visited[x2][y2])
