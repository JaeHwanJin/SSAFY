'''
나이순 정렬

문제
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

출력
첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

예제 입력 1
3
21 Junkyu
21 Dohyun
20 Sunyoung
예제 출력 1
20 Sunyoung
21 Junkyu
21 Dohyun
'''

## 1번째 풀이
import sys

N = int(input())
result = []
num = 1
for i in range(N):
    age, name = sys.stdin.readline().split()
    result.append([age, name, num]) # age가 같을때 등록한 순으로 정렬하기 위해 등록번호 부여
    num += 1

result = sorted(result, key=lambda x: [x[0], x[2]]) # age 등록번호 순으로 정렬

for j in range(len(result)):
    print(*result[j][:2])   # 등록번호 빼고 age와 name 출력

# 왜 실패인지 모르겠다... 알려주세요 고수님들...



## 2번째 풀이
import sys

N = int(input())
result = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    result.append([age, name])

result = sorted(result, key=lambda x: x[0])

for j in result:
    print(*j)

### 구글링을 통해 알아보니 append때문에 자동으로 등록된 순으로 들어가는 걸 깨달았다....
### age만 기준으로 정렬해줬지만 실패..


## 3번째 풀이
N = int(input())
result = []
for i in range(N):
    age, name = map(str, input().split())
    result.append([int(age), name])

result = sorted(result, key=lambda x: x[0])

for j in result:
    print(*j)

### 성공!
### 사실 2번째 풀이와 3번째 풀이의 차이점에 대해 모르겠다.
### 2번째 풀이에 strip를 통해 개행문자를 제거 해줘도 똑같이 실패했다..
### input과 sys의 차이점을 명확히 알고 사용해야겠다.

### 1번째와 2번째 틀린 이유
### sys를 통해 입력을 받았기때문에 age를 int로 감싸줘야하는데 그러지 않아서 실패했던 것이었다...