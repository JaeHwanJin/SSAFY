'''
요세푸스 문제는 다음과 같다.
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

출력
예제와 같이 요세푸스 순열을 출력한다.

예제 입력 1
7 3
예제 출력 1
<3, 6, 2, 7, 5, 1, 4>
'''

# N, K = map(int, input().split())
# q = [i for i in range(1, N + 1)]
# result = []
# while len(q) > 0:
#     for i in range(K-1):
#         q.append(q.pop(0))
#     result.append(q.pop(0))
# print('<' + ', '.join(map(str, result)) + '>')

from collections import deque

N, K = map(int, input().split())

# 1부터 N까지의 숫자를 큐에 넣음
q = deque(range(1, N+1))

# 요세푸스 순열을 담을 리스트 초기화
josephus = []

# 큐에 원소가 남아있는 동안 반복
while len(q) > 1:
    # K-1번째까지의 원소를 맨 뒤로 보냄
    for _ in range(K-1):
        q.append(q.popleft())
    # K번째 원소를 제거하고 요세푸스 순열에 추가함
    josephus.append(q.popleft())

# 마지막으로 남은 하나의 원소를 요세푸스 순열에 추가함
josephus.append(q[0])

# 요세푸스 순열을 출력
print('<' + ', '.join(map(str, josephus)) + '>')

