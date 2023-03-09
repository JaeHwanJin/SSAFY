'''
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다.
하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.
이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다.

출력
각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

제한
4 ≤ n ≤ 10,000
예제 입력 1
3
8
10
16
예제 출력 1
3 5
5 5
5 11
'''


# 시간초과 실패실패...
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     pn = []  # N 이하의 소수를 담을 list
#     # 소수 찾기 for문
#     for i in range(2, N + 1):
#         cnt = 0
#         for l in range(2, int(i ** 0.5) + 1):
#             if i % l == 0:
#                 cnt += 1
#         if cnt == 0 :
#             pn.append(i)
#     result = 10000 # 골드바흐의 파티션 중 차이가 가장 작은 것을 담을 변수
#     x, y = 0, 0 # 차이가 가장 작은 소수 2개를 담을 변수
#     for j in range(len(pn)):
#         for k in range(j, len(pn)):
#             if pn[j] + pn[k] == N:
#                 if result > pn[k] - pn[j]:
#                     result = pn[k] - pn[j]
#                     x, y = pn[j], pn[k]
#     print(x, y)

# 소수인지 확인하는 함수
def prime(n):
    if n == 1:
        return False
    # n이 n제곱은 이하의 수로 나누어 떨어지지 않으면 그 이상의 수로도 나누어 떨어지지 않는다.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


T = int(input())
for tc in range(T):
    num = int(input())
    pn1, pn2 = num // 2, num // 2   # num을 반으로 나누고 각 각 +1 -1 해주면서 두 수가 소수인지 확인
    while pn1 > 0:
        if prime(pn1) and prime(pn2):
            print(pn1, pn2)
            break
        else:
            pn1 -= 1
            pn2 += 1

