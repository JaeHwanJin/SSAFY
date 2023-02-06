from pprint import pprint

N, M = map(int, input().split())

for i in range(N):
    m = input()
    result = m[::-1]
    print(result)




'''
[입력]
9 0 0 18 0 0
9 0 1 18 0 0
12 14 52 12 15 30
'''

'''
[출력]
9 0 0
8 59 59
0 0 38
'''
