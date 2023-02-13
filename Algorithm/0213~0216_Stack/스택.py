# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         # stack 리스트에 요소가 없다면... 반환값이 없음
#         if len(self.stack) == 0:
#             return
#         return self.stack.pop(-1)


def push(item):
    global stack
    stack.append(item)


def pop():
    global stack
    if len(stack) == 0:
        return
    return stack.pop(-1)


stack = []

'''
()()((()))
((()((((()()((()())((())))))
())
(()
'''


def check(string):
    global stack
    stack = []
    # 문자열에서 문자를 하나씩 꺼내겠다.
    for ch in string:
        # 검사를 진행하다가 검사가 실패한다면 False
        #
        if ch == '(':
            # '(': 스택에 push
            push('(')
        else:  # elif ch == ')':
            # ')': pop '(' <-> ')'
            if pop() == '(':
                continue
            return False
    # stack 안에도 요소가 없다면 (검사 결과가 잘 진행되었다면) True
    if not stack:
        return True
    return False


for _ in range(4):
    string = input().replace(' ', '')
    if check(string):
        print('SUCCESS')
    else:
        print('FAIL')