# x = [55, 7, 78, 12, 42]
#
# for i in range(len(x)-1, 0 , -1) :
# 	for j in range(len(x)-1) :
# 			if x[j] > x[j+1] :
# 				x[j], x[j+1] = x[j+1], x[j]
# print(x)


# N = int(input())
# arr = list(map(int, input().split()))
# for i in range(N-1, 0, -1) : # 각 구간의 끝
# 	for j in range(i) :			# 비교할 왼쪽 요소
# 		if arr[j] > arr[j+1] :
# 			arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

# T = int(input())
#
# for i in range(1, T + 1):
#     N, M = map(int, input().split())
#     ai = list(map(int, input().split()))
#     max_sum = 0
#     min_sum = 1000000
#     for j in range(N - M + 1):
#         SUM = 0
#         for l in range(M):
#             SUM += ai[j:j + M][l]
#         if SUM > max_sum:
#             max_sum = SUM
#         if SUM < min_sum:
#             min_sum = SUM
#     print(f'#{i} {max_sum - min_sum}')

