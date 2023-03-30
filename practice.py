def f(num):
    if num <= 1:
        return 1
    return num * f(num-1)
N, K = map(int, input().split())
print(f(N) // (f(K)*f(N-K)))