'''
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.
노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
두 노드 S와 G가 서로 연결되어 있지 않다면, 0을 출력한다.

입력
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
1 9

출력
#1 2
'''
from collections import deque


# BFS : start 노드를 시작해서 end 노드에 도착할 때 까지 간선수를 반환
# 다음 노드로 건너갈 때 마다 카운트를 1씩....
def bfs(start, end):
    # 방문체크를 하기 위한 배열
    visited = [False for _ in range(V + 1)]
    # 1. 결과 배열을 만들어서 진행.
    # results = [0 for _ in range(V + 1)]
    # 큐
    Queue = deque()
    Queue.append(start)
    visited[start] = True
    results[start] = 0

    while Queue:
        node = Queue.popleft()
        # 해당 노드에서 다른 인접한 노드로 건너갈 수 있는 것들을 탐색
        for nxt_node in adj[node]:
            # 방문 체크를 먼저 해줘야 한다
            if visited[nxt_node] == False:
                Queue.append(nxt_node)
                visited[nxt_node] = True
                results[nxt_node] = results[node] + 1  # 이전 노드 간선 갯수 +1

    # BFS 탐색이 종료 된것이기 때문에..
    return results[end]


# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
T = int(input())
for tc in range(1, T + 1):
    # 다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
    V, E = map(int, input().split())
    # 인접 리스트 : a 정점노드에서 연결되어 있는 노드들을 리스트에 넣는 것.
    # a : 1 -> 2, 3, 5
    adj = [[] for _ in range(V + 1)]  # 인덱스가 1부터 시작하기때문에 +1해준다. 0은 버림
    # 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
    for _ in range(E):
        # 간선 정보의 입력을 받는 코드
        a, b = map(int, input().split())
        adj[a].append(b)  # a -> b
        adj[b].append(a)  # b -> a
        # E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.
        S, G = map(int, input().split())

        # BFS 탐색해서 S -> .... -> G 의 간선 갯수를 출력한다.
        result = bfs(S, G)
        print(f'#{tc} {result}')
