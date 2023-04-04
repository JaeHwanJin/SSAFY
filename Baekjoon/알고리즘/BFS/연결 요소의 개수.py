'''
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1
2
예제 입력 2
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2
1
'''
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # 정점의 개수 N, 간선의 개수 M
graph = [[0] * (N + 1) for _ in range(N + 1)]  # 각 정점에 연결된 다른 점들

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (N + 1)  # 이미 방문한 점


def BFS(v):
    if visited[v] == 0:
        q = deque()
        q.append(v)
        visited[v] = 1
        while q:
            v = q.popleft()
            for i in range(1, N + 1):
                if graph[v][i] == 1 and not visited[i]:
                    q.append(i)
                    visited[i] = 1


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        BFS(i)
        cnt += 1

print(cnt)
