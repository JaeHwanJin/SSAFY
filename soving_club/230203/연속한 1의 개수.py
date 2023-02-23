'''
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

입력
첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N, 다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
1<=T<=10, 10<=N<=1000

출력
#과 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

입력
3
10
0011001110
10
0000100001
10
0111001111

출력
#1 3
#2 1
#3 4
'''
# T = int(input())
#
# for i in range(1, T + 1):
#     N = int(input())
#     number = list(map(int, input()))
#     cnt = 0
#     x = 0
#     List = []
#     for j in range(N):
#         if 1 == number[j]:
#             cnt += 1
#             x = cnt
#             List.append(x)
#         if 0 == number[j]:
#             cnt = 0
#
#     for k in range(len(List)-1):
#         if x < List[k]:
#             x = List[k]
#
#     print(f'#{i} {x}')

# -------------------------------------- #
# 2023 - 02 - 23 복습
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input()))
    cnt = 0
    result = []
    for i in range(N):
        if num[i] == 1:  # 연속된 1의 개수를 세기위한
            cnt += 1
        else:            # 1이 아닌 수를 만나면 연속이 깨지기때문에 cnt 값 초기화
            result.append(cnt)
            cnt = 0
    result.append(cnt)
    print(f'#{tc} {max(result)}')
