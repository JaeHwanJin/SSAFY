'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

[예제]
N이 3일 경우,
1   2   3
8   9   4
7   6   5

N이 4일 경우,
1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7

[제약사항]
달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

[출력]
각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
2
3
4

출력
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
'''

# Test_case = int(input())
#
# for tc in range(1, Test_case + 1):
#     N = int(input())
#     grid = [[0 for i in range(N)] for i in range(N)]  # 2차원 배열 생성
#     row = 0  # 행
#     col = -1  # 열 / 달팽이모양으로 숫자가 증가하려면 첫 이동을 열부터 시작해야하기 때문에(move를 더해주면서 시작) -1부터 시작
#     move = 1  # 이동
#     cnt = 1  # 인덱스에 채워질 숫자
#     while N > 0:
#         for i in range(N):  # N의 범위만큼 열 증가
#             col += move
#             grid[row][col] = cnt
#             cnt += 1
#
#         N -= 1  # 한 줄 채워졌기때문에
#
#         for i in range(N):
#             row += move
#             grid[row][col] = cnt
#             cnt += 1
#
#         move *= -1  # 달팽이모양으로 숫자를 증가시키려면 열 +1 행 +1 열 -1 행 -1 순이기때문에
#     print(f'#{tc}')
#     for i in grid:
#         print(*i)

# ----------------------------------------------------------------- #
# 2023 - 02 - 24 복습

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    row, col, move, num = 0, -1, 1, 1  # col부터 이동하기때문에 col = -1
    while N > 0:
        for i in range(N):
            col += move
            arr[row][col] += num
            num += 1

        N -= 1  # N -1을 해줘야 남은 칸들을 채워갈 때 범위를 넘지 않을 수 있음

        for j in range(N):
            row += move
            arr[row][col] += num
            num += 1

        move *= -1  # 행 열 한번씩 돌때마다 방향 꺽어주기 때문에
    print(f'#{tc}')
    for k in range(len(arr)):
        print(*arr[k])
