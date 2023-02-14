# 자기 자신을 호출하여 순환 수행되는 것
# 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성 가능
# 예시 Factorial : 1부터 n 까지의 모든 자연수를 곱하여 구하는 연산
def factorial(n):
    if n == 1:  # n이 1일 때
        return 1  # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)  # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함


# print(factorial(5))


# 피보나치 수를 구하는 재귀함수
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(5))


# Memoization
n = 100
memo = [0] * (n + 1)
memo[0] = 0
memo[1] = 1


def fibo1(n):
    global memo
    if n < 2 or memo[n]:
        return memo[n]
    # # 이 전에 계산된 값이 있다면 이를 반환
    # if memo[n]:
    #     return memo[n]  # 계산된 값

    # 계산된 값을 저장
    memo[n] = fibo1(n - 1) + fibo1(n - 2)
    return memo[n]

print(fibo1(10))


# 동적계획 알고리즘은 그리디 알고리즘과 같이 최적화문제를 해결하는 알고리즘이다.
# 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여,
# 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.

def fibo2(n):
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]