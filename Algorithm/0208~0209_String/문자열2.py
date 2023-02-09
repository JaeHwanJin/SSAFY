def bf1(p, t, len_p, len_t):
    for i in range(len_t - len_p + 1):
        for j in range(len_p):
            if t[i + j] != p[j]:
                break
        else:
            return i  # 패턴이 매칭된 위치
    return -1  # 발견 못했을경우


# 슬라이싱을 사용한 방법
def bf2(p, t, len_p, len_t):
    for i in range(len_t - len_p + 1):
        # p에서 문자열을 len_t만큼 가져오고
        # t와 비교를 수행한다.
        if p[i:i + len_p] == t:
            return i
    return -1


# 문자열 메소드를 사용하는 방법
def bf3(p, t, len_p, len_t):
    # 문자열 find 메소드...
    return t.find(p)  # 2


# 카운트 하는 함수를 만들어보자, find 메소드를 써서
def count1(p, t, len_p, len_t):
    # 카운트 하는 변수
    cnt = 0
    # 인덱스를 저장하는 i 변수
    i = 0
    # while문의 조건 작성
    while i != -1:
        if i == 0:
            i = t.find(p)
        else:
            i = t.find(p, i + 1)
        if i != -1:
            cnt += 1
    return cnt


# count 메소드 사용하기
def count2(p, t, len_p, len_t):
    return t.count(p)


p = 'is'  # 찾을 패턴
t = 'This is a book~!'  # 전체문장
M = len(t)
N = len(p)
len_p = len(p)
len_t = len(t)

print(bf1(p, t, len_p, len_t))
print(bf2(p, t, len_p, len_t))
print(bf3(p, t, len_p, len_t))
print(count1(p, t, len_p, len_t))
print(count2(p, t, len_p, len_t))

# def bf(p, t, N, M):
#     i = 0  # t에서의 비교 위치
#     j = 0  # p에서의 비교 위치
#     while i < N and j < M:  # 비교 할 문장이 남아있고, 패턴을 찾이 전이면
#         if t[i] != p[j]:  # 서로 다른 글자를 만나면
#             i += 1  # 비교를 시작한 위치로
#             j += 1  # 패턴의 시작 전으로
#         else:
#             i = i - j + 1
#             j = 0
#         # if t[i] != p[j]:
#         #     i -= j
#         #     j -= -1
#         # i += 1
#         # j += 1
#     if j == M:  # 패턴을 찾은 경우
#         return i - M
#     else:
#         return -1
#
#
# def bf2(p, t, N, M):
#     for i in range(N - M + 1):
#         for j in range(M):
#             if t[i + j] != p[j]:
#                 break
#         else:
#             return i
#
#
# print(bf(p, t, N, M))

# kmp
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    # preprocessing
    j = 0 # 일치한 개수== 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j          # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # search
    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치
    while i < N and j <= M:
        if j==-1 or t[i]== p[j]:     # 첫글자자 불일치했거나, 일치하면
            i += 1
            j += 1
        else:               # 불일치
            j = lps[j]
        if j==M:    # 패턴을 찾을 경우
            print(i-M, end = ' ')    # 패턴의 인덱스 출력
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
p =  "AAAA"
kmp(t, p)
t = "AAAAABAAABA"
p =  "AA"
kmp(t, p)