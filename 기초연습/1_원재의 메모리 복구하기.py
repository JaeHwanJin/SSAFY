# T = int(input())
#
# for tc in range(1, T + 1):
#     num = list(input()) # string 타입은 immutable객체이므로 list로 생성
#     reset = list('0' * len(num))    # 초기화 상태 리스트 생성
#     a = ['0'] * len(num)
#     cnt = 0
#     for i in range(len(num)):
#         if reset[i] != num[i]:  # 각 리스트의 0번 인덱스의 값이 다르다면
#             reset[i:] = num[i] * len(reset[i:]) # 다른 인덱스의 값을 리스트의 끝까지 추가
#             cnt += 1    # 횟수 +1
#     print(f'#{tc} {cnt}')

