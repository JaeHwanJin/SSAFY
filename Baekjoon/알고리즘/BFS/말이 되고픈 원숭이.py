'''
동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그 녀석은 말(Horse)이 되기를 간절히 원했다. 그래서 그는 말의 움직임을 유심히 살펴보고 그대로 따라 하기로 하였다. 말은 말이다. 말은 격자판에서 체스의 나이트와 같은 이동방식을 가진다. 다음 그림에 말의 이동방법이 나타나있다. x표시한 곳으로 말이 갈 수 있다는 뜻이다. 참고로 말은 장애물을 뛰어넘을 수 있다.
 	x	 	x
x	 	 	 	x
 	 	말
x	 	 	 	x
 	x	 	x
근데 원숭이는 한 가지 착각하고 있는 것이 있다. 말은 저렇게 움직일 수 있지만 원숭이는 능력이 부족해서
총 K번만 위와 같이 움직일 수 있고, 그 외에는 그냥 인접한 칸으로만 움직일 수 있다. 대각선 방향은 인접한 칸에 포함되지 않는다.
이제 원숭이는 머나먼 여행길을 떠난다. 격자판의 맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다.
인접한 네 방향으로 한 번 움직이는 것, 말의 움직임으로 한 번 움직이는 것, 모두 한 번의 동작으로 친다.
격자판이 주어졌을 때, 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법을 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 정수 K가 주어진다. 둘째 줄에 격자판의 가로길이 W, 세로길이 H가 주어진다. 그 다음 H줄에 걸쳐 W개의 숫자가 주어지는데, 0은 아무것도 없는 평지, 1은 장애물을 뜻한다. 장애물이 있는 곳으로는 이동할 수 없다. 시작점과 도착점은 항상 평지이다. W와 H는 1이상 200이하의 자연수이고, K는 0이상 30이하의 정수이다.

출력
첫째 줄에 원숭이의 동작수의 최솟값을 출력한다. 시작점에서 도착점까지 갈 수 없는 경우엔 -1을 출력한다.

예제 입력 1
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
예제 출력 1
4
예제 입력 2
2
5 2
0 0 1 1 0
0 0 1 1 0
예제 출력 2
-1
'''
import sys, collections

# 입력부
k = int(sys.stdin.readline())
m, n = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dx, dy : 일반적인 동서남북 4방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# hx, hy : 특수 이동인 8방향
hx = [-1, -2, -1, -2, 1, 2, 1, 2]
hy = [-2, -1, 2, 1, -2, -1, 2, 1]

# check : 3차원 검사 배열
check = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]


# go : (a,b)에서 시작하여 특수이동, 일반이동을 모두 고려했을 때 도착점으로 가기 위한 최소 동작 횟수를 리턴하는 함수
def go(a, b):
    q = collections.deque()
    q.append((a, b, 0, 0))
    # 처음에는 특수 이동을 쓰지 않았으므로 [a][b][0]이다
    check[a][b][0] = True
    while q:
        # x, y : 현재 x좌표, y좌표
        # skill : 현재 특수 이동을 한 횟수
        # cnt : 그때의 동작 횟수
        x, y, skill, cnt = q.popleft()

        # 도착점이면 동작 횟수 리턴
        if x == n - 1 and y == m - 1:
            return cnt

        # 일반적인 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny][skill] == False:
                    if table[nx][ny] == 0:
                        check[nx][ny][skill] = True
                        # 특수 이동을 쓰지 않았으므로 skill은 증가시키지 않고 큐에 넣는다
                        q.append((nx, ny, skill, cnt + 1))

        # 특수 이동이 가능한 경우
        if skill < k:
            # 특수 이동 8방향 탐색
            for i in range(8):
                nx, ny = x + hx[i], y + hy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    # 현재 특수 이동을 하게 되면 가려는 정점은
                    # 현재 특수 이동 횟수 + 1번째에 방문하는 것이므로
                    # check[nx][ny][skill]이 아니라
                    # check[nx][ny][skill + 1]을 체크해야 한다
                    if check[nx][ny][skill + 1] == False:
                        if table[nx][ny] == 0:
                            check[nx][ny][skill + 1] = True
                            # 다음 이동을 위해 특수 이동을 한번 썼기 때문에 skill을 1증가 시키고 큐에 넣는다
                            q.append((nx, ny, skill + 1, cnt + 1))

    # 불가능한 경우 -1 리턴
    return -1


# 정답 출력
print(go(0, 0))

import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
hx, hy = [-2, -2, -1, 1, 2, 2, -1, 1], [-1, 1, -2, -2, -1, 1, 2, 2]


def bfs():
    q = deque()
    q.append((0, 0, K, 0))  # 맨 왼쪽 위에서 시작 - 인덱스, 말처럼 움직일 기회가 몇번 남았는지, 이동 횟수

    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]  # 세로 좌표, 가로 좌표, 남은 점프 횟수
    visited[0][0][K] = True
    while q:
        i, j, k, cnt = q.popleft()

        # 목적지 도착했으면
        if i == (H - 1) and j == (W - 1):
            return cnt

        # 말처럼 이동 가능하면
        if k > 0:
            for m in range(8):
                ni, nj = i + hx[m], j + hy[m]

                    # 범위 체크, 방문 체크, 목적지가 장애물이면 이동 불가능
                if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == 0 and visited[ni][nj][k - 1] == False:
                    visited[ni][nj][k - 1] = True
                    q.append((ni, nj, k - 1, cnt + 1))

        # 사방으로 이동
        for m in range(4):
            ni, nj = i + dx[m], j + dy[m]

            # 범위 체크, 방문 체크, 목적지가 장애물이면 이동 불가능
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == 0 and visited[ni][nj][k] == False:
                visited[ni][nj][k] = True
                q.append((ni, nj, k, cnt + 1))

    # 도착점 도착할 수 없으면
    return -1


K = int(input())
W, H = map(int, input().split())
arr = tuple(tuple(map(int, input().split())) for _ in range(H))
print(bfs())