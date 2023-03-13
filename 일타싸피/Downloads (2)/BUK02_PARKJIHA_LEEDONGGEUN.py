import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'BUK02_PARKJIHA_LEEDONGGEUN'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    targetList = list()
    if order == 1:
        targetList = [1, 3, 5]
    else:
        targetList = [2, 4, 5]
    remainList = [1,2,3,4,5]

    pocket = [[0,0], [127,0] ,[254,0] ,[0,127] ,[127,127] ,[254,127]]

    def distance(ball1, ball2):
        widths = ball2[0] - ball1[0]
        heights = ball2[1] - ball1[1]
        return math.sqrt(widths ** 2 + heights ** 2)


    def getAngle(ball1, ball2):
        chk = 0
        widths = abs(ball2[0] - ball1[0])
        heights = abs(ball2[1] - ball1[1])
        if ball1[0] == ball2[0]:
            if ball1[1] < ball2[1]:
                angles = 0
                cal = -1
            else:
                angles = 180
                cal = -3
        elif ball1[1] == ball2[1]:
            if ball1[0] < ball2[0]:
                angles = 90
                cal = -2
            else:
                angles = 270
                cal = -4
        elif ball1[0] < ball2[0] and ball1[1] < ball2[1]: # 1사분면
            chk = 1
            radians = math.atan(widths / heights)
            angles = 180 / math.pi * radians
            cal = 90-angles
        elif ball1[0] > ball2[0] and ball1[1] < ball2[1]: # 2사분면
            chk = 2
            radians = math.atan(widths / heights)
            angles = 360 - (180 / math.pi * radians)
            cal = angles-270
        elif ball1[0] > ball2[0] and ball1[1] > ball2[1]: # 3사분면
            chk = 3
            radians = math.atan(widths / heights)
            angles = (180 / math.pi * radians) + 180
            cal = 270-angles
        elif ball1[0] < ball2[0] and ball1[1] > ball2[1]: # 4사분면
            chk = 4
            radians = math.atan(heights / widths)
            angles = (180 / math.pi * radians) + 90
            cal = angles-90

        return [angles, chk, cal]


    def getHitPoint(LOAD,ball):
        hitX = ball[0]
        hitY = ball[1]
        radians = LOAD[2] * math.pi / 180
        if LOAD[1] == 1:
            hitX = ball[0] - 5.729 * math.cos(radians)
            hitY = ball[1] - 5.729 * math.sin(radians)
        elif LOAD[1] == 2:
            hitX = ball[0] + 5.729 * math.cos(radians)
            hitY = ball[1] - 5.729 * math.sin(radians)
        elif LOAD[1] == 3:
            hitX = ball[0] + 5.729 * math.cos(radians)
            hitY = ball[1] + 5.729 * math.sin(radians)
        elif LOAD[1] == 4:
            hitX = ball[0] - 5.729 * math.cos(radians)
            hitY = ball[1] + 5.729 * math.sin(radians)
        elif LOAD[1] == 0:
            if LOAD[2] == -1:
                hitY = ball[1] - 5.73
            elif LOAD[2] == -2:
                hitX = ball[0] - 5.73
            elif LOAD[2] == -3:
                hitY = ball[1] + 5.73
            elif LOAD[2] == -4:
                hitX = ball[0] + 5.73
        if 2.865 < hitX < 251.135 and 2.865 < hitY < 124.135:
            return [hitX, hitY]
        else:
            return None


    def outer(pos1, pos2, ball):
        M = abs((pos1[0]-ball[0])*(pos2[1]-ball[1]) - ((pos1[1]-ball[1])*(pos2[0]-ball[0])))
        T = math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

        if M/T < 5.75:
            return False
        else:
            return True


    def canPath(pos1, pos2, ball):
        B = outer(pos1, pos2, ball)
        len1 = distance(pos1, ball)
        len2 = distance(pos2, ball)
        lenT = distance(pos1, pos2)

        if not B and len1 <= lenT and len2 <= lenT:
            return False
        else:
            return True


    def canTouch(ball1, ball2, H):
        B = outer(ball1,H,ball2)
        lenL = distance(ball1,ball2)
        lenM = distance(ball1,H)
        # if getAngle(ball2,H)[0] - getAngle(ball2,ball1)[0] < 10:
        #     return False
        if lenM < math.sqrt(lenL**2 - B**2):
            return True
        else:
            return False


    for i in range(5):
        if targetList.count(i):
            if balls[i][0] == -1:
                targetList.remove(i)
        if balls[i][0] == -1:
            remainList.remove(i)

    targetBall = balls[targetList[0]]
    LOADSTACK = list()
    HITSTACK = list()
    temp = list()

    for p in pocket:
        LOADSTACK.append([distance(targetBall, p), getAngle(targetBall, p), pocket.index(p)])
    #print(LOADSTACK)
    LOADSTACK.sort()

    for L in LOADSTACK:
        for r in remainList:
            if not (r != targetList[0] and not canPath(balls[targetList[0]],pocket[L[2]],balls[r])):
                if getHitPoint(L[1], targetBall):
                    HITSTACK.append(getHitPoint(L[1], targetBall))
    print(HITSTACK)
    print("and remain is", remainList)
    temp = list()
    for H in HITSTACK:
        for r in remainList:
            if r != targetList[0] and not canPath(balls[0],H,balls[r]):
                if H not in temp:
                    temp.append(H)
            elif r == targetList[0] and not canTouch(balls[0],balls[r],H):
                if H not in temp:
                    temp.append(H)

    for t in temp:
        if len(HITSTACK) > 1:
            HITSTACK.remove(t)

    print("remain H is" ,HITSTACK)

    if not HITSTACK:
        HITSTACK.append(getHitPoint(L[1], targetBall))

    print("plus H is",HITSTACK)
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    angle = getAngle(balls[0], HITSTACK[0])[0]
    # distance: 두 점(좌표) 사이의 거리를 계산
    #distance = math.sqrt(width**2 + height**2)
    distance = distance(balls[0], balls[targetList[0]])
    print(getAngle(balls[targetList[0]], HITSTACK[0])[0] - getAngle(balls[targetList[0]], balls[0])[0])
    #distance = distance(balls[0], balls[3])

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.6
    power = max(25,min(100,power))
    print(balls[0][1])






    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')