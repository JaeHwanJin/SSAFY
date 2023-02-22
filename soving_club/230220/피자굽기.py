'''
N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.
1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.
주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.
- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.
3<=N<=20, N<=M<=100, 1<=Ci<=20

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.
입력
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

출력
#1 4
#2 8
#3 6
'''
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = deque(map(int, input().split()))

    for _ in range(len(pizza)):
        pizza[_] = [_ + 1, pizza[_]]
    # print(pizza)

    fp = deque(maxlen=N)
    for _ in range(N):
        fp.append(pizza.popleft())
    # print(fp)

    while len(fp) != 1:
        op = fp.popleft()
        cheese = op[1] // 2
        pn = op[0]
        if cheese != 0:
            fp.append([pn, cheese])
        elif cheese == 0:
            if len(pizza) > 0:
                fp.append(pizza.popleft())
    print(f'#{tc} {fp[0][0]}')




# from collections import deque
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     pizza = deque(map(int, input().split()))
#     PIZZA = deque() # 피자에 index 부여
#     for _ in range(len(pizza)): # 피자에 index 부여
#         PIZZA.append([_ + 1, pizza[_]])
#     fp = deque(maxlen=N)    # 화덕 최댓값 지정
#     for _ in range(N):
#         fp.append(PIZZA.popleft())
#     while len(PIZZA) != 0:  # 화덕에 넣을 피자가 남아있지 않을때까지
#         for i in range(len(fp)):
#             if fp[i][1] == 0:
#                 if len(PIZZA) != 0:
#                     fp[i] = PIZZA.popleft()
#             elif len(PIZZA) != 0:
#                 if fp[i][1] != 0:
#                     fp[i][1] = fp[i][1] // 2
#     MAX = 0
#     result = 0
#     for i in range(len(fp)):
#         if MAX < fp[i][1]:
#             MAX = fp[i][1]
#             result = fp[i][0]
#     print(f'#{tc} {result}')

# from collections import deque
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#
#     pizza = list(map(int, input().split()))
#     pizzas = deque()
#     for i in range(M):
#         pizzas.append([pizza[i], i + 1])
#
#     oven = deque(maxlen=N)
#
#     for _ in range(N):
#         oven.append(pizzas.popleft())
#
#     result = -1
#     while len(oven) > 1:
#         # print('oven: ', oven)
#         # print('pizzas: ', pizzas)
#         peek = oven.popleft()
#         peek_cheese = peek[0] // 2
#         peek_num = peek[1]
#         print(oven)
#         if peek_cheese > 0:
#             oven.append([peek_cheese, peek_num])
#         else:
#             if len(pizzas) > 0:
#                 oven.append(pizzas.popleft())
#
#     print(f'#{test_case} {oven.popleft()[1]}')
