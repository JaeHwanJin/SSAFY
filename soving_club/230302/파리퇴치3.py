'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수를 의미한다.
아래는 N=5 의 예이다.
파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다. 스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다. 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
다음은 M=3 세기로 스프레이르 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다. 뿌려진 일부가 영역을 벗어나도 상관없다.
한 번에 잡을 수 있는 최대 파리수를 출력하라.

[제약 사항]
1. N 은 5 이상 15 이하이다.
2. M은 2 이상 N 이하이다.
3. 각 영역의 파리 갯수는 30 이하 이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
다음 N 줄에 걸쳐 N x N 배열이 주어진다.

입력
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29

출력
#1 64
#2 157
'''
# 리스트에 추가해서 가장 큰 값 찾기
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     spray = [list(map(int, input().split())) for _ in range(N)]
#     mr = [0, 0, 1, -1]    # + 방향 탐색
#     mc = [1, -1, 0, 0]
#     cnt_arr = []  델타검색 할 때마다 퇴치한 파리수를 담을 list
#     xcnt_arr = []
#     xmr = [1, 1, -1, -1]  # X 방향 탐색
#     xmc = [-1, 1, -1, 1]
#     for i in range(len(spray)):
#         for j in range(len(spray)):
#             cnt = 0
#             xcnt = 0
#             for k in range(1, M):
#                 for l in range(4):
#                     nr = i + mr[l] * k    # 델타검색 후 1칸씩 범위 늘리기
#                     nc = j + mc[l] * k
#                     xnr = i + xmr[l] * k
#                     xnc = j + xmc[l] * k
#                     if 0 <= nr < N and 0 <= nc < N:
#                         # print(spray[nr][nc])
#                         cnt += spray[nr][nc]
#                     if 0 <= xnr < N and 0 <= xnc < N:
#                         # print(spray[xnr][xnc])
#                         xcnt += spray[xnr][xnc]
#             cnt += spray[i][j]
#             cnt_arr.append(cnt)
#             xcnt += spray[i][j]
#             xcnt_arr.append(xcnt)
#     if max(cnt_arr) > max(xcnt_arr):
#         print(f'#{tc} {max(cnt_arr)}')
#     else:
#         print(f'#{tc} {max(xcnt_arr)}')
#     # print('cnt',max(cnt_arr))
#     # print('xcnt',max(xcnt_arr))

# 최대값 갱신 해서 풀기
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     spray = [list(map(int, input().split())) for _ in range(N)]
#     mr = [0, 0, 1, -1] # + 방향 탐색
#     mc = [1, -1, 0, 0]
#     xmr = [1, 1, -1, -1]  # X 방향 탐색
#     xmc = [-1, 1, -1, 1]
#     max_cnt, max_xcnt = 0, 0  # 최대값 저장 할 변수
#     for i in range(len(spray)):
#         for j in range(len(spray)):
#             cnt = 0
#             xcnt = 0
#             for k in range(1, M):
#                 for l in range(4):
#                     nr = i + mr[l] * k    # 델타검색 후 1칸씩 범위 늘리기
#                     nc = j + mc[l] * k
#                     xnr = i + xmr[l] * k
#                     xnc = j + xmc[l] * k
#                     if 0 <= nr < N and 0 <= nc < N:
#                         cnt += spray[nr][nc]
#                     if 0 <= xnr < N and 0 <= xnc < N:
#                         xcnt += spray[xnr][xnc]
#             cnt += spray[i][j]
#             xcnt += spray[i][j]
#             # if max_cnt < cnt:
#             #     max_cnt = cnt
#             # if max_xcnt < xcnt:
#             #     max_xcnt = xcnt
#             max_cnt = max(max_cnt, cnt)
#             max_xcnt = max(max_xcnt, xcnt)
#
#     if max_xcnt > max_cnt:
#         print(f'#{tc} {max_xcnt}')
#     else:
#         print(f'#{tc} {max_cnt}')

# T = int(input())
# for tc in range(1, T + 1):
#     # N은 2차원 배열 크기 M은 스프레이의 세기
#     N, M = map(int, input().split())
#     fly = [list(map(int, input().split())) for _ in range(N)]
#     mr = [0, 0, 1, -1]
#     mc = [1, -1, 0, 0]
#     for i in range(N):
#         for j in range(N):
#             for l in range(M):
#                 p = 1
#                 for k in range(4):
#                     nr = i + mr[k] * p
#                     nc = j + mc[k] * p


