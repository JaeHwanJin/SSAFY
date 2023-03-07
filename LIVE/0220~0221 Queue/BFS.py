# import heapq
#
# # 리스트를 힙으로 변환
# list1 = [3, 7, 1, 9, 2, 5]
# heapq.heapify(list1)
# print(list1)  # [1, 2, 5, 9, 7, 3]
#
# # 힙에서 가장 작은 값 삭제 및 반환
# min_val = heapq.heappop(list1)
# print(min_val)  # 1
# print(list1)  # [2, 7, 5, 9, 3]
#
# # 힙에 값 추가
# heapq.heappush(list1, 4)
# print(list1)  # [2, 4, 5, 9, 7, 3]
#
# # 힙에서 가장 작은 값 반환 (삭제하지 않음)
# min_val = heapq.heappushpop(list1, 1)
# print(min_val)  # 1
# print(list1)  # [1, 4, 5, 9, 7, 3]
#
# # 힙의 n번째 작은 값 반환 (삭제하지 않음)
# n = 3
# n_val = heapq.nsmallest(n, list1)[-1]
# print(n_val)  # 5
#
# # 힙의 n번째 큰 값 반환 (삭제하지 않음)
# n = 2
# n_val = heapq.nlargest(n, list1)[-1]
# print(n_val)  # 7

# 파이썬 우선순위 큐 (priority queue, min-heap) 만들어서 사용하는 방법
# - heapq.heapify(list): 리스트를 힙으로 변환합니다.
# - heapq.heappop(heap): 힙에서 가장 작은 값을 삭제 및 반환합니다.
# - heapq.heappush(heap, item): 힙에 값을 추가합니다.
# - heapq.heappushpop(heap, item): 힙에 값을 추가한 후 가장 작은 값을 삭제 및 반환합니다.
# - heapq.nsmallest(n, iterable): iterable에서 n개의 가장 작은 값을 반환합니다.
# - heapq.nlargest(n, iterable): iterable에서 n개의 가장 큰 값을 반환합니다.

# # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# N = 7
# E = 8
# adj = [[] for _ in range(N + 1)]
#
# # 인접 리스트 (노드끼리 서로 연결된 노드들을 표시)
# arr = list(map(int, input().split()))
# for i in range(E):
#     a = arr[i * 2]
#     b = arr[i * 2 + 1]
#     adj[a].append(b)
#     adj[b].append(a)
#     # print(f'a = {a}')
#     # print(f'b = {b}')
#     # print(adj)
#
#
# # BFS
# def bfs(start):
#     # BFS, 큐
#     queue = []
#     # 방문 체크
#     visited = [False for _ in range(N + 1)]
#     queue.append(start)
#     visited[start] = True
#
#     # 반복을 진행하는데... 큐가 빌때까지
#     while queue:
#         node = queue.pop(0)
#         # node 탐색하는 추가 로직...
#         # ....
#         print(f'-{node}', end='')
#         for nxt_node in adj[node]:
#             if visited[nxt_node] == False:
#                 queue.append(nxt_node)
#                 visited[nxt_node] = True
#
#
# bfs(1)
# 출력:
# -1-2-3-4-5-7-6


# # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# N = 7
# E = 8
# adj = [[] for _ in range(N + 1)]
#
# # 인접 리스트 (노드끼리 서로 연결된 노드들을 표시)
# arr = list(map(int, input().split()))
# for i in range(E):
#     a = arr[i * 2]
#     b = arr[i * 2 + 1]
#     adj[a].append(b)
#     adj[b].append(a)
#
# # DFS (재귀호출)
# def dfs(visited, start):
#     # 기저조건 (종료를 하는 지점)
#     if visited[start] == True:
#         return
#     # 해당 노드를 방문함
#     visited[start] = True
#     print(f'-{start}', end='')
#     # 해당 노드에서 다른 노드의 정점으로 이동
#     for nxt_node in adj[start]:
#         # 값을 추가해주는 코드
#         # ...
#         dfs(visited, nxt_node)
#         # 값을 복원하는 코드
#         # ...
#
#
# visited = [False for _ in range(N + 1)]
# dfs(visited, 1)
# # 출력:
# # -1-2-3-4-5-7-6

# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
N = 7
M = 8
adj = [[] for _ in range(N + 1)]
arr = list(map(int, input().split()))

for i in range(N + 1):
    a = arr[i * 2]
    b = arr[i * 2 + 1]
    adj[a].append(b)
    adj[b].append(a)


def bfs(start):
    Queue = []
    visited = [False for _ in range(N)]
    visited[start] = True
    Queue.append(start)
    while Queue:
        node = Queue.pop(0)
        print(f'-{node}', end=' ')
        for i in adj[node]:
            if visited[i] == False:
                visited[i] = True
                Queue.append(i)


bfs(1)
