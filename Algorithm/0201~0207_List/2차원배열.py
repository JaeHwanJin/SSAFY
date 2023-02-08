# 참고 사이트
# https://velog.io/@gndan4/2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%88%9C%ED%9A%8C-%EB%B6%80%EB%B6%84-%EC%A7%91%ED%95%A9%EB%B9%84%ED%8A%B8-%EC%97%B0%EC%82%B0

# from pprint import pprint

# 2차원 배열 생성
# Array = []
#
# # 직접 값 입력
# # N = int(input())
# # Array = [list(map(int, input().split())) for _ in range(N)]
# # pprint(Array)
#
# # Array = [[col for col in range(5)] for row in range(5)]
# # pprint(array)
#
#
# for i in range(5):
#     array = []
#     for j in range(5):
#         array.append(0)
#     Array.append(array)
# # pprint(Array)

# 행 우선 순회
# cnt = 1
# for i in range(len(Array)):
#     for j in range(len(Array[0])):
#         Array[i][j] = cnt
#         cnt += 1
# # pprint(Array)

# 열 우선 순회
# cnt = 1
# for i in range(len(Array)):
#     for j in range(len(Array[0])):
#         Array[j][i] = cnt
#         cnt += 1
# # pprint(Array)

# 지그재그 순회
# cnt = 1
# for i in range(len(Array)):
#     for j in range(len(Array[0])):
#         if i % 2:
#             Array[i][(len(Array[0]) - 1 - j)] = cnt
#             cnt += 1
#         else:
#             Array[i][j] = cnt
#             cnt += 1
# # pprint(Array)
#
# cnt = 1
# for i in range(len(Array)):
#     for j in range(len(Array[0])):
#         Array[i][j + ((len(Array[0]) - 1 - 2 * j) * (i % 2))] = cnt
#         cnt += 1
#
# # pprint(Array)

# 부분집합 구하기
# arr = list(map(int, input().split()))  # 구하고자 하는 부분집합의 집합
#
# for i in range(1 << len(arr)):  # arr 집합의 부분집합의 총개수 2의 n제곱 - 1
#     new_list = []
#     for j in range(len(arr)):
#         if i & (1 << j):
#             new_list.append(arr[j])
#     print(new_list)

# 부분집합의 합
# def is_zero_subset(arr):
#     '''
#     부분집합의 합이 0이 되도록 하는 값이 존재하는지 계산하는 함수
#     :param arr: 정수 10개의 배열
#     :return: 합이 0이 되는 부분집합이 있다면 True 반환
#     '''
#     # 부분집합
#     n = len(arr)
#     for i in range(1, 1 << n):
#         hap = 0
#         for j in range(n):
#             if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소 출력
#                 # 이 안에서 합을 진행
#                 hap += arr[j]
#         # 0이 된다면 True 반환
#         if hap == 0:
#             return True
#     # 부분집합의 합으로 0이 되는 것이 없다면 False 반환
#     return False
#
#
# # 정수 10개의 입력을 받는다
# # arr = list(map(int, input().split()))
# # print(is_zero_subset(arr))

# 델타를 이용한 2차원 배열 탐색(달팽이)

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = 3
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             ni, nj = i + di[k], j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(i, j, ni, nj)

3
40+480
# N = 3
# for i in range(N):
#     for j in range(N):
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(i, j, ni, nj)

N = 5
arr = [[0] * N for _ in range(N)]

num = 0  # 배열에 넣을 숫자
y = 0  # 줄 위치
x = -1  # 칸 위치
size = N  # 배열 크기
step = 1  # 증가/감소 크기: 1, -1

while size > 0:
    for _ in range(size):  	# 가로로 이동
        x += step
        num += 1
        arr[y][x] = num
    size -= 1

    for _ in range(size):	# 세로로 이동
        y += step
        num += 1
        arr[y][x] = num
    step *= -1

for i in range(N):
    for j in range(N):
        print("%2d " % arr[i][j], end='')
    print()

