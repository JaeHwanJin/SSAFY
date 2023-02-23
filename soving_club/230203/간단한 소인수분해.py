'''
숫자 N은 아래와 같다.
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.

[제약 사항]
N은 2 이상 10,000,000 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
10
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750

출력
#1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0
'''
#
# T = int(input())
#
# for i in range(1, T + 1):
#     N = int(input())
#     minority = 2
#     minority_list = []
#     minority_dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
#     while N // minority >= 1:
#         if N % minority == 0:
#             minority_list.append(minority)
#             N //= minority
#         elif N % minority != 0:
#             minority += 1
#     for j in minority_list:
#         if j in minority_dict.keys():
#             minority_dict[j] += 1
#     print(f'#{i}', *minority_dict.values())


# -------------------------------------- #
# 2023 - 02 - 23 복습
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# T = int(input())
# # 각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.
# for tc in range(1, T + 1):
#     cnt2, cnt3, cnt5, cnt7, cnt11 = 0, 0, 0, 0, 0
#     N = int(input())
#     while N > 1:  # 더 이상 나눌 수 없을때 까지 진행
#         if N % 2 == 0:  # 2로 나눴을때 나머지가 0이라면 2의 배수
#             N //= 2
#             cnt2 += 1
#         elif N % 3 == 0:  # 3로 나눴을때 나머지가 0이라면 3의 배수
#             N //= 3
#             cnt3 += 1
#         elif N % 5 == 0:  # 5로 나눴을때 나머지가 0이라면 5의 배수
#             N //= 5
#             cnt5 += 1
#         elif N % 7 == 0:  # 7로 나눴을때 나머지가 0이라면 7의 배수
#             N //= 7
#             cnt7 += 1
#         elif N % 11 == 0:  # 11로 나눴을때 나머지가 0이라면 11의 배수
#             N //= 11
#             cnt11 += 1
#     print(f'#{tc} {cnt2} {cnt3} {cnt5} {cnt7} {cnt11}')
