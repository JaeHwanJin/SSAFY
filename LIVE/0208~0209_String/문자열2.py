# 1. 이중포문을 사용한 방법
def bf1(p, t, M, N):
    for i in range(N - M + 1):
        for j in range(M):
            if t[i + j] != p[j]:
                break
        else:
            return i  # 패턴이 매칭된 위치
    return -1


# 2. 슬라이싱을 사용한 방법
def bf2(p, t, M, N):
    for i in range(N - M + 1):
        # p에서 문자열을 M만큼 가져오고
        # t와 비교를 수행한다.
        if t[i:i + M] == p:
            return i
    return -1


# 3. 문자열 메소드를 활용하는 방법
def bf3(p, t, M, N):
    # 문자열 find 메소드...
    return t.find(p)  # 2
    # p.find(t, 3) #5


# 4. 카운트하는 함수를 만들보자, find메소드를 써서
def count1(p, t, M, N):
    # 카운트 하는 변수
    cnt = 0
    # 인덱스를 저장하는 i 변수
    i = 0
    # while문의 조건 작성
    while i != -1:
        # find 메소드를 사용해서 i 인덱스를 갱신
        if i == 0:
            i = t.find(p)
        else:
            i = t.find(p, i + 1)
        if i != -1:
            cnt += 1
    return cnt


# 4. 카운트하는 함수를 만들보자, find메소드를 써서
def count2(p, t, M, N):
    # 카운트 하는 변수
    cnt = 0
    # 인덱스를 저장하는 i 변수
    i = -1
    # while문의 조건 작성
    while (i := t.find(p, i + 1)) != -1:
        cnt += 1

    return cnt


# 5. count 메소드 사용하기
def count3(p, t, M, N):
    return t.count(p)


# p = 'is'  # 찾을 패턴
# t = 'This is a book~!'  # 전체 텍스트
# M = len(p)  # 찾을 패턴의 길이
# N = len(t)  # 전체 텍스트의 길이
#
# print(bf1(p, t, M, N))
# print(bf2(p, t, M, N))
# print(bf3(p, t, M, N))
#
# print(count1(p, t, M, N))
# print(count2(p, t, M, N))
# print(count3(p, t, M, N))


# kmp
def kmp(t, p):
    len_t = len(t)
    len_p = len(p)
    lps = [0] * (len_p + 1)
    # preprocessing
    j = 0  # 일치한 개수== 비교할 패턴[ 위치
    lps[0] = -1
    for i in range(1, len_p):
        lps[i] = j  # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[len_p] = j
    # search
    i = 0  # 비교할 텍스트 위치
    j = 0  # 비교할 패턴 위치
    while i < len_t and j <= len_p:
        if j == -1 or t[i] == p[j]:  # 첫글자자 불일치했거나, 일치하면
            i += 1
            j += 1
        else:  # 불일치
            j = lps[j]
        if j == len_p:  # 패턴을 찾을 경우
            print(i - len_p, end=' ')  # 패턴의 인덱스 출력
            j = lps[j]

    print()
    return


t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)
t = 'AABAACAADAABAABA'
p = 'AABA'
kmp(t, p)
t = "AAAAABAAABA"
p = "AAAA"
kmp(t, p)
t = "AAAAABAAABA"
p = "AA"
kmp(t, p)
