'''
정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.
그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.
예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
양의 정수 N 개 A1, …, AN이 주어진다.
 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.


[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.
두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.

[출력]
각 테스트 케이스마다 단조 증가하는 수인 Ai x Aj중에서 그 최댓값을 출력한다.
만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.

입력
1
4
2 4 7 10	// 테스트케이스 개수, T=1
// N=4
// A1=2, A2=4, A3=7, A4=10

출력
#1 28
'''
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 0     # 단조 증가하는 수 중 가장 큰 값을 넣기 위한 변수
    danjo = []      # 단조 증가하는 수를 모으기 위한 리스트
    for i in range(N):
        for j in range(i + 1, N):
            a = arr[i] * arr[j]
            str_a = str(a)
            if len(str_a) > 1 and int(str_a[0]) < int(str_a[1]):     # 곱이 단조 증가하는 수인지 확인
                danjo.append(a)
    for k in range(len(danjo)): # 곱이 단조 증가하는 수들 중 가장 큰 값을 max_num에 저장
        if max_num < danjo[k]:
            max_num = danjo[k]
    if len(danjo) == 0: # 단조리스트의 길이가 0 이면 곱이 단조증가하는 수라는 조건을 만족하지 못했기때문에 -1을 출력
        print(f'#{tc} {-1}')
    else:
        print(f'#{tc} {max_num}')
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
