'''
어느날 교수님은 문득 OO산 등반을 하고 싶었다.
그래서 조교A에게 같이 산에 올라가자고 제안하였다.
조교는 한숨을 푹 쉬며, N*N 공간의 주변 일대에 산 정상의 높이가
가장 높은 산과 가장 낮은 산의 높이차를 파악해보기로 하였다.

*제약조건
1. 한 구역을 중심으로 8방으로 높으면 산의 정상이다.
2. 단, 가장자리는 산의 정상으로 취급하지 않는다.
3. 산이 하나 이하인 경우에는 수행하지 않는다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 10 )
다음 줄부터 테스트케이스의  정수 개수 N이 주어진다 ( 3 ≤ N ≤ 100 )
다음 줄에 N개의 높이 값 a1가 공백과 함께 주어진다 ( 0 ≤ a1 ≤ 300 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 산의 높이차를 순서대로 출력하시오.
(*산이 하나만 있거나 없는 경우에는 -1을 출력하시오.)

입력
4
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
1 5 1 1 1
1 1 1 5 1
1 1 1 1 1
1 1 1 1 1
5
1 1 1 1 1
1 6 1 3 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1
출력
#1 -1
#2 -1
#3 0
#3 4
'''

# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     mr = [-1, -1, 0, 1, 1, 1, 0, -1]
#     mc = [0, 1, 1, 1, 0, -1, -1, -1]
#     high = arr[1][1]
#     low = arr[1][1]
#     m = []
#     for i in range(1, N - 1):
#         for j in range(1, N - 1):
#                 if all(arr[i][j] > arr[i + mr[k]][j + mc[k]] for k in range(8)):
#                     m.append(arr[i][j])
#     MAX = 0
#     MIN = 10000000
#     if len(m) > 1:
#         for l in range(len(m)):
#             if MAX < m[l]:
#                 MAX = m[l]
#             if MIN > m[l]:
#                 MIN = m[l]
#         print(f'#{tc} {MAX - MIN}')
#     else:
#         print(f'#{tc} -1')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mr = [-1, -1, 0, 1, 1, 1, 0, -1]
    mc = [0, 1, 1, 1, 0, -1, -1, -1]
    mountain = []
    high = 0
    low = 10000
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            cnt = 0
            for k in range(8):
                nr, nc = i + mr[k], j + mc[k]
                if 0 <= nr < N and 0 <= nc < N and arr[i][j] > arr[nr][nc]:
                    cnt += 1
            if cnt == 8:
                mountain.append(arr[i][j])
    for l in mountain:
        if high < l:
            high = l
        if low > l:
            low = l
    if len(mountain) < 2:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {high - low}')
