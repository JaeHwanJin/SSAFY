'''
영준이는 당근 크기 선별기를 이용해 수확한 순서대로 당근의 크기를 기록하였다. 이 당근 선별기에는 특별한 기능이 있는데
연속으로 당근의 크기가 커진 경우 그 개수를 알려준다.
당근의 크기가 수확한 순서로 주어질 때, 선별기가 알려준 연속으로 커지는 당근의 갯수는 최대 얼마인지 확인하기 위한 프로그램을 만드시오.
연속으로 커지지않는 경우 구간의 최소 길이는 1이다.
N개의 당근을 수확하며, 당근의 크기 C는 1부터 10까지의 정수로 정해진다.
5<=N<=1000, 1<=C<=10
'''
# 입력
# 첫 줄에 테스트케이스의 개수 T, 다음 줄 부터 테스트케이스별로 첫 줄에 당근 개수 N, 다음 줄 당근의 크기 C를 의미하는 N개의 정수가 주어진다.

# 출력
# 테스트케이스번호와 연속으로 커지는 당근 개수의 최대값을 출력한다.
'''
입력
3
5
1 2 3 4 5
5
4 5 1 2 3
5
5 4 3 2 1
'''

'''
출력
#1 5
#2 3
#3 1
'''

# T = int(input())
# for i in range(1, T + 1):
#     cnt = 1
#     N = int(input())
#     size = list(map(int, input().split()))
#     size_list = []
#     for j in range(len(size) - 1):
#         if size[j] + 1 == size[j + 1]:
#             cnt += 1
#         else:
#             cnt = 1
#         size_list.append(cnt)
#     for k in range(len(size_list) - 1):
#         if cnt < size_list[k]:
#             cnt = size_list[k]
#
#     print(f'#{i} {cnt}')

# -------------------------------------- #
# 2023 - 02 - 23 복습

# 첫 줄에 테스트케이스의 개수 T
T = int(input())

for tc in range(1, T + 1):
    # 다음 줄 부터 테스트케이스별로 첫 줄에 당근 개수 N
    N = int(input())
    # 다음 줄 당근의 크기 C를 의미하는 N개의 정수가 주어진다.
    C = list(map(int, input().split()))
    result = []  # 연속으로 커지는 당근 개수 리스트
    cnt = 1  # 연속으로 커지는 당근 개수
    for i in range(N - 1):  # 비교 해서 연속이면 카운트 연속이 아니면 cnt result에 추가 후 1로 초기화
        if C[i] + 1 == C[i + 1]:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
    result.append(cnt) # 연속하다 끝나면 result에 추가
    # 테스트케이스번호와 연속으로 커지는 당근 개수의 최대값을 출력한다.
    print(f'#{tc} {max(result)}')


