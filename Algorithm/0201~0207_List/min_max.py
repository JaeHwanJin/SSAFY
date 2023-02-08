# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

# 첫 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

for i in range(1, T + 1):
    # 각 케이스의 첫 줄에 양수의 개수 N이 주어진다.
    N = int(input())

    # 다음 줄에 N개의 양수 number이 주어진다.
    number = list(map(int, input().split()))
    maxV = number[0]
    minV = number[0]

    for j in range(N - 1):
        if maxV < number[j + 1]:
            maxV = number[j + 1]
    print(f'maxV = {maxV}')

    for j in range(N - 1):
        if minV > number[j + 1]:
            minV = number[j + 1]
    print(f'minV = {minV}')

    print(f'#{i} {maxV - minV}')


