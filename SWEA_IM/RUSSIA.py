'''
2016년은 삼성전자가 러시아 현지법인을 설립한지 20주년이 된 해이다. 이를 기념해서 당신은 러시아 국기를 만들기로 했다.
먼저 창고에서 오래된 깃발을 꺼내왔다. 이 깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 파란색, 빨간색 중 하나로 칠해져 있다.
당신은 몇 개의 칸에 있는 색을 다시 칠해서 이 깃발을 러시아 국기처럼 만들려고 한다. 다음의 조건을 만족해야 한다.
위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.
이렇게 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 두 정수 N,M(3≤N,M≤50)이 공백으로 구분되어 주어진다.
다음 N개의 줄에는 M개의 문자로 이루어진 문자열이 주어진다. i번 째 줄의 j번째 문자는 깃발에서 i번째 행 j번째 열인 칸의 색을 의미한다.
‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색을 의미한다. ‘W’, ‘B’, ‘R’외의 다른 문자는 입력되지 않는다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여 T 줄에 걸쳐서 출력한다.

입력
2   //Test Case 수
4 5 //N=4, M=5
WRWRW
BWRWB
WRWRW
RWBWR
6 14    //N=6, M=14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW

출력
#1 11
#2 44
'''
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 행렬의 크기 3~50
    russia = [list(input()) for _ in range(N)]
    MIN = N * M
    wcnt = 0
    for w in range(0, N - 2): # 파랑색과 빨강색으로 변경할 줄 빼고
        for i in range(M):
            if russia[w][i] != 'W':
                wcnt += 1
        bcnt = 0
        for b in range(w+1, N-1): # 흰색으로 변경한 한 줄 빼고 / 빨강색으로 변경 할 한 줄 빼고
            for i in range(M):
                if russia[b][i] != 'B':
                    bcnt += 1
            rcnt = 0
            for r in range(b+1, N):
                for i in range(M):
                    if russia[r][i] != 'R':
                        rcnt += 1
            SUM = wcnt + bcnt + rcnt
            if MIN > SUM:
                MIN = SUM
    print(f'#{tc} {MIN}')



# wcnt = 0
# for w in range(0, n - 2):  # 화이트
#     for k in range(0, m):
#         if arr[w][k] != 'W':z
#             wcnt += 1
#
#     bcnt = 0
#     for b in range(w + 1, n - 1):  # 블루
#         for k in range(0, m):
#             if arr[b][k] != 'B':
#                 bcnt += 1
#
#         rcnt = 0
#         for r in range(b + 1, n):  # 레드
#             for k in range(0, m):
#                 if arr[r][k] != 'R':
#                     rcnt += 1
#
#         SUM = wcnt + bcnt + rcnt
#         if mymin > SUM:
#             mymin = SUM
# print(f'#{tc} {mymin}')
