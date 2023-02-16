'''
땅속의 구조물을 촬영할 수 있는 특수 위성 카메라에 땅속에 묻힌 고대 구조물이 발견되었다.
구조물은 폭 1m, 길이 2m 이상의 직선 형태로 서로 평행 또는 직각으로만 자리하고 있으며,
1mx1m의 해상도의 사진데이터에 구조물이 있는 자리는 1로 나타난다.
사진의 해상도는 NxM이며, 구조물이 있는 곳은 1, 빈 땅은 0으로 표시된다. 위 그림의 경우 가장 긴 구조물은 노란색으로 표시된 영역이며, 길이는 6이다. 교차하거나 만나는 것처럼 보이는 구조물은 서로 다른 깊이에 묻힌 것이므로 직선인 구조물만 고려하면 된다.
다음과 같은 경우는 길이가 3인 구조물 4개가 겹쳐 보이는 것이다.
평행한 모든 구조물은 서로 1m이상 떨어져 있고, 구조물의 최소 크기는 1x2m이다.
여러 구역의 사진 데이터가 주어질 때, 각 구역 별로 가장 긴 구조물의 길이를 찾는 프로그램을 만드시오.
입력
첫 줄에 사진 데이터의 개수, 다음 줄부터 사진 데이터 별로 첫 줄에 N과 M, 이후 N개의 줄에 M개씩의 데이터가 제공된다.
(3<=N, M<=100)

출력
#과 1번부터 시작하는 사진 번호, 빈칸과 가장 긴 구조물의 길이를 출력한다.

입력
3
3 3
0 1 0
0 1 0
0 1 0
3 3
0 1 0
1 1 1
0 0 0
8 8
1 0 0 0 0 0 1 0
1 0 1 1 1 0 1 0
1 0 0 0 0 0 1 0
0 0 0 1 0 0 1 0
0 0 0 1 0 0 1 0
0 1 1 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1

출력
#1 3
#2 3
#3 6
'''


def check(x, y):
    # arr[x][y] = 1
    global MAX
    for i in range(4):
        cnt = 1
        dx = x + di[i]
        dy = y + dj[i]
        if 0 <= dx < N and 0 <= dy < N:
            while 0 <= dx < N and 0 <= dy < M and arr[dx][dy] == 1:
                dx += di[i]
                dy += dj[i]
                cnt += 1
            if MAX < cnt:
                MAX = cnt
    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    MAX = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                check(i, j)

    print(f'#{tc} {MAX}')


def DFS(row, col):
    global mx_cnt
    for k in range(4):
        cnt = 1
        nx = row + dx[k]
        ny = col + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            while 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                nx += dx[k]
                ny += dy[k]
                cnt += 1
            if mx_cnt < cnt:
                mx_cnt = cnt
    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx_cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                DFS(i, j)

    print(f'#{tc} {mx_cnt}')