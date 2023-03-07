# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
T = int(input())
for tc in range(1, T + 1):
    # 다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100
    N, string = input().split()
    N = int(N)
    # 16진수 A부터 F는 대문자로 표시된다.
    # 0 ~ 15, 0 ~ 'F'
    # 1. 16진수 -> 2 진수 테이블...
    # hex_to_bin = {
    #     '0': '0000',
    #     '1': '0001',
    #     '2': '0010',
    #     '3': '0011',
    #     '4': '0100',
    #     '5': '0101',
    #     '6': '0110',
    #     '7': '0111',
    #     '8': '1000',
    #     '9': '1001',
    #     'A': '1010',
    #     'B': '1011',
    #     'C': '1100',
    #     'D': '1101',
    #     'E': '1110',
    #     'F': '1111',
    # }
    #
    # result = ''
    # for ch in string:
    #     # result += hex_to_bin.get(ch)
    #     result += hex_to_bin[ch]

    # 2. 직접 계산해서 하는 방법
    # 16진수 문자열을 하나씩 때어내서...
    # 해당되는 숫자.. 0~9 ABCDEF
    # 해당되는 2진수 값으로 직접 변환...
    hex_table = '0123456789ABCDEF'
    result = ''
    for ch in string:
        digit = hex_table.find(ch) # 문자 하나를 십진수로...
        # 십진수 -> 이진수 (네자리를...)
        for i in range(4):
            digit, mod = divmod(digit, 2)
            result += str(mod)

    print(f'#{tc} {result}')

# N진수 -> 10진수
string = input() # N진수를 문자열로 받았다..
print(int(string, 6))

# 10진수 -> N-진수...
def convert(num, N):
    s = ''
    t = '0123456789ABCDEF'

    # num의 값이 0이 될때까지 반복
    while num > 0:
        # 몫과 나머지
        num, tmp = divmod(num, N)
        s += t[tmp]
    # 다시 역순으로 뒤집는다
    s = s[::-1]
    return s


print(convert(149, 2))  # 10010101
print(convert(149, 8))  # 225
print(convert(149, 3))
print(convert(149, 16))  # 95