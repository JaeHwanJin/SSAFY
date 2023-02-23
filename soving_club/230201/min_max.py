# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오

# 첫 줄에 테스트 케이스 개수 T가 주어진다.
T = int(input())

for i in range(1, T + 1):
    # 다음 주부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다.
    N = int(input())
    # 다움 줄에 N개의 숫자 ai가 여백없이 주어진다.
    ai = list(map(int, input()))
    cnt = [0] * 10
    for k in ai:
        cnt[k] += 1
    x = cnt[0]
    for j in range(len(cnt)):
        if x <= cnt[j]:
            x = cnt[j]
            idx = j

    # 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
    print(f'#{i} {idx} {x}')


# -----------------------------------------------------#
#   2023 - 02 - 23 복습#
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
T = int(input())
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
for tc in range(1, T + 1):
    N = int(input())
    # 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
    ai = list(map(int, input().split()))
    MAX = 0 # 가장 큰 수를 담을 변수
    MIN = 1000001 # 가장 작은 수를 담을 변수 ai의 크기가 1 이상 1000000이하 이기때문에
    for i in range(len(ai)):
        if MAX < ai[i]: # ai리스트 안의 값들을 비교해서 MAX 구하기
            MAX = ai[i]
        if MIN > ai[i]: # ai리스트 안의 값들을 비교해서 MIN 구하기
            MIN = ai[i]
    print(f'#{tc} {MAX - MIN}')