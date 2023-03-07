# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
N = 7
E = 8
adj = [[] for _ in range(N + 1)]

# 인접 리스트 (노드끼리 서로 연결된 노드들을 표시)
arr = list(map(int, input().split()))
for i in range(E):
    a = arr[i * 2]
    b = arr[i * 2 + 1]
    adj[a].append(b)
    adj[b].append(a)

# DFS (재귀호출)
def dfs(visited, start):
    # 기저조건 (종료를 하는 지점)
    if visited[start] == True:
        return
    # 해당 노드를 방문함
    visited[start] = True
    print(f'-{start}', end='')
    # 해당 노드에서 다른 노드의 정점으로 이동
    for nxt_node in adj[start]:
        # 값을 추가해주는 코드
        # ...
        dfs(visited, nxt_node)
        # 값을 복원하는 코드
        # ...


visited = [False for _ in range(N + 1)]
dfs(visited, 1)
# 출력:
# -1-2-3-4-5-7-6