'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

입력
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

출력
#1 1
#2 1
#3 0
'''


# N = 8
# mazeArray = [[0, 0, 1, 1, 1, 1, 1, 1],
#              [1, 0, 0, 0, 0, 0, 0, 1],
#              [1, 1, 1, 1, 1, 1, 1, 1],
#              [1, 1, 1, 0, 1, 1, 1, 1],
#              [1, 0, 0, 0, 0, 0, 0, 1],
#              [1, 0, 1, 1, 1, 1, 1, 1],
#              [1, 0, 0, 0, 0, 0, 0, 0],
#              [1, 1, 1, 1, 1, 1, 1, 0]]
#
#             [1, 1, 0, 0, 0, 0, 0, 0]
#             [0, 1, 1, 1, 1, 1, 1, 0]
#             [0, 0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 0, 0, 0]
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# # visited : 방문 체크 배열
# visited = [[False] * N for _ in range(N)]
# # stack... <- 재귀호출로 최대한 처리 (시스템스택)
# # 현재 내가 가고 있는 방향, (x, y)
#
#
#
# def dfs(visited, x, y):
#     # (x, y) 좌표가 끝에 도달했을 때 탐색 성공! (기저조건)
#     if x == N - 1 and y == N - 1:
#         return True
#     # 내가 현재 있는 위치에 방문 체크
#     visited[x][y] = True
#     result = False
#     # 사방탐색을 해서 갈 수 있는 위치가 생기면
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 갈 수 있는 위치인지 체크 (갈 수 없는 위치에 있다면 탐색 다시 진행)
#         if nx < 0 or ny < 0 or nx >= N or ny >= N or mazeArray[nx][ny] == 1 or visited[nx][ny] == True:
#             continue
#
#         # 그 위치로 dfs함수를 재귀호출
#         result |= dfs(visited, nx, ny)
#
#
#     return result
#
#
# result = dfs(visited, 0, 0)
# print(result)


def check(x, y):
    miro[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if miro[nx][ny] == '0':
                check(nx, ny)
            elif miro[nx][ny] == '3':
                global ans
                ans = 1
                return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    miro = [list(input()) for i in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    ans = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                sx = i
                sy = j

    ans = 0
    check(sx, sy)
    print(f'#{tc} {ans}')
