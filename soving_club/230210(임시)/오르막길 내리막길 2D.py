'''
어느날 교수님은 문득 OO산 등반을 하고 싶었다.
그래서 조교A에게 같이 산에 올라가자고 제안하였다.
조교는 한숨을 푹 쉬며, N*N 공간의 주변 일대에 산 정상의 높이가
가장 높은 산과 가장 낮은 산을 미리 파악해보기로 하였다.

*제약조건
1. 한 구역을 중심으로 4방이 높으면 산의 정상이다.
2. 단, 가장자리는 산의 정상으로 취급하지 않는다.
*모든 입력에는 반드시 산이 1개 이상 있다고 가정한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 10 )
다음 줄부터 테스트케이스의  정수 개수 N이 주어진다 ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 높이 값 a1가 공백과 함께 주어진다 ( 0 ≤ a1 ≤ 300 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 낮은 산과 가장 높은 산을 순서대로 출력하시오.

입력
3
3
1 2 3
4 5 3
4 1 2
4
1 1 1 1
1 5 1 1
1 1 6 1
1 1 1 1
5
1 1 1 1 1
1 6 1 3 1
1 1 2 1 1
1 1 1 1 1
1 1 1 1 1
출력
#1 5 5
#2 5 6
#3 2 6
'''

from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    high = arr[1][1]
    low = arr[1][1]
    for i in range(1, N - 1):  # 0번 인덱스와 끝 인덱스는 포함시키지 않기때문에 range 범위를 1, N-1로 설정
        for j in range(1, N - 1):
            for mi, mj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 우하좌상 값 비교
                if 0 <= i + mi <= N - 1 or 0 <= j + mj <= N - 1:
                    break
            if high < arr[i + mi][j + mj]:
                high = arr[i][j]
            if low > arr[i + mi][j + mj]:
                low = arr[i][j]
    print(low, high)

# arr = [[0] * 3 for i in range(3)]

# for i in range(3):
#     for j in range(3):
#         for mi, mj in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # 우 하 좌 상 순
#             mmi, mmj = i+mi, j+mj
#             if 0 <= mmi < 3 and 0 <= mmj < 3:
#                 arr[i][j] = arr[mmi][mmj]

# T = int(input())
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# for test_case in range(1, T+1):
#     total_move = 0
#
#     N = int(input())
#     mountain = []
#     for _ in range(N):
#         mountain.append(list(map(int, input().split())))
#
#     temp_min = 300
#     temp_max = 0
#     for i in range(1, N-1):
#         for j in range(1, N-1):
#             is_peak = False
#             for k in range(4):
#                 nx = i+dx[k]
#                 ny = j+dy[k]
#                 if mountain[i][j] <= mountain[nx][ny]:
#                     break
#                 is_peak = True
#             if is_peak:
#                 if temp_min > mountain[i][j]:
#                     temp_min = mountain[i][j]
#                 if temp_max < mountain[i][j]:
#                     temp_max = mountain[i][j]
#
#     print(f'#{test_case} {temp_min} {temp_max}')
