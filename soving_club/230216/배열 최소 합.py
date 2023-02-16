'''
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
예를 들어 다음과 같이 배열이 주어진다.
2 1 2
5 8 5
7 2 2
이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

입력
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

출력
#1 8
#2 14
#3 9
'''


def check(col, sum):
    global min_num
    if sum > min_num:
        return
    if col == N:
        if sum < min_num:
            min_num = sum
    for row in range(N):
        if visited[row] == 0:
            print(visited)
            visited[row] = 1
            print(visited)
            print(f'sum = {sum}')
            print(f'arr[col][row] = {arr[col][row]}')
            check(col + 1, sum + arr[col][row])
            visited[row] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_num = 10000
    check(0, 0)
    print(f'#{tc} {min_num}')

# def dfs(r, current):
#     global min_sum
#     if current > min_sum:
#         return
#     if r == N:
#         if current < min_sum:
#             print(current)
#             min_sum = current
#     else:
#         for c in range(N):
#             if not visited[c]:
#                 print(f'visited = {visited}')
#                 print(f'visited[c] = {visited[c]}')
#                 visited[c] = 1
#                 print(f'r + 1 = {r+1} current{current} + matrix[r][c]{matrix[r][c]} = {current + matrix[r][c]}')
#                 print()
#                 dfs(r + 1, current + matrix[r][c])
#                 visited[c] = 0
#
#
# TestCase = int(input())
# for tc in range(1, TestCase + 1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#     min_sum = 101
#
#     dfs(0, 0)
#     print(f'#{tc} {min_sum}')

# def pm(x, num):
#     global min_num
#     if num > min_num:
#         # min_num = num
#         return
#     if x == N:
#         # print(num, min_num)
#         if num < min_num:
#             min_num = num
#     for i in range(N):
#         if visited[i] == 0:
#             # print(visited)
#             visited[i] = 1
#             # print(f'num = {num} arr[x][i] = {arr[x][i]}')
#             # print()
#             pm(x + 1, num + arr[x][i])
#             visited[i] = 0
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N
#     min_num = 10000
#     pm(0, 0)
#     print(f'#{tc} {min_num}')


# A = [1, 2, 3]
#
# def f(i,N):
#     # 기저조건 (i == N) 종료해
#     if i == N: #순열완성
#         print(A)
#         return
#
#     # for j : i -> N-1 [i,N)
#     for j in range(i, N):
#         #배열 요소 교환
#         A[i], A[j] = A[j], A[i]
#         f(i+1, N)
#         #배열 요소 원복
#         A[i], A[j] = A[j], A[i]
#
# A = [1,2,3]
# N = len(A)
# f(0,N)
#
#
# # row를 파라미터로 받는 최소 합을 찾는 함수
# def find_min(row):
#     global partial_sum, min_sum
#     # pruning을 위한 조건
#     # 부분합이 이미 최소합보다 크게되면 더 내려갈 의미가 없다.
#     if partial_sum > min_sum:
#         return
#     # 마지막 행에 도달하면 종료한다.
#     # 아직 더하는 연산이 없으므로 조건은 N-1이 아니라 N이 되어야한다.
#     if row == N:
#         # 마지막에 도달했는데 부분합이 최소합보다 작다면 갱신해준다.
#         if partial_sum < min_sum:
#             min_sum = partial_sum
#     # i는 col를 의미한다
#     for i in range(N):
#         # 아직 방문하지 않은 col이라면
#         if not visited[i]:
#             # 특정 row의 i번째 값으로 결정이 되있을 때에
#             # 방문으로 갱신
#             visited[i] = True
#             partial_sum += arry[row][i]
#             # i로 결정했을 때 그 아래를 계산한다.
#             find_min(row + 1)
#             # find_min이 바닥까지 가거나 pruning 된 후에야 위에 것이 끝나므로
#             # 다시 현재 row로 올라와야 한다.
#             visited[i] = False
#             partial_sum -= arry[row][i]
#
#
# # 테스트케이스 입력
# T = int(input())
# for idx in range(T):
#     # 배열의 길이
#     N = int(input())
#     arry = [list(map(int, input().split())) for _ in range(N)]
#     # 방문한 배열의 col 번호를 저장하기 위한 배열
#     visited = [False] * N
#     # 부분합과 최소값을 저장할 변수
#     # (N이 10보다 작고 10보다 작은 자연수가 주어지므로 최소값의 시작은 1000이면 충분)
#     partial_sum, min_sum = 0, 1000
#     # 최소 값을 찾기위한 함수
#     find_min(0)
#     print(min_sum)
#
#
#
# #방법 2
# def section_sum(idx, total):
#     global answer
#
#     if idx == N:
#         if total < answer:
#             answer = total
#             return
#
#     if total > answer:
#         return
#
#     for i in range(N):
#         if i not in visited:
#             visited.append(i)
#             section_sum(idx+1, total+matrix[idx][i])
#             visited.pop()
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     answer = 30
#     visited = []
#     section_sum(0, 0)
#     print('#{} {}'.format(tc, answer))
#
#
# #방법 3
# def backtracking(i, N, s, visited):
#     global sumV
#     if i == N:
#         if s < sumV:
#             sumV = s
#     elif s > sumV:
#         return
#     else:
#         for j in range(N):
#             if not visited[j]:
#                 visited[j] = 1
#                 backtracking(i+1, N, s+num_list[i][j], visited)
#                 visited[j] = 0
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     num_list = [list(map(int, input().split())) for _ in range(N)]
#     sumV = 100
#     visited = [0]*N
#
#     backtracking(0, N, 0, visited)
#     print(f'#{tc + 1} {sumV}')

#
# def count(idx, visited, SUM):
#     global MIN
#     if idx >= N:
#         if SUM < MIN:
#             MIN = SUM
#         return
#
#     if SUM > MIN:
#         return
#     for k in range(0, N):
#         if visited[k] == 0:  # k번째 값에 접근한 적이 없다면
#             SUM += maze[idx][k]
#             # print(SUM, 'sum+= maze')
#             visited[k] = 1
#             count(idx + 1, visited, SUM)
#             visited[k] = 0  # 원상복구
#             SUM -= maze[idx][k]
#             # print(SUM, 'sum -= maze')
#
#
# T = int(input())
# for TC in range(1, T + 1):
#     N = int(input())
#     maze = []
#     for i in range(N):
#         arr = list(map(int, input().split()))
#         maze.append(arr)
#         # print(maze)
#
#     visited = {}
#     for i in range(0, N):
#         visited[i] = 0
#     SUM = 0
#     MIN = 99999
#
#     count(0, visited, SUM)
#
#     print("#%d %d" % (TC, MIN))
