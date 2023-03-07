# arr 배열 안에 10 미만의 요소만 있는지 파악하는 코드 작성
arr = [1,7,3,5,9]

# # 1. 카운트 변수
# cnt = 0
# # arr 배열을 순회하면서 10미만의 요소가 있다면 cnt 1 증가.
# for i in arr:
#     if i < 10:
#         cnt += 1
#
# # cnt 변수와 arr 배열 크기가 같다면? (안의 모든 요소가 10미만 값이다)
# if cnt == len(arr):
#     print('모든 요소는 10 미만이에요!')
# else:
#     print('요소 중에 10이상인 값이 있어요!')


# # 2. 함수를 만들어서 체크하는 방법
# # arr 배열을 순회하면서 10 이상의 값이 있다면 바로 False
# # 아니라면 True를 반환하게 한다.
# def check(arr):
#     for i in arr:
#         if i > 10:
#             return False
#     return True
#
# if check(arr):
#     print('다들 10미만의 값이에요!')
# else:
#     print('10 이상의 값이 있어요!')


# 3. for~else 문
# for 문이 (break문이나 제어문에 의해 강제적으로 종료되지 않는 경우)
# 정상적으로 종료가 되면, else 문의 코드 블럭을 실행합니다...

for i in arr:
    if i > 10:
        break
else:
    print('10 미만의 값만 있어요!')

print('코드의 끝!')