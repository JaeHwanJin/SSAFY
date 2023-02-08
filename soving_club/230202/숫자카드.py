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