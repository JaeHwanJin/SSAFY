import sys


def get_pi(pattern):
    length = len(pattern)
    pi = [0] * length
    j = 0

    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    return pi


def kmp(text, pattern):
    pi = get_pi(pattern)
    t_len, p_len = len(text), len(pattern)
    j = 0
    result = []

    for i in range(t_len):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            if j == p_len - 1:
                result.append(i - p_len + 2)
                j = pi[j]
            else:
                j += 1

    return result


text = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()

result = kmp(text, pattern)

print(len(result))
print(*result)
