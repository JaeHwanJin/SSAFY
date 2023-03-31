'''
충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오. 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.
다음은 1번에서 출발 5번이 종점인 경우의 예이다.
1번에서 장착한 충전지 용량이 2이므로, 3번 정류장까지 운행할 수 있다. 그러나 2번에서 미리 교체하면 종점까지 갈 수 있다.
마지막 정류장에는 배터리가 없다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 한 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다

입력
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1

출력
#1 1
#2 2
#3 5
'''

# 실패

T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().split()))
    charge, max_charge = N[1], N[1]
    cnt = 0
    for i in range(2, len(N)):
        charge -= 1
        if N[i] > max_charge:
            max_charge = N[i]
        if charge == 0:
            charge = max_charge
            cnt += 1
            print(max_charge)
    print(f'#{tc} {cnt}')


# 성공

# T = int(input())
#
# for tc in range(1, T + 1):
#     arr = list(map(int, input().split()))
#     N = arr[0]
#     charge = [0] + arr[1:]
#     # print(charge)
#
#     # 현재 정류장에서 충전해서 최대 어디까지 갈 수 있는지 저장
#     max_charge = [0 for _ in range(N)]
#     # print(max_charge)
#     for i in range(N):
#         max_charge[i] = i + charge[i]
#     # print(max_charge)
#     cnt = -1  # 1번 정류장에서 장착은 교환횟수에서 제외
#     target = N
#     j = 1
#     while target > 1:
#         if max_charge[j] >= target:
#             cnt += 1
#             target = j
#             j = 1
#         else:
#             j += 1
#     print(f'#{tc} {cnt}')

# 교수님
'''
def dfs(n, cnt, sm):  # n: n번째 정류장 / cnt: 충전 횟수 / sm: 배터리 잔량
    global ans
    # 가지치기 (항상 먹히는 가지치기~~)
    if ans <= cnt:
        return
 
    # 기저조건
    if n == N:
        ans = min(ans, cnt)
        return
 
    # 가지치기를 고려하는 경우: 유망한 답이 먼저 나오는 방향으로 호출!
    # 교체하는 경우
    # n+1: 정류장 하나 이동, cnt+1: 충전횟수 1회 추가, lst[n]-1: lst[n]번째의 정류장 배터리에서 -1
    dfs(n + 1, cnt + 1, lst[n] - 1)
 
    # 교체하지 않는 경우 ( 배터리 잔량이 0보다 클 때만 가능 )
    if sm > 0:
        # n+1: 정류장 하나 이동, cnt: 그대로 유지, sm-1: 배터리 잔량 -1
        dfs(n + 1, cnt, sm - 1)
 
t = int(input())
for tc in range(1, t + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N  # 모든 정류장에서 교체할 경우에는 n번
 
    dfs(2, 0, lst[1] - 1)  # 1번 정류장에서는 교체회수 x, 2번부터 진행할거임
    print(f'#{tc} {ans}')
'''