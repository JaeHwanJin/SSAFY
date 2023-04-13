from collections import deque


def dfs(graph, v, visited):
    # v는 시작위치
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 노드를 재귀적으로 호출
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 7],
    [1, 4, 6],
    [1, 5, 7],
    [2, 6],
    [3, 7],
    [2, 4],
    [1, 3]
]

# 각 노드가 방문한 정보를 리스트 자료형으로 표현
visited = [False] * 9

print("방문순서")
dfs(graph, 1, visited)