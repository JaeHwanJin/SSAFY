T = int(input())  # 테스트 케이스

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    r, c = map(int, input().split())  # 망치의 시작 위치
    time = 0
    score = 0
    for i in range(N):
        A, B, K = list(map(int, input().split()))  # 두더지의 좌표, 두더지가 머무르는 시간
        while K > 0:
            for x in range(abs(r - A)):
                for y in range(abs(c - B)):
                    time += 1
                    K -= 1
            r = r - A
            c = c - B
            # print(K, time)
            if K == time:
                score += 1
                break
    print(f'#{tc} {score}')


