T = int(input())  # 테스트 케이스

for tc in range(1, T + 1):  # 테스트 케이스만큼 반복
    N, M = map(int, input().split())  # 도화지 크기와 도장을 찍은 횟수
    arr = [[0] * 8 for _ in range(8)]  # 주어진 도화지의 크기
    cnt = 0  # 도장을 찍은 횟수를 확일할 때 사용 할 cnt
    for i in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        for x in range(x1, x1 + y2):  # 모서리 좌표에서부터 너비와 높이를 더한 값만큼 도장을 찍어준다.
            for y in range(y1, y1 + x2):
                arr[x][y] += 1
                if arr[x][y] > 1:  # 겹치는 부분을 제외하기 위한 if문
                    arr[x][y] = 1
    for k in range(len(arr)):  # 도장을 찍은 부분이 몇 칸인지 확인해 결과를 출력
        for z in range(len(arr)):
            if arr[k][z] == 1:
                cnt += 1
    print(f'#{tc} {cnt}')  # 결과 출력
