'''
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
3 4 + .
Forth에서는 동작은 다음과 같다.
숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.
Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
다음은 Forth 연산의 예이다.

코드       출력
4 2 / .     2
4 3 - .     1

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
나눗셈의 경우 항상 나누어 떨어진다.

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

입력
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .

출력
#1 84
#2 error
#3 168
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    for i in range(N):
        string = list(map(str, input().split()))
        operators = {
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b
        }

        # 스택 변수
        stack = []
        # 후위표현식의 문자열을 순회
        for ch in string:
            # 1. 피연산자(숫자)를 만난다면 stack에 push.
            if ch.isnumeric():
                stack.append(ch)
            # 2. 연산자를 만난다면 stack에 있는 값을 2개 꺼내고(popx2) 연산을 진행하고
            #     결과를 다시 stack에 넣어준다.
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                c = operators[ch](b, a)
                stack.append(c)

        # stack에 요소가 하나 남는데, 이 값이 결괏값...
        result = stack.pop()
        print(result)


# # 2. 하나하나 비교하면서 탐색할꺼야
# def dfs(x, y):
#     miro[x][y] = 1  # 그 길을 지나가면 1로 변경
#     for i in range(4):  # 2)4개방향을 탐색해본다
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:  # 범위 안에 있는 경우
#             if miro[nx][ny] == '0':  # 갈길이 있는 경우
#                 dfs(nx, ny)  # 재귀를 불러옴
#             elif miro[nx][ny] == '3':  # 값이 3이면(도착했다면)
#                 global ans  # 답은 1!
#                 ans = 1
#                 return
#
#
# for tc in range(1, T + 1):
#
#     n = int(input())
#
#     # 미로 만들기
#     miro = [list(input()) for i in range(n)]
#
#     # 1.방향 탐색하기 위해서 dx,dy정의 위,아래,왼,오
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#
#     for i in range(n):  # 시작지점 찾기
#         for j in range(n):
#             if miro[i][j] == '2':
#                 start_x = i
#                 start_y = j
#     ans = 0
#     dfs(start_x, start_y)
#     print(f'#{tc} {ans}')