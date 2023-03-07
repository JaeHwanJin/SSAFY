# 첫 입력값이 정점의 개수
N = int(input())  # 13

# 왼쪽 자식 배열
left = [0 for _ in range(N + 1)]  # [0] * (N+1)
# 오른쪽 자식 배열
right = [0 for _ in range(N + 1)]

# 부모 - 자식
arr = list(map(int, input().split()))  # [부모1, 자식1, 부모2, 자식2 ,...]
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

# 부모 자식을 순회하면서 왼쪽, 오른쪽 자식을 넣어주는 과정...
for i in range(0, len(arr), 2):
    # 부모 i, 자식 i+1
    p, c = arr[i], arr[i + 1]
    # 왼쪽 자식이 있는지 여부 -> 없다면 왼쪽에 자식 할당
    if left[p] == 0:
        left[p] = c
    # -> 있다면.. 오른쪽에 할당
    else:
        right[p] = c
print(left)
print(right)
# 카운트 변수 (전역)
count = 0


# 순회... VLR 전위순회, 서브트리에 포함되는 노드의 갯수
def VLR(t):
    global count
    if t != 0:
        count += 1  # V
        VLR(left[t])  # L 왼쪽
        VLR(right[t])  # R 오른쪽


VLR(3)
print(count)

count = 0


def LVR(t):
    global count
    if t != 0:
        LVR(left[t])  # L 왼쪽
        count += 1  # V
        LVR(right[t])  # R 오른쪽


LVR(3)
print(count)

count = 0


def LRV(t):
    global count
    if t != 0:
        LRV(left[t])  # L 왼쪽
        LRV(right[t])  # R 오른쪽
        count += 1  # V


LRV(3)
print(count)