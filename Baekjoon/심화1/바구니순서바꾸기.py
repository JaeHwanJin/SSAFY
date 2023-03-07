'''
도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다. 바구니는 일렬로 놓여져 있고, 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다.
도현이는 앞으로 M번 바구니의 순서를 회전시키려고 만들려고 한다. 도현이는 바구니의 순서를 회전시킬 때, 순서를 회전시킬 범위를 정하고, 그 범위 안에서 기준이 될 바구니를 선택한다. 도현이가 선택한 바구니의 범위가 begin, end이고, 기준이 되는 바구니를 mid라고 했을 때, begin, begin+1, ..., mid-1, mid, mid+1, ..., end-1, end 순서로 되어있는 바구니의 순서를 mid, mid+1, ..., end-1, end, begin, begin+1, ..., mid-1로 바꾸게 된다.
바구니의 순서를 어떻게 회전시킬지 주어졌을 때, M번 바구니의 순서를 회전시킨 다음, 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
둘째 줄부터 M개의 줄에는 바구니의 순서를 바꾸는 만드는 방법이 주어진다. 방법은 i, j, k로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 회전시키는데, 그 때 기준 바구니는 k번째 바구니라는 뜻이다. (1 ≤ i ≤ k ≤ j ≤ N)
도현이는 입력으로 주어진 순서대로 바구니의 순서를 회전시킨다.

출력
모든 순서를 회전시킨 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.

예제 입력 1
10 5
1 6 4
3 9 8
2 10 5
1 3 3
2 6 2
예제 출력 1
1 4 6 2 3 7 10 5 8 9
'''
# 문제를 잘 읽고 또 완전히 숙지 후 풀이
# mid~end의 인덱스의 값을 변경해야하는데 mid~end 값을 위치변경했음...
# N, M = map(int, input().split())
# num = []
# for i in range(0, N + 1):  # list의 index는 0부터 시작하기때문에
#     num.append(i)
# for j in range(M):
#     st, end, mid = map(int, input().split())
#     cnt = 0
#     for k in range(mid, end + 1):
#         for l in range(len(num)):
#             if k == num[l]:
#                 del num[l]
#                 num.insert(st + cnt, k)
#                 cnt += 1
# print(*num[1:])


# N, M = map(int, input().split())
# buckets = []
# for i in range(0, N + 1):  # list의 index는 0부터 시작하기때문에
#     buckets.append(i)
# for j in range(M):
#     st, end, mid = map(int, input().split())
#     cnt = 0
#     for k in range(mid, end + 1):  # mid부터 end index의 값 찾아서 위치 변경
#         NUM = buckets[k]
#         del buckets[k]
#         buckets.insert(st + cnt, NUM)
#         cnt += 1
# print(*buckets[1:])

# 좀 더 간단하게
# N, M = map(int, input().split())
# buckets = [i for i in range(0, N + 1)]  # list의 index는 0부터 시작하기때문에
#
# for _ in range(M):
#     i, j, k = map(int, input().split())
#     i, j, k = i, j, k
#     # 리스트 연산 가능한 점을 이용
#     buckets = buckets[:i] + buckets[k:j + 1] + buckets[i:k] + buckets[j + 1:]
# print(*buckets[1:])
