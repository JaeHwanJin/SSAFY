def recursive_function(num):
    if num == 101:
        return
    else:
        print(num, '번째 재귀함수에서', num+1, '번째 재귀함수를 호출합니다.')
        recursive_function(num + 1)
        print(num, '번째 재귀함수를 종료합니다.')
recursive_function(1)