'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjm = [[0] * (V + 1) for _ in range(V + 1)]
adjl = [[] for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]  # 1 2 / 1 3 한쌍씩 가져오기위함
    adjm[v1][v2] = 1
    adjm[v2][v1] = 1

    adjl[v1].append(v2)
    adjl[v2].append(v1)
d