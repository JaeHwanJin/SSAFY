'''
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.
level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

입력
첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

예제 입력 1
level
예제 출력 1
1
예제 입력 2
baekjoon
예제 출력 2
0
'''

word = input()
lword = len(word)

# 처음 풀이할 때 아래 처럼 풀었는데 이렇게 하면 llooalloo도 팰린드롬으로 인정하기 때문에 잘못된 코드이다.
# # 짝수일때 word의 길이를 반만큼 나누면 딱 떨어지기때문에 반으로 나눈 후 정렬 한 값이 같으면 팰린드롬이다.
# if lword % 2 == 0 and sorted(word[:lword//2]) == sorted(word[lword//2:]):
#     print(1)
# # 홀수일때 word의 길이를 반만큼 나누고 가운데 값을 제외한 값을 정렬 한 후 값이 같으면 팰린드롬이다
# elif lword % 2 != 0 and sorted(word[:lword//2]) == sorted(word[lword//2+1:]):
#     print(1)
# # 위 두가지를 제외한 경우는 모두 팰린드롬이 아니다.
# else:
#     print(0)

# 두번째 풀이
# 이렇게 하니 lellel 이나 oooooo 같은 값들도 팰린드롬이 아니라고 처리하더라...
# 정렬 하기 전에는 서로 값이 달라야 한다.

# # 짝수일때 word의 길이를 반만큼 나누면 딱 떨어지기때문에 반으로 나눈 후 정렬 한 값이 같으면 팰린드롬이다.
# if lword % 2 == 0 and word[:lword//2] != word[lword//2:] and sorted(word[:lword//2]) == sorted(word[lword//2:]) :
#     print(1)
# # 홀수일때 word의 길이를 반만큼 나누고 가운데 값을 제외한 값을 정렬 한 후 값이 같으면 팰린드롬이다
# elif lword % 2 != 0 and word[:lword//2] != word[lword//2+1:] and sorted(word[:lword//2]) == sorted(word[lword//2+1:]):
#     print(1)
# # 위 두가지를 제외한 경우는 모두 팰린드롬이 아니다.
# else:
#     print(0)

# 세번째 풀이 정답
# 슬라이싱을 활용해 앞 뒤를 비교

if lword % 2 == 0 and word[:lword // 2] == word[lword:lword // 2 - 1:-1]:
    print(1)

elif lword % 2 != 0 and word[:lword // 2] == word[lword:lword // 2:-1]:
    print(1)
# 위 두가지를 제외한 경우는 모두 팰린드롬이 아니다.
else:
    print(0)
