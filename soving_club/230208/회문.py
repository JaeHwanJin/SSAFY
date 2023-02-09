'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ

출력
#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT

'''
from pprint import pprint

# Test_case = int(input())
#
# for tc in range(1, Test_case + 1):
#     n, m = map(int, input().split())
#
#     row_list = [input() for i in range(n)]
#     col_list = list(zip(*row_list))  # row_list를 열 기준으로 변환
#
#     result = ''
#
#     for j in range(n):
#         start = 0  # m 크기만큼만 비교를 해야 하기 때문에 시작 값 지정
#         while start < n - m + 1:
#             if start != 0:
#                 if row_list[j][start: start + m] == row_list[j][start + m - 1:start - 1:-1]:
#                     result = row_list[j][start: start + m]
#                     break
#             else:
#                 if row_list[j][start: start + m] == row_list[j][start + m - 1::-1]:
#                     result = row_list[j][start: start + m]
#                     break
#             if result != '':
#                 break
#             start += 1
#
#     if result == '':
#         for j in range(n):
#             word = ''.join(col_list[j])
#             start = 0
#             while start < n - m + 1:
#                 if start != 0:
#                     if word[start: start + m] == word[start + m - 1:start - 1:-1]:
#                         result = word[start: start + m]
#                     break
#                 else:
#                     if word[start: start + m] == word[start + m - 1::-1]:
#                         result = word[start: start + m]
#                     break
#                 if result != '':
#                     break
#                 start += 1
#
#     print(f'#{tc} {result}')

testCase = int(input())

def check_word(matrix, N, M, isrow):
    for j in range(N):
        start = 0
        while start < N - M + 1:
            if not isrow:  # 입력값 그대로 join
                check = matrix[j]
            else:  # 입력값을 세로열로 join
                check = zip(matrix[j])
            if start != 0:
                if check[start:start + M] == check[start + M - 1:start - 1:-1]:
                    return check[start:start + M]
            else:
                if check[start:start + M] == check[start + M - 1::-1]:
                    return check[start:start + M]
            start += 1
    return None


for i in range(1, testCase + 1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    result = check_word(matrix, N, M, False)
    if result == None:
        result = check_word(matrix, N, M, True)

    print(f'#{i} {result}')
