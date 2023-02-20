# 함수로 구현
# def enqueue(data):
#     global rear
#     rear += 1
#     queue[rear] = data
#
# def dequeue():
#     global front
#     front += 1
#     return queue[front]
#
# queue = [0] * 3
# front = -1
# rear = -1
#
# rear += 1   # enqueue(1)
# queue[rear] = 1
#
# enqueue(2)
# enqueue(3)
#
# print(dequeue())
# print(dequeue())
# if front != rear:   # 같으면 빈 것 같지 않으면 남아 있는것
#     print(dequeue())
# if front != rear:
#     print(dequeue())

# list로 구현
# q = []
# q.append(10)
# q.append(20)
# q.append(30)
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))

# import 사용해서 구현
# from collections import deque
#
# q1 = deque()
# q1.append(100)
# q1.append(200)
# q1.append(300)
# print(q1.popleft())
# print(q1.popleft())
# print(q1.popleft())

# 1. 선형큐 직접 구현해보기
# def enqueue(item):  # 큐에 값을 넣는 함수
#     global rear
#     # rear가 한칸 밀려나면서 해당 위치에 item을 저장
#     if is_full():  # 큐가 꽉 찼을때
#         print('queue if full.')
#     else:
#         rear += 1
#         queue[rear] = item
#
#
# def dequeue():  # 큐에 값을 빼는 함수
#     global front
#     # front가 한칸 뒤로 밀려나면서 해당 위치의 아이템을 삭제
#     if is_empty():  # 큐가 비었을때
#         print('queue is empty.')
#     else:
#         front += 1
#         return queue[front]
#
#
# def is_empty():  # 위치가 같을때
#     global front, rear
#     return front == rear
#
#
# def is_full():  # 포화 상태일때
#     global rear
#     return rear == MAX_SIZE - 1
#
#
# def Qpeek():
#     global front
#     return queue[front + 1]
#
#
# MAX_SIZE = 100
# queue = [0] * MAX_SIZE
# front = -1
# rear = - 1
#
# enqueue(30)
# item = dequeue()
# print(item)

# 2. 동적인 리스트에서는 어떻게 작성하나..
# 뒤에다가 item 삽입
# def enqueue(item):  # 큐에 값을 넣는 함수
#     queue.append(item)
#
#
# # 앞에서 아이템 빼기
# def dequeue():  # 큐에 값을 빼는 함수
#     if is_empty():
#         print('queue if empty.')
#     else:
#         return queue.pop(0)
#
#
# def is_empty():  # 위치가 같을때
#     return len(queue) == 0
#
#
# # def is_full():  # list에서는 필요가 없다
# #     pass
#
# def Qpeek():
#     if is_empty():
#         print('queue if empty.')
#     else:
#         return queue[0]
#
#
# queue = []  # 비워있는 리스트
#
# enqueue(30)
# item = dequeue()
# print(item)
# print(is_empty())
# # print(is_full())
#
#
# enqueue(1)
# enqueue(2)
# enqueue(3)
# item = dequeue()
# print(item)
# item = dequeue()
# print(item)
# item = dequeue()
# print(item)

# 3. 모듈을 사용해서 구현하기

# 1. queue 모듈 Queue 자료구조 (동기화 지원 -> 속도가 느리다)
# from queue import Queue
#
# q = Queue()
# q.put(10)
# q.put(20)
# q.put(30)
# print(q.get())
# print(q.get())
# print(q.get())
# # print(q.get()) # 큐가 비어있으면 정지한다...
# print('코드 끝!')

# 2. collections 모듈 deque 자료구조 (동기화 지원x -> 속도가 빠름)
# from collections import deque
#
# q = deque()
# # 앞에다가 삽입
# q.appendleft(10)
# q.appendleft(20)
# q.appendleft(30)
# # 뒤에다가 빼기
# print(q.pop())
# print(q.pop())
# print(q.pop())
'''
원형 큐의 구조
공백상태와 포화상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
'''
