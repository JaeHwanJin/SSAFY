<<<<<<< HEAD
# -*- coding: utf-8 -*-
'''
직사각형 모양의 종이가 있다. 이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다.
가로 점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고, 세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.
점선을 따라 이 종이를 칼로 자르려고 한다. 가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지,
세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다.
입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.

입력
첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. 가로와 세로의 길이는 최대 100㎝이다. 둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 세로로 자르는 점선은 1과 점선 번호가 주어진다. 입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.

출력
첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.

입력
10 8
3
0 3
1 4
0 2
출력
30
'''

row, col = map(int, input().split())  # 가로와 세로의 길이
l = [0]  # 가로 변길이를 담을 리스트
h = [0]  # 세로 변길이를 담을 리스트
n = int(input())
for tc in range(n):
    a, b = map(int, input().split())
    if a == 0:
        h.append(b)
    else:
        l.append(b)
l.append(row)
h.append(col)
l.sort()
h.sort()
L = 0
H = 0
for i in range(0, len(l) - 1):
    a = l[i + 1] - l[i]  # 정렬 된 리스트내에서 근접한 변수의차이 = 가로변의 길이
    if L < a:
        L = a
for j in range(0, len(h) - 1):  # 정렬 된 리스트내에서 근접한 변수의차이 = 세로변의 길이
    b = h[j + 1] - h[j]
    if H < b:
        H = b
print(L * H)
=======
# -*- coding: utf-8 -*-
'''
직사각형 모양의 종이가 있다. 이 종이는 가로방향과 세로 방향으로 1㎝마다 점선이 그어져 있다.
가로 점선은 위에서 아래로 1번부터 차례로 번호가 붙어 있고, 세로 점선은 왼쪽에서 오른쪽으로 번호가 붙어 있다.
점선을 따라 이 종이를 칼로 자르려고 한다. 가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지,
세로 점선인 경우는 위쪽 끝에서 아래쪽 끝까지 한 번에 자른다.
입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.

입력
첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다. 가로와 세로의 길이는 최대 100㎝이다. 둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 세로로 자르는 점선은 1과 점선 번호가 주어진다. 입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.

출력
첫째 줄에 가장 큰 종이 조각의 넓이를 출력한다. 단, 넓이의 단위는 출력하지 않는다.

입력
10 8
3
0 3
1 4
0 2
출력
30
'''

row, col = map(int, input().split())  # 가로와 세로의 길이
l = [0]  # 가로 변길이를 담을 리스트
h = [0]  # 세로 변길이를 담을 리스트
n = int(input())
for tc in range(n):
    a, b = map(int, input().split())
    if a == 0:
        h.append(b)
    else:
        l.append(b)
l.append(row)
h.append(col)
l.sort()
h.sort()
L = 0
H = 0
for i in range(0, len(l) - 1):
    a = l[i + 1] - l[i]  # 정렬 된 리스트내에서 근접한 변수의차이 = 가로변의 길이
    if L < a:
        L = a
for j in range(0, len(h) - 1):  # 정렬 된 리스트내에서 근접한 변수의차이 = 세로변의 길이
    b = h[j + 1] - h[j]
    if H < b:
        H = b
print(L * H)
>>>>>>> b2acc9c228201052bf05820050910e4f96064e7d
