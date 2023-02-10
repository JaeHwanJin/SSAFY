from pprint import pprint

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    # print(a)
    lst = [[0] * N for i in range(N)]
    print(a)
    print(lst)

    print(lst)

