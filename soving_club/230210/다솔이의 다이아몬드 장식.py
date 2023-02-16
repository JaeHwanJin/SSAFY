'''
다솔이는 어떤 문자열을 하나 가지고 있는데, 이 문자열이 별로 아름답지 못하다고 생각하고 있다.
그래서 장식을 해주기로 했다.
예를 들어 문자열이 “D”라면 주위를 ‘#’로 이루어진 다이아몬드로 감싸서 다음과 같이 5x5크기로 장식한다.
빈 곳은 ‘.’로 표시한다.
만약 문자열의 길이가 1보다 더 크면, 인접한 문자는 ‘#’과 ‘.’을 공유하여 장식한다.
예를 들어 문자열이 “APPLE”이면 다음과 같이 장식한다
주어진 문자열을 장식해주는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 길이가 1이상 50이하인 문자열이 주어진다.

[출력]
각 테스트 케이스마다 다섯 줄에 걸쳐 장식된 문자열을 출력한다.

입력
2       // TC의 개수
D       // 첫번째 TC의 문자열
APPLE   // 두번째 TC의 문자열

출력

..#..
.#.#.
#.D.#
.#.#.
..#..

..#...#...#...#...#..
.#.#.#.#.#.#.#.#.#.#.
#.A.#.P.#.P.#.L.#.E.#
.#.#.#.#.#.#.#.#.#.#.
..#...#...#...#...#..
'''

T = int(input())

start = end = ['.', '.', '#', '.', '.']

second = fourth = ['.', '#', '.', '#', '.']

third = ['#', '.', '', '.', '#']
storage = ''
for tc in range(1, 1 + T):
    string = input().strip()
    result = []
    # 글자 수만큼 first, second, third, fourth 를 반복적으로 출력할 리스트에 추가합니다.
    for i in range(len(string)):
        result.append(start)
        result.append(second)
        tmp = third[:]
        # 기존값을 출력할 글자로 대체합니다.
        tmp[2] = string[i]
        result.append(tmp)
        result.append(fourth)
    # 마지막에 뚜껑을 닫아줍니다.
    result.append(end)

    output = [[0] * len(result) for _ in range(len(result[0]))]
    # 아래로 길게 늘어진 데이터를 왼쪽으로 90도 회전에서 저장
    for r in range(len(result)):
        for c in range(len(result[0])):
            output[-c - 1][r] = result[r][c]

    for i in range(len(output)):
        storage += ''.join(output[i]) + '\n'
print(storage)