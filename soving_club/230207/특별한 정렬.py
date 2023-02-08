# 문제
'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5
 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

[출력]
 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.

입력
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

출력
#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21
'''
# 풀이
Test_case = int(input())

for tc in range(1, Test_case + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        max_idx = i
        min_idx = i
        for j in range(i, len(arr)): # 가장 큰 값
            if arr[max_idx] < arr[j]:
                max_idx = j
        for k in range(i, len(arr)): # 가장 작은 값
            if arr[min_idx] > arr[k]:
                min_idx = k
        if i % 2 == 0 or i == 0:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f'#{tc}', *arr[:10])

# 내장함수 사용

# T = int(input())
# for i in range(1, T+1):
#     result = [0] * 10
#     num_leng = int(input())
#     num_list = sorted(list(map(int,input().split())))
#     for j in range(10):
#         if j % 2 == 0:
#             result[j] = num_list.pop(-1)
#         else:
#             result[j] = num_list.pop(0)
#     print(f'#{i}',end = ' ')
#     for k in result:
#         print(k, end = ' ')
#     print()




