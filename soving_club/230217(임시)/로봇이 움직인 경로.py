'''
로봇이 새로운 행성을 탐사 중이다.
탐색 구역을 NxN 개의 격자 형태로 나누고, 지형을 미리 조사해 각 구역에서 로봇이 움직일 수 있는 방향을 정해 두었다.
로봇의 이동 방향은 숫자로 표시하며, 표시된 방향으로만 다른 구역으로 이동할 수 있다. 다음은 숫자가 의미하는 이동 방향이다.
0	1	2	3
→	↓	←	↑
로봇은 항상 NxN 구역의 왼쪽 맨 윗 칸에서 출발하며, 가능한 방향으로 이동하게 된다.
다음은 N=3인 구역의 예로, 로봇은 화살표 방향으로 움직이게 된다.

[제약사항]
- 로봇은 NxN 구역을 벗어날 수 없다.
- 로봇이 구역의 모든 칸을 지나야 하는 것은 아니다.
- 로봇은 지나간 구역은 다시 지나지 않는다. 위의 예에서 로봇은 노란색 칸에서 방향 전환 후 멈추게 된다.
로봇의 최초 이동부터 멈출 때까지 이동 방향을 표시하면 0 1 1 0 3 3 2가 된다.
로봇은 !@$#@$%@%$@%@$%@#%$!#$@^$@^#@%#@%@#$%^...

[입력]
첫 줄에 구역의 개수 T가 주어진다. (3<=T<=10)
다음 줄부터 각 구역 별로 첫 줄에 구역의 크기 N, 다음 줄 부터 N줄에 걸쳐 N개씩, 이동 방향 di가 빈칸으로 구분되어 주어진다. ( 3<=N<=100, 0<=di<=3)

[출력]
#과 1번부터인 구역 번호, 빈칸에 이어 빈칸으로 구분된 "방향"을 출력한다.
입력
3
3
0 1 2
2 1 3
3 0 3

출력
#1 0 1 1 0 3 3 2
'''
#
# T = int(input())
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# # 로봇은 0: 오른쪽 / 1: 밑 / 2: 왼쪽 / 3: 위족
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# # 방문위치 / 결과 리스트
# visited = [[False] * N for _ in range(N)]
# result = []
#
# # 범위를 설정
# # 출발지점
# si, sj = 0, 0
# visited[si][sj] = True
# result.append(arr[si][sj])
#
# # 인덱스 값이 arr[i][j]의 값으로 나타나 있다.
# # while True를 작성해 주고 / -> break문으로 종료조건을 만들어준다.
# while True:
#     ci, cj = si + di[arr[si][sj]], sj + dj[arr[si][sj]]
#     if visited[ci][cj] == True or ci < 0 or cj < 0 or ci >= N or cj >= N:
#         break
#     visited[ci][cj] = True
#     result.append(arr[ci][cj])
#     # 시작 위치 갱신
#     si, sj = ci, cj
#
# print('#1', end=' ')
# print(*result)


# T = int(input())
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# mr = [0, 1, 0, -1]
# mc = [1, 0, -1, 0]
# visited = [[False] * N for _ in range(N)]
# way = []
# sr, sc = 0, 0
# visited[sr][sc] = True
# way.append(arr[sr][sc])
# while True:
#     nr, nc = sr + mr[arr[sr][sc]], sc + mc[arr[sr][sc]]
#     if visited[nr][nc] == True or nr < 0 or nc < 0 or nr >= N or nc >= N:
#         break
#     visited[nr][nc] = True
#     way.append(arr[nr][nc])
#     sr, sc = nr, nc
# print(way)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    way = []
    mr = [0, 1, 0, -1]
    mc = [1, 0, -1, 0]
    sr, sc = 0, 0
    visited[sr][sc] = True
    way.append(arr[sr][sc])
    while True:
        nr, nc = sr + mr[arr[sr][sc]], sc + mc[arr[sr][sc]]
        if visited[nr][nc] == True or nr < 0 or nc < 0 or nr >= N or nc >= N:
            break
        visited[nr][nc] = True
        way.append(arr[nr][nc])
        sr, sc = nr, nc
    print(f'#{tc}', *way)
