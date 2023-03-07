'''
중위 표기법에서 후위 표기법으로 변환 알고리즘(스택 이용)
1. 입력 받은 중위 표기식에서 토큰을 읽는다.
2. 토큰이 피연산자이면 토큰을 출력한다.
3. 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면
    스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때 까지
    스택에서 pop 한 후 토큰의 연산자를 push한다.
    만약 top에 연산자가 없으면 push한다.
'''

# 중위 표현식 입력
string = input()

# 스택
result = []
stack = []
for ch in string:
    # 1. 피연산자(숫자라면)
    if ch.isnumeric():
        result.append(ch)
    # 2. '(' 라면
    elif ch == '(':
        stack.append(ch)
    # 3. '*' or '/' 라면
    elif ch == '*' or ch == '/': #elif ch in ['*', '/']:
        # 만약에 top에 이미 '*', '/' 있다면 pop해준다.
        if len(stack) > 0 and stack[-1] == '*' or stack[-1] == '/':
            result.append(stack.pop())
        # 그리고 자기 자신은 stack에 추가
        stack.append(ch)
    # 4. '+' or '-' 라면
    elif ch == '+' or ch == '-':
        # 기존에 stack에 들어있던 값이 우선순위가 높다면 빼준다.
        while len(stack) > 0 and stack[-1] in ['+', '-', '*', '/']:
            result.append(stack.pop())
        stack.append(ch)
    # 5. ')' 라면
    elif ch == ')':
        # 여는 괄호가 나올 때 까지 pop을 해준다.
        while stack[-1] != '(':
            result.append(stack.pop())
        stack.pop() # '('

# stack에 남아있는 연산자들을 모두 빼준다.
while len(stack) > 0:
    result.append(stack.pop())

print(*result)
