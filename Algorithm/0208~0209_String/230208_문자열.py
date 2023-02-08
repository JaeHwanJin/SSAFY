# 문자열 뒤집기
# a = 'algorithm'
# print(a[::-1])

# a = list(a)
# a.reverse()
# a = ''.join(a)
# print(a)

# 내장함수를 사용하지 않고 형변환
# def itoa(number):
#     result = ''  # number의 문자열을 저장할 변수
#     # 변환과정 : 123 -> 12'3' -> 1'23' -> '123'
#     while number > 0:
#         # 1. 숫자의 첫째자리 수를 문자로 변환해서 result 문자열에 더해주는 과정
#         result = chr(ord('0') + number % 10) +result
#         # 2. number = number // 10
#         number = number // 10
#     return result
#
#
# if __name__ == '__main__':
#     num = 123
#     string = itoa(num)  # '123'
#     print(string)
#     print(type(string))

# 회문
# 회문인지 확인하고 결과를 반환
# 1번째 방법
# if string == string[::-1]:
#     return True
# else:
#     return False

# 2번째 방법 list
# origin = string
# string = list(string)
# string.reverse()
# return origin == ''.join(string)

# 3번째 방법 for
# for i in range(len(string) // 2):
#     if string[i] != string[-1]:
#         return False
# return True
