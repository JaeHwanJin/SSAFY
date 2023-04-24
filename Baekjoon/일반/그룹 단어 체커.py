'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.

예제 입력 1
3
happy
new
year
예제 출력 1
3
예제 입력 2
4
aba
abab
abcabc
a
예제 출력 2
1
예제 입력 3
5
ab
aa
aca
ba
bb
예제 출력 3
4
예제 입력 4
2
yzyzy
zyzyz
예제 출력 4
0
예제 입력 5
1
z
예제 출력 5
1
'''

# 첫번째 풀이 오답
# 왜 오답인지 모르겠다... 하드코딩이긴하지만 맞는거같은데...
# 반례 abcb abcbdb
# N = int(input())
# result = 0
# for i in range(N):
#     word = list(map(str, input()))
#     check = []  # 떨어져서 나타나는지 확인하기 위한 리스트
#     cnt = 0
#     for j in range(len(word) - 1):
#         if word[j] != word[j + 1]:  # 인접한 문자끼리 같지 않을 경우 연속한 문자가 끝난것이기 때문에 check에 추가해준다.
#             check.append(word[j])
#             word.pop(j)  # 연속한문자가 끝나면 word에서 제거해준다
#             word.append('/')  # for문 index에러를 방지하기 위한 append
#             for k in range(len(check)):
#                 if check[k] in word:  # 연속한 문자가 끝났는데 word에 있다면 그룹문자가 아니다.
#                     cnt += 1
#         else:
#             word.pop(j)
#             word.append('/')
#     if cnt == 0:
#         result += 1
#     print(result)

# 두번째 풀이 정답
# 슬라이싱을 잘 활용하고 범위를 잘 생각하자
# N = int(input())
# cnt = N
#
# for i in range(N):
#     word = input()
#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:    # 연속한 문자면 pass
#             pass
#         elif word[j] in word[j+1:]: # 연속한 문자가 끝이 났는데 그 뒤에 같은 문자가 있다면 그룹문자가 아니다
#             cnt -= 1
#             break
#
# print(cnt)
