
T = int(input())
# T만큼 테스트 케이스 반복
for tc in range(1, T + 1):
    '''
    K : 최대 이동횟수
    N : 종점 정류장
    M : 충전기가 설치된 정류장 수
    '''
    K, N, M = list(map(int, input().split()))
    # 전기버스 충전기가 설치된 정류장
    charge_station = list(map(int, input().split()))
    # 충전 횟수 count와 현재 위치 current 변수 초기화
    count = current = 0
    # 종점에 도착할 때까지 반복
    while current + K < N:
        # 최대 이동횟수 K 동안 이동
        for move in range(K, 0, -1):
            # 현재 위치에서 이동가능한 횟수만큼 이동했을때 전기버스충전기가 있다면 현재위치 수정
            if (current + move) in charge_station:
                # 현재 위치 수정
                current += move
                # 충전 횟수 수정
                count += 1
                break
            # 현재 위치에서 이동가능한 횟수만큼 이동했을때 전기버스충전기가 없다면 현재위치 수정
            else:
                count = 0
                break
    # 결과 출력
    print(f'#{tc} {count}')