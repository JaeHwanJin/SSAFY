import sys
input = sys.stdin.readline
S = set()
T = int(input())
for i in range(T):
    lst = input().split()
    if len(lst) == 1:
        if lst[0] == 'all':
            S = set([x for x in range(1, 21)])
        else:
            S = set()

    else:
        cmd, x = lst[0], int(lst[1])
        if cmd == 'add':
            S.add(x)
        elif cmd == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif cmd == 'remove':
            if x in S:
                S.discard(x)
        elif cmd == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
