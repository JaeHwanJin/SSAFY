T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    max_sum = 0
    min_sum = 1000000
    for j in range(N - M + 1):
        SUM = 0
        for l in range(M):
            SUM += ai[j:j + M][l]
        if SUM > max_sum:
            max_sum = SUM
        if SUM < min_sum:
            min_sum = SUM
    print(f'#{i + 1} {max_sum - min_sum}')