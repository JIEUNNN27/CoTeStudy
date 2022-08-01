# 스택

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


n = int(input())

# order = ['push', 'pop', 'size', 'empty', 'top']

order = []
stack = []

for _ in range(n):
    temp = list(map(str, input().split()))
    order.append(temp)

# print(f'order[1][0] = {order[1][0]}')

for i in range(n):
    print(f' -------------{i}------------------')
    if order[i][0] == 'push':
        stack.append(order[i][1])
    elif order[i][0] == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif order[i][0] == 'size':
            print(len(stack))
    elif order[i][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[i][0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

# print(f'order = {order}')
# print(f'stack = {stack}')