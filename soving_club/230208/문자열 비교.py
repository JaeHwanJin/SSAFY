Test_case = int(input())

for tc in range(1, Test_case + 1):
    n = input()
    m = input()
    if n in m:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


