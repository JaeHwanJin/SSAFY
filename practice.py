from pprint import pprint

# T = int(input())
# for tc in range(1, T + 1):
#     N, K, A, B = map(int, input().split())
#     star = [list(map(str, input().split())) for _ in range(N)]
#     STAR = 0
#     star_cnt = 0
#     result = 0
#     check = 0
#     for i in range(N):
#         for j in range(N):
#             if star[i][j] == '*':
#                 star_cnt += 1
#     while True:
#         UP, DOWN = A - K // 2, A + K // 2
#         LEFT, RIGHT = B - K // 2, B + K // 2
#         for i in range(UP, DOWN + 1):
#             for j in range(LEFT, RIGHT + 1):
#                 if star[i][j] == '*':
#                     STAR += 1
#         if STAR == star_cnt:
#             result += 1
#             K -= 2
#             check += 1
#         else:
#             break
#
#     if check == 0:
#         print(f'{tc} -1')
#     else:
#         print(f'#{tc} {result}')

# T = int(input())
# for tc in range(1, T + 1):
#     N, K, A, B = map(int, input().split())
#     star = [list(map(str, input().split())) for _ in range(N)]
#     star_cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if star[i][j] == '*':
#                 star_cnt += 1
#     result = 0
#     while True:
#         UP, DOWN = A - K // 2, A + K // 2
#         LEFT, RIGHT = B - K // 2, B + K // 2
#         for i in range(UP, DOWN + 1):
#             for j in range(LEFT, RIGHT + 1):
#                 if star[i][j] == '*':
#                     result += 1


# 첫 입력값이 정점의 개수
N = int(input())  # 13

# 왼쪽 자식 배열
left = [0 for _ in range(N + 1)]  # [0] * (N+1)
# 오른쪽 자식 배열
right = [0 for _ in range(N + 1)]

# 부모 - 자식
arr = list(map(int, input().split()))  # [부모1, 자식1, 부모2, 자식2 ,...]
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

# 부모 자식을 순회하면서 왼쪽, 오른쪽 자식을 넣어주는 과정...
for i in range(0, len(arr), 2):
    # 부모 i, 자식 i+1
    p, c = arr[i], arr[i + 1]
    # 왼쪽 자식이 있는지 여부 -> 없다면 왼쪽에 자식 할당
    if left[p] == 0:
        left[p] = c
    # -> 있다면.. 오른쪽에 할당
    else:
        right[p] = c
# print(left)
# print(right)
# 카운트 변수 (전역)
count = 0
def LVR(t):
    global count
    if t != 0:
        LVR(left[t])  # L 왼쪽
        print()  # V
        LVR(right[t])  # R 오른쪽


LVR(3)
print(count)

count = 0


