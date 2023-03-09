'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1
10
5
2
3
1
4
2
3
5
1
7
예제 출력 1
1
1
2
2
3
3
4
5
5
7
'''
# for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리초과가 발생한다.
# 시간과 메모리에 제한을 둔것을 보면 시간과 메모리 관리가 주요 문제이다.
# 파이썬은 내부적으로 연산과 메모리를 관리하기 때문에 파이썬에 내장되어있는 함수들을 적용할수록
# 메모리를 효율적으로 관리할 수 있다고 한다.

## 첫번째 풀이
# num = []
# for i in range(int(input())):
#     num.append(int(input()))
# num.sort()  # sort함수로 정렬
#
# # for문만 사용해서 오름정렬
# # for i in range(len(num)):
# #     for j in range(i + 1, len(num)):
# #         if num[i] > num[j]:
# #             num[i], num[j] = num[j], num[i]
# for j in num:
#     print(j)

## 두번째 풀이
import sys

num = [0] * 100001  # 10,000보다 작거나 같은 자연수리스트를 만들어준다.

for i in range(int(sys.stdin.readline())):
    num[int(sys.stdin.readline())] += 1  # 입력값의 인덱스에 1씩 추가 해준다.

for j in range(10001):
    if num[j] != 0:  # 해당 인덱스의 값이 0 이 아니라면 해당 인덱스를 인덱스의 값만큼 출력해준다.
        for k in range(num[j]):
            print(j)
