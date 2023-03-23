from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations

l = [1, 2, 3]

# 조합 combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합 뽑기
# for i in combinations(l, 2):
    # print(i)

# combinations_with_replacement(iterable, r): iterable에서 원소 개수가 r개인 중복 조합 뽑기
# for i in combinations_with_replacement(l, 2):
    # print(i)

# 순열 permutations(iterable,r=None) : iterable에서 원소 개수가 r개인 순열 뽑기
# for i in permutations(l): #r을 지정하지 않거나 r=None으로 하면 최대 길이의 순열이 리턴된다
# 	print(i)

# eval 문자열 내의 숫자 사칙연산 제공
print(eval('3+5'))