'''
통계학
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	133835	30335	24315	25.537%
문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

예제 입력 1
5
1
3
8
-2
2
예제 출력 1
2
2
1
10
예제 입력 2
1
4000
예제 출력 2
4000
4000
4000
0
예제 입력 3
5
-1
-2
-3
-1
-2
예제 출력 3
-2
-2
-1
2
예제 입력 4
3
0
0
-1
예제 출력 4
0
0
0
1
'''

### 1번째 풀이
# import sys
#
# num = []
# for inp in range(int(sys.stdin.readline().strip())):
#     num.append(int(sys.stdin.readline().strip()))  # 입력 값 리스트에 추가
#
# num.sort()  # 리스트 오름차순 정렬
#
# print(round(sum(num) / len(num)))  # 산술평균
# print(num[len(num) // 2])  # 중앙값
#
# mode = []  # 숫자와 빈도수를 담을 list
# for i in range(len(num)):
#     mode.append((num[i], num.count(num[i])))
# mode = list(set(mode))  # 중복값 제거
# mode = sorted(mode, key=lambda x: x[0])  # N개의 수 들이 각각 몇번 나타나는지 기준으로 정렬
# MAX = max(mode, key=lambda x: x[0])[1]  # 빈도수가 가장 높은 값
# cnt = 0
# result = []  # 최빈값을 담을 list
# for x, y in mode:
#     if y == MAX:
#         cnt += 1
#         result.append((x, y))  # 최빈값이 다수 일 경우
# if cnt == 1:
#     print(MAX)
# else:
#     print(result[1][0])
#
# print(max(num) - min(num))  # 범위 : 최댓값과 최솟값의 차이

# 시간초과로인해 실패
# 최빈값을 구하는데 너무 많음 함수를 사용했다.

import sys

num = []
for inp in range(int(sys.stdin.readline().strip())):
    num.append(int(sys.stdin.readline().strip()))  # 입력 값 리스트에 추가

num.sort()  # 리스트 오름차순 정렬

print(round(sum(num) / len(num)))  # 산술평균
print(num[len(num) // 2])  # 중앙값

mode = dict()
for i in num:
    if i in mode:
        mode[i] += 1
    else:
        mode[i] = 1
MAX = max(mode.values())  # 최빈값
MAX_dic = []  # 최빈값을 저장 할 list

for j in mode:
    if MAX == mode[j]:
        MAX_dic.append(j)

if len(MAX_dic) > 1:  # 최빈값이 여러개라면
    print(MAX_dic[1])  # 두번째로 작은 값
else:
    print(MAX_dic[0])   # 최빈값

print(max(num) - min(num))  # 범위 : 최댓값과 최솟값의 차이
