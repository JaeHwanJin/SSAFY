T = 10

for tc in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 100 * 100
    for sj in range(1, 101):
        # 시작지점 찾기.
        si = 0
        if arr[si][sj] != 1:
            continue
        cnt, dj = 0, 0
        ci, cj = si, sj
        while ci < 99:
            cnt += 1
            if dj == 0:
                if arr[ci][cj - 1] == 1: # 좌측
                    dj = -1
                    cj -= 1
                elif arr[ci][cj + 1] == 1: # 우측
                    dj = 1
                    cj += 1
                else:
                    ci += 1
            else:
                if arr[ci][cj + dj] == 1:
                    cj += dj
                else:   # 진행방향이 막힌경우 이대로
                    dj = 0
                    ci += 1
        if mn >= cnt:
            mn, ans = cnt, sj - 1

    print(f'#{tc} {ans}')


import sys

sys.stdin = open('input.txt', 'r')


# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트 케이스가 주어진다.

# 사다리를 탐색 진행(마지막 99에 닿을 때까지) 카운트값을 가져온다
def go(arr, start):
    """
    :param arr: 사다리 이차원 배열
    :param start: 시작 위치
    :return: 사다리 탐색을 진행하면서 걸어온 거리 (카운트값)
    """
    # 출발 지점에서 내려가는 진행을 해줘야한다 (x, y) 좌표로 나타낸다
    # arr[x][y], arr[0][start]
    x, y = 0, start

    # 총 걸어간 거리 (카운트)
    cnt = 0

    # 방향 (아래 방향)
    direction = 0
    # 마지막 99에 닿을 때까지 반복 진행

    while x < 99:
        # 내려가면서 왼쪽 오른쪽이 있는지 확인해준다
        if direction == 0:  # 아랫 방향
            if y > 0 and arr[x][y-1]: # 왼쪽 확인을 하고 있다면 방향 바꿈
                direction = 1
                y = y - 1 # 가로를 한칸 타게 해준다
                cnt += 1
                # continue
            elif y < 99 and arr[x][y+1]: # 오른쪽 확인을 하고 있다면 방향 바꿈
                direction = 2
                y = y + 1  # 가로를 한칸 타게 해준다
                cnt += 1
                # continue
            else: # 아랫 방향으로 계속 진행
                x = x + 1
                cnt += 1
        # 왼쪽 -> , 아래를 확인하면서 내려갈 수 있으면 내려간다. (없다면 왼쪽)
        elif direction == 1:
            if arr[x+1][y]: # 아래를 내려갈 수 있다면 내려간다.
                direction = 0
                x = x+1
                cnt += 1
                # continue
            else: # 그냥 왼쪽으로 계속 간다
                y = y - 1
                cnt += 1
                # continue
        # 오른쪽 <-, 아래를 확인하면서 내려갈 수 있으면 내려간다. (없다면 오른쪽)
        else:  # elif direction == 2:
            if arr[x + 1][y]:  # 아래를 내려갈 수 있다면 내려간다.
                direction = 0
                x = x + 1
                cnt += 1
                # continue
            else: # 그냥 오른쪽으로 계속 간다
                y = y + 1
                cnt += 1
                # continue
    return cnt

for _ in range(10):
    tc = int(input())  # 테스트 케이스
    # 배열을 입력 100 x 100
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 사다리 카운트 최소값을 저장하는 변수
    mn = 100001
    mnIdx = 0
    # 사다리 첫 시작 부분 탐색.
    for i in range(100):
        if arr[0][i] == 1:
            tmp = go(arr, i)
            if mn > tmp:
                mn = tmp
                mnIdx = i


    print(f'#{tc} {mnIdx}')