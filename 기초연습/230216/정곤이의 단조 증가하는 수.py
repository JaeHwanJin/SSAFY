# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_num = 0     # 단조 증가하는 수 중 가장 큰 값을 넣기 위한 변수
#     danjo = []      # 단조 증가하는 수를 모으기 위한 리스트
#     for i in range(N):
#         for j in range(i + 1, N):
#             a = arr[i] * arr[j]
#             str_a = str(a)
#             if len(str_a) > 1 and int(str_a[0]) < int(str_a[1]):     # 곱이 단조 증가하는 수인지 확인
#                 danjo.append(a)
#     for k in range(len(danjo)): # 곱이 단조 증가하는 수들 중 가장 큰 값을 max_num에 저장
#         if max_num < danjo[k]:
#             max_num = danjo[k]
#     if len(danjo) == 0: # 단조리스트의 길이가 0 이면 곱이 단조증가하는 수라는 조건을 만족하지 못했기때문에 -1을 출력
#         print(f'#{tc} {-1}')
#     else:
#         print(f'#{tc} {max_num}')
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     max_num = 0  # 출력 할 최대값
#     for i in range(N):
#         for j in range(i + 1, N):
#             int_a = 0  # 최댓값을 구하기 위한 int
#             str_a = []  # 단조 증가하는 수인지 확인하기 위한 str
#             int_a = arr[i] * arr[j]
#             str_a += str(arr[i] * arr[j])
#             # print(str_a)
#             for k in range(len(str_a) - 1):
#                 if str_a[k] > str_a[k + 1]: # 인접한 인덱스 값끼리 비교해서 단조인지 확인
#                     break
#             else:
#                 if int_a > max_num: # 단조인 수 중 가장 큰 값을 max_num에 입력
#                     max_num = int_a
#
#     if max_num == 0:
#         print(f'#{tc} {-1}')
#     else:
#         print(f'#{tc} {max_num}')
