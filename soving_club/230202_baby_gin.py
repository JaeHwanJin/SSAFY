# 대표적인 greedy-problem(탐욕 알고리즘 문제)
# 매 순간에 선택과 방법이 최적인 답이 나오는 문제
# (단, 그 순간 선택이 종합적으로 봤을 때 최적이지 않을 수 있다...)
# 결론 : 탐욕 문제인지 아닌지는 많은 알고리즘 문제를 풀어봐야한다.
# 베이비진 문제 : 탐욕x 순열로 3개 카드를 뽑아내서 run, trippet... <


# 베이비진인지 확인해서 True, False 를 함수
# run, trippet 이라면 True, (아니라면 False 반환)
# 탐욕적으로 작성! 매 순간, 최선의 선택! -> '체크를 하는 순간' 입력이 들어온 카드를 기준으로 작성...
# def isBabygin(counts, c):
#     """
#     :param counts: 플레이어의 카드 카운트 리스트
#     :param c: 방금 입력 받은 카드 번호
#     :return: 베이비진이면 True를 반환, (아니라면 False 반환)
#     """
#     # run 인지 판별하는 로직
#     if counts[c] >= 3:
#         return True
#     # trippet 인지 판별하는 로직
#     # c, c+1, c+2 의 카드가 존재하는지 확인
#     if (c < 8) and counts[c] and counts[c+1] and counts[c+2]:
#         return True
#     # c-1, c, c+1 의 카드가 존재하는지 확인
#     if (1 < c < 9) and counts[c-1] and counts[c] and counts[c+1]:
#         return True
#     # c-2, c-1, c 의 카드가 존재하는지 확인
#     if (2 < c) and counts[c-2] and counts[c-1] and counts[c]:
#         return True
#     # run, trippet 해당되지 않으면 False 반환
#     return False
#
# T = int(input()) # 테스트케이스
#
# for tc in range(1, T+1):
#     # 두 플레이어가 가지게 되는 카드 리스트 (0~9 : 길이가 10인 리스트)
#     p1_counts = [0] * 10
#     p2_counts = [0] * 10
#     # 숫자 리스트를 저장할 리스트
#     cards = list(map(int, input().split()))
#     result = 0 # 승리한 사람의 정수를 담는 변수
#     # 숫자 리스트를 순회하면 플레이어1, 플레이어2 순서대로 카드를 나눠주는 로직
#     for idx, card in enumerate(cards):
#         if idx % 2 == 0:
#             p1_counts[card] += 1
#             # 베이비진인지 판별하는 로직 (run, trippet ...판단 로직... -> 함수!)
#             if isBabygin(p1_counts, card):
#                 # True -> 해당 플레이어가 승리했다고 결과를 반환하고, 순회 종료
#                 result = 1
#                 break
#         else: #플레이어2
#             p2_counts[card] += 1
#             # 베이비진인지 판별하는 로직 (run, trippet ...판단 로직... -> 함수!)
#             if isBabygin(p2_counts, card):
#                 # True -> 해당 플레이어가 승리했다고 결과를 반환하고, 순회 종료
#                 result = 2
#                 break
#     # 승리 결과를 출력
#     print(f'#{tc} {result}')


"""
입력

3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
"""

"""
출력 

#1 0
#2 1
#3 2
"""