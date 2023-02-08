'''
1 이상 100만(106) 이하의 모든 소수를 구하는 프로그램을 작성하시오.
참고로, 10 이하의 소수는 2, 3, 5, 7 이다.

[입력]
이 문제의 입력은 없다.

[출력]
1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.

입력

출력
 2 3 5 7 .... (생략) ... 999983
'''

# 2 ~ n-1 나누는거를 시도했을 때... 나머지가 0인 경우가 없다면 소수

# 1번째 방법 (단점으로 연산이 오래 걸린다...)
# def is_prime_number(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# 전역 변수로 리스트를 생성
# 2~n-1 나누는거를 시도했을 때... 나머지가 0인 경우가 없다면 소수o
# def is_prime_number(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#



# 전역 변수로 하나 리스트를 생성
isPrime = []

# 에라토스테네스의 체 구현 함수, N의 범위는 우리가 찾을 소수 범위 최대값.
def seive(N):
    global isPrime
    isPrime = [True] * (N + 1)
    isPrime[0] = isPrime[1] = False # 0과 1은 소수가 아니므로 False 대입 (기저조건)
    # 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
    for i in range(2, int(N**0.5)+1):
        # 체크가 안된 값이 있다면 (소수)
        if isPrime[i]:
            # pass # 이 i라는 숫자는 소수!
            # 자기 자신을 제외한 i의 배수를 모두 지운다.
            for j in range(i*2, N+1, i):
                isPrime[j] = False # 얘는 소수가 아닙니다...
    pass
    # return isPrime

# num이 소수라면 True 를 반환하는 함수.
def is_prime_number(num):
    global isPrime
    return isPrime[num]



if __name__ == '__main__':
    seive(10 ** 6)
    prime_numbers = []
    for i in range(2, 10 ** 6):
        if is_prime_number(i):
            prime_numbers.append(i)

    print(*prime_numbers)


# 그림에서 회색 사각형으로 두른 수들이 여기에 해당한다.
# 2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)

# 남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
# 자기 자신을 제외한 3의 배수를 모두 지운다.
# 남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
# 자기 자신을 제외한 5의 배수를 모두 지운다.
# 남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
# 자기 자신을 제외한 7의 배수를 모두 지운다.
# 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.