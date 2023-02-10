'''
N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라

[제약 사항]
N은 3 이상 7 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
다음 N 줄에는 N x N 행렬이 주어진다.

[출력]
출력의 첫 줄은 '#t'로 시작하고,
다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
입력과  달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
# 목저지 기준으로 원본의 어떤 좌표의 값이 저장되는지 확인

# 목적지 기준 i,j 범위를 기준으로 정리
from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_90 = [[0] * N for _ in range(N)]
    arr_180 = [[0] * N for _ in range(N)]
    arr_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N - 1 - j][i]
            arr_180[i][j] = arr[N - 1 - i][N - 1 - j]
            arr_270[i][j] = arr[j][N - 1 - i]
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_270[i][j], end='')
        print()


# T = int(input())
#
# for tc in range(1, T + 1):
#     n = int(input())
#     arr = [input().split() for _ in range(n)]
#     # arr_t = list(map(list, zip(*arr)))
#     arr1 = [[0] * n for _ in range(n)]  # 90도
#     arr2 = [[0] * n for _ in range(n)]  # 180도
#     arr3 = [[0] * n for _ in range(n)]  # 270도
#
#     # 회적각도에 따른 위치값을 저장
#     for i in range(n):
#         for j in range(n):
#             arr1[i][j] = arr[n - 1 - j][i]
#             arr2[i][j] = arr[n - 1 - i][n - 1 - j]
#             arr3[i][j] = arr[j][n - 1 - i]
#
#     # 전치배열과 읽는 방향에 따른 처리
#     # for i in range(n):
#     #     print(f'{"".join(arr_t[i][::-1])} {"".join(arr[n - 1 - i][::-1])} {"".join(arr_t[n - 1 - i])}')
#
#     print(f'#{tc} ')
#     for a, b, c in zip(arr1, arr2, arr3):
#         print(f'{"".join(a)} {"".join(b)} {"".join(c)}')