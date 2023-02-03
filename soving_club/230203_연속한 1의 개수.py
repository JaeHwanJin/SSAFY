T = int(input())

for i in range(1, T + 1):
    N = int(input())
    number = list(map(int, input()))
    cnt = 0
    x = 0
    List = []
    for j in range(N):
        if 1 == number[j]:
            cnt += 1
            x = cnt
            List.append(x)
        if 0 == number[j]:
            cnt = 0

    for k in range(len(List)-1):
        if x < List[k]:
            x = List[k]

    print(f'#{i} {x}')
