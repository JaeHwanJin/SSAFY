'''
어느날 교수님은 문득 회색의 도화지가 필요한 일이 생겼다.
조교A에게 남아있는 100x100 짜리 흰색 도화지에 연구실 비품으로 남아있는
회색 색종이를 붙여서 회색 도화지를 만들라 요청했다.
조교는 한숨을 푹 쉬며, 회색 색종이를 요청한 위치에 붙여서 회색 도화지를 만드려고 했을 때
회색의 영역의 공간의 크기를 출력하시오.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 10 )
다음 줄부터 테스트케이스의 첫 줄에 회색 색종이 개수 N이 주어진다. ( 1 ≤ N ≤ 100 )
다음 줄에 N개의 회색 색종이를 붙이는 좌표 x1, y1, x2, y2가 공백과 함께 한줄씩 주어진다   ( 0 ≤ x1, y1, x2, y2 ≤ 99 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 총 회색 영역의 공간 크기를 출력한다.

입력
3
1
0 0 99 99
3
1 1 10 10
2 2 11 11
3 3 12 12
4
1 1 1 1
2 2 2 2
99 99 99 99
88 88 88 88

출력
#1 10000
#2 138
#3 4
'''
for tc in range(1, T + 1):
    Arr = []
    grid = [[0 for i in range(10)] for j in range(10)]
    # for i in range(10):
    #     arr = []
    #     for j in range(10):
    #         arr.append(0)
    #     Arr.append(arr)
    N = int(input())
    count = 0
    for j in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                grid[x][y] += 1

from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 100 for _ in range(100)]
    Sum = 0
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        arr[x1][y1]
    print(Sum)


