'''
트리의 일부를 서브 트리라고 한다. 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.
이런 경우의 트리는 부모 노드를 인덱스로 다음과 같은 방법으로 나타낼 수 있다. 자식 노드가 0인 경우는 노드가 자식이 없는 경우이다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

입력
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10

출력
#1 3
#2 1
#3 3
'''

T = int(input())


def VLR(node):
    global cnt
    if node != 0:
        cnt += 1
        VLR(left[node])
        VLR(right[node])


def LVR(node):
    global cnt
    if node != 0:
        LVR(left[node])
        cnt += 1
        LVR(right[node])


def LRV(node):
    global cnt
    if node != 0:
        LRV(left[node])
        LRV(right[node])
        cnt += 1


for tc in range(1, T + 1):
    E, N = map(int, input().split())
    left = [0 for _ in range(E + 2)]
    right = [0 for _ in range(E + 2)]
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(0, len(arr), 2):
        P, C = arr[i], arr[i + 1]
        # print(P, C)
        if left[P] == 0:
            left[P] = C
        else:
            right[P] = C
    LRV(N)
    print(f'#{tc} {cnt}')
    # print(left)
    # print(right)
