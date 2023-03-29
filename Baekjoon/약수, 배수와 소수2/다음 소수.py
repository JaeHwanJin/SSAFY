'''
다음 소수 다국어

문제
정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

출력
각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

예제 입력 1
3
6
20
100
예제 출력 1
7
23
101
'''
# 1번째 풀이 실패...

# N = int(input())
# for n in range(N):
#     n = int(input())
#     while True:
#         for i in range(2, int(n ** (1 / 2)) + 1):
#             if n % i == 0:
#                 break
#         else:
#             print(n)
#             break
#         n += 1

# 2번째 풀이

# def prime_number(num):
#     if num == 0 or num == 1:
#         return False
#     for i in range(2, int(num ** (0.5)) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# T = int(input())
# for tc in range(T):
#     num = int(input())
#     while True:
#         if prime_number(num):
#             print(num)
#             break
#         else:
#             num += 1
