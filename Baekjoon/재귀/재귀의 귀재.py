'''
재귀의 귀재

문제
정휘는 후배들이 재귀 함수를 잘 다루는 재귀의 귀재인지 알아보기 위해 재귀 함수와 관련된 문제를 출제하기로 했다.

팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다. 팰린드롬의 예시로 AAA, ABBA, ABABA 등이 있고, 팰린드롬이 아닌 문자열의 예시로 ABCA, PALINDROME 등이 있다.

어떤 문자열이 팰린드롬인지 판별하는 문제는 재귀 함수를 이용해 쉽게 해결할 수 있다. 아래 코드의 isPalindrome 함수는 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환하는 함수다.

def recursion(s, l, r):
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

print('ABBA:', isPalindrome('ABBA'))
print('ABC:', isPalindrome('ABC'))

정휘는 위에 작성된 isPalindrome 함수를 이용하여 어떤 문자열이 팰린드롬인지 여부를 판단하려고 한다.

구체적으로는, 문자열
문자열 S를 isPalindrome 함수의 인자로 전달하여 팰린드롬 여부를 반환값으로 알아낼 것이다. 더불어 판별하는 과정에서 recursion 함수를 몇 번 호출하는지 셀 것이다.

정휘를 따라 여러분도 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.

입력
첫째 줄에 테스트케이스의 개수 T가 주어진다.
둘째 줄부터 T개의 줄에 알파벳 대문자로 구성된 문자열 S가 주어진다.
출력
각 테스트케이스마다, isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수를 한 줄에 공백으로 구분하여 출력한다.

예제 입력 1
5
AAA
ABBA
ABABA
ABCA
PALINDROME

예제 출력 1
1 2
1 3
1 3
0 2
0 1
'''


def recursion(s, st, end):
    global cnt  # 호출 횟수 cnt를 사용하기 위한 global cnt
    cnt += 1    # recursion 함수 호출시마다 cnt 1씩 증가
    if st >= end:
        return 1
    elif s[st] != s[end]:
        return 0
    else:
        return recursion(s, st + 1, end - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


for i in range(int(input())):
    cnt = 0 # 호출 횟수
    print(isPalindrome(input()), cnt)

'''
문제를 보면 펠린드롬인지 판별하는 함수를 알려준다.
해당 함수를 활용해 펠린드롬인지와 호출 회수를 출력하면 되는 문제이다.
재귀함수 공부를 위해 해당 함수를 보지 않고 완전히 이해할때까지 반복해서 작성해봤다.
다른 공부보다 재귀함수부분이 제일 어려운것 같다.... 재귀함수에서 시간을 많이 소요할 것 같다...
'''