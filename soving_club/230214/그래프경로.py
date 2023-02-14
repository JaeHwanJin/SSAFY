'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

출력
#1 1
#2 1
#3 1
'''


# # 1. 그래프 - 인접행렬로 작성하는 방법
# node, edge = map(int, input().split())  # 노드와 간선의 수(정점, 연결선)
#
# # 노드의 갯수가 N, N * N 이차원 배열을 만든다.
# adj = [[0 for _ in range(node)] for _ in range(node)]
#
# # 입력으로 노드간의 연결을 입력으로 받는다 (간선 정보)
# for _ in range(edge):
#     src, dest = map(int, input().split())
#     adj[src][dest] = 1  # src <-> dest 서로 연결점이 있다.
#     adj[dest][src] = 1  # dest <-> src 서로 연결점이 있다.
#
# # 2. 그래프 - 인접리스트로 작성하는 방법(연결 관계만 기록하는 방법)
# # a -> [b, c, f] / b -> [a, f] ....
# # 1. 그래프 - 인접행렬로 작성하는 방법
# node, edge = map(int, input().split())  # 노드와 간선의 수(정점, 연결선)
#
# # 노드의 갯수만큼 빈 리스트를 만든다.
# adj = [[] for _ in range(node)]
#
# for _ in range(edge):
#     src, dest = map(int, input().split())
#     adj[src].append(dest)  # src -> dest 연결 정보를 추가
#     adj[dest].append(src)  # dest -> src 연결 정보를 추가


# 6 5
# 1 4
# 1 3
# 2 3
# 2 5
# 4 6
# 1 6


def check(arr, sl):
    stack.append(sl)
    while stack:
        current = stack.pop()
        visited.append(current)
        for i in arr[current]:
            if i not in visited:
                stack.append(i)


T = int(input())

for tc in range(1, T + 1):
    node, line = map(int, input().split())
    arr = [[] for _ in range(node + 1)]

    for i in range(line):
        sl, el = map(int, input().split())
        arr[sl].append(el)
    S, G = map(int, input().split())
    visited = []
    stack = []

    check(arr, S)

    if G in visited:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


'''
def dfs(graph, visited, start, end):
    # 현재 위치가 목적지면 1 반환, 종료 (기저조건)
    if start == end:
        return True

    # 현재 위치 방문 체크
    visited[start] = True

    # 현재 위치와 연결된 모든 노드 탐색
    for nxt in graph[start]:
        # 연결된 노드의 방문 여부 확인
        if visited[nxt] == False:
            # 들어갈 노드 방문 체크 해주고 재귀 호출
            visited[nxt] = True
            r = dfs(graph, visited, nxt, end)
            # 목적지에 도달해서 반환받은 1로 종료
            if r == True:
                return True

    return False


T = int(input())
for tc in range(1, T + 1):
    # 정점 갯수와 간선의 갯수 입력
    V, E = map(int, input().split())

    # 인접 리스트를 생성하는데...
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        s, e = map(int, input().split())
        graph[s].append(e) # 단방향 그래프라서 s -> e

    # S -> ... -> G 연결하는 경로가 있는가...?
    S, G = map(int, input().split())

    # 방문 체크할 배열 생성
    visited = [False] * (V + 1)

    # 목적지 도달했는지 여부로 결과 출력
    result = dfs(graph, visited, S, G)
    if result == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
'''