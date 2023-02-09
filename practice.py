from pprint import pprint
import sys

row1, col1 = map(int, input().split())
row2, col2 = map(int, input().split())
row3, col3 = map(int, input().split())
x = 0
y = 0
if row1 == row2:
    x = row3
elif row2 == row3:
    x = row1
else:
    x = row2

if col1 == col2:
    y = col3
elif col2 == col3:
    y = col1
else:
    y = col2

print(x, y)
