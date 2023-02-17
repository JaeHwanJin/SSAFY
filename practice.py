T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mr = [-1, -1, 0, 1, 1, 1, 0, -1]
    mc = [0, 1, 1, 1, 0, -1, -1, -1]
    high = arr[1][1]
    low = arr[1][1]
    m = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
                if all(arr[i][j] > arr[i + mr[k]][j + mc[k]] for k in range(8)):
                    m.append(arr[i][j])
    MAX = 0
    MIN = 10000000
    if len(m) > 1:
        for l in range(len(m)):
            if MAX < m[l]:
                MAX = m[l]
            if MIN > m[l]:
                MIN = m[l]
        print(f'#{tc} {MAX - MIN}')
    else:
        print(f'#{tc} -1')

#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for i in range(N)]
#     high = arr[1][1]
#     low = arr[1][1]
#     for i in range(1, N - 1):  # 0번 인덱스와 끝 인덱스는 포함시키지 않기때문에 range 범위를 1, N-1로 설정
#         for j in range(1, N - 1):
#             for mi, mj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 우하좌상 값 비교
#                 if 0 <= i + mi <= N - 1 or 0 <= j + mj <= N - 1:
#                     break
#             if high < arr[i + mi][j + mj]:
#                 high = arr[i][j]
#             if low > arr[i + mi][j + mj]:
#                 low = arr[i][j]
#     print(low, high)
