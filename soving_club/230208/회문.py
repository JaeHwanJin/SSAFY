from pprint import pprint

Test_case = int(input())

for tc in range(1, Test_case + 1):

    n, m = map(int, input().split())
    row_list = [input() for i in range(n)]
    col_list = list(zip(*row_list))

    result = ''

    for j in range(n):
        start = 0
        while start < n - m + 1:
            word_list = ''.join(col_list[j])
            if start == 0:
                if row_list[j][start: start + m] == row_list[j][start + m - 1::-1]:
                    result = row_list[j][start: start + m]
                elif word_list[start: start + m] == word_list[start + m - 1::-1]:
                    result = word_list[start: start + m]
            else:
                if row_list[j][start: start + m] == row_list[j][start + m - 1:start - 1:-1]:
                    result = row_list[j][start: start + m]
                elif word_list[start: start + m] == word_list[start + m - 1:start - 1:-1]:
                    result = word_list[start: start + m]
            if result != '':
                break
            start += 1

    print(f'#{tc} {result}')

# testCase = int(input())
#
# def check_word(matrix, N, M, isrow):
#     for j in range(N):
#         start = 0
#         while start < N - M + 1:
#             if not isrow:  # 입력값 그대로 join
#                 check = matrix[j]
#             else:  # 입력값을 세로열로 join
#                 check = zip(matrix[j])
#             if start != 0:
#                 if check[start:start + M] == check[start + M - 1:start - 1:-1]:
#                     return check[start:start + M]
#             else:
#                 if check[start:start + M] == check[start + M - 1::-1]:
#                     return check[start:start + M]
#             start += 1
#     return None
#
#
# for i in range(1, testCase + 1):
#     N, M = map(int, input().split())
#     matrix = [input() for _ in range(N)]
#     result = check_word(matrix, N, M, False)
#     if result == None:
#         result = check_word(matrix, N, M, True)
#
#     print(f'#{i} {result}')
