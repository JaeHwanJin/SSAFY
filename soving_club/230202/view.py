import sys

sys.stdin = open('input.txt', 'r')

# 총 10개의 테스트 케이스가 주어진다
for tc in range(1, 11):  # 1~10

    # 각 테스트케이스의 첫 번째 줄에는 건물의 개수 N이 주어진다.
    n = int(input())
    # 그 다음 줄에는 N개의 건물의 높이가 주어진다.
    buildings = list(map(int, input().split()))

    result = 0  # 나중에 사용 할 결과 값
    # 빌딩을 순회한다 i : [2, n-2]
    for i in range(2, n - 2):
        # 1번 방법
        # 두칸까지 빌딩 높이차가 몇인지 확인 : b[i-2], b[i-1] (), b[i+1], b[i+2] 빌딩의 높이 차를 확인한다.
        # diff1 = buildings[i] - buildings[i - 2]
        # diff2 = buildings[i] - buildings[i - 1]
        # diff3 = buildings[i] - buildings[i + 1]
        # diff4 = buildings[i] - buildings[i + 2]
        # # 높이차가 이 중에서 0 초과로 되어야만 조망권이 확보된다. (조건식)
        # if diff1 > 0 and diff2 > 0 and diff3 > 0 and diff4:
        #     # 높이차 중에서 가장 작은 값을 카운트 하면 된다.
        #     result += min(diff1, diff2, diff3, diff4)

        # 2번 방법
        # 비교할 빌딩 중에 가장 높은 빌딩을 찾아서 조망권이 있는지 확인
        mx = max(buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2])
        if buildings[i] > mx:
            result += buildings[i] - mx
    print(f'#{tc} {result}')



