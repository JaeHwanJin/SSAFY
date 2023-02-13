'''
다음과 같이 두 개의 숫자 N, M이 주어질 때, N의 M 거듭제곱 값을 구하는 프로그램을 재귀호출을 이용하여 구현해 보아라.
2 5 = 2 X 2 X 2 X 2 X 2 = 32
3 6 = 3 X 3 X 3 X 3 X 3 X 3 = 729

[제약 사항]
총 10개의 테스트 케이스가 주어진다.
결과 값은 Integer 범위를 넘어가지 않는다.

[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄에는 두 개의 숫자가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

입력
1
9 8
2
2 8

출력
#1 43046721
#2 256
'''

for _ in range(10):
    tc = int(input()) # 테스트 케이스 번호
    a, b = map(int, input().split())

    def test(a, b):
        return f'#{tc} {a ** b}'# a의 b제곱값 출력
    print(test(a, b))


