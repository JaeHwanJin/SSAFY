A = [1, 2, 3]
N = len(A)


def f(i, N):
    # 기저조건 ( i == N ) 종료해라...
    if i == N:  # 순열완성
        print(A)
        return

        # for j : i -> N-1[i, N]
    for j in range(i, N):
        # 배열 요소 교환
        A[i], A[j] = A[j], A[i]
        # 다음 단계로 진행
        f(i + 1, N)
        # 배열 요소 원상복구
        A[i], A[j] = A[j], A[i]


f(0, N)


