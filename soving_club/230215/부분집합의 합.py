# 부분 집합 만들기
# i는 현재 해당되는 인덱스의 값을 0 또는 1로 바꿔주는 값
# k값은 인덱스의 끝, 배열의 크기 (기저조건)
def f1(i, k):
    if i == k: # 기저조건
        print(bits)
        return
    # i에 해당되는 인덱스 값을 0 으로 바꿔준다 (그 후에 재귀호출 -> 다음 i+1)
    bits[i] = 0
    f1(i+1, k)
    # i에 해당되는 인덱스 값을 1 으로 바꿔준다
    bits[i] = 1
    f1(i+1, k)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
bits = [0] * N
f1(0, N)


# k값은 인덱스의 끝, 배열의 크기 (기저조건)
def f1(i, k):
    if i == k:  # 기저조건
        # 부분 집합이 합이 10이면, 출력...
        total = 0
        for idx in range(len(bits)):
            if bits[idx] == 1:
                total += A[idx]
        if total == 10:
            for idx in range(len(bits)):
                if bits[idx] == 1:
                    print(A[idx], end=' ')
            print()
        return
    # i에 해당되는 인덱스 값을 0 으로 바꿔준다 (그 후에 재귀호출 -> 다음 i+1)
    bits[i] = 0
    f1(i + 1, k)
    # i에 해당되는 인덱스 값을 1 으로 바꿔준다
    bits[i] = 1
    f1(i + 1, k)


def f2(i, k, total):
    if total > 10:
        return
    if i == k:  # 기저조건
        if total == 10:
            for idx in range(k):
                if bits[idx]:
                    print(A[idx], end=' ')
            print()
        return
    # i에 해당되는 인덱스 값을 0 으로 바꿔준다 (그 후에 재귀호출 -> 다음 i+1)
    bits[i] = 0
    f1(i + 1, k, total)

    # i에 해당되는 인덱스 값을 1 으로 바꿔준다
    bits[i] = 1
    # total += A[i]
    f1(i + 1, k, total + A[i])
    # total -= A[i]


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
bits = [0] * N
f1(0, N)
f2(0, N, 0)