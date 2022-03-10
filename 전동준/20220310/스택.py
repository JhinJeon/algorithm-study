# 구글링 한 코드 참고해서 작성
from sys import stdin
n = int(input())
stack = []
for i in range(n):
    commandline = stdin.readline().split()
    order = commandline[0]
    if order == 'push':
        stack.append(commandline[1])
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'size':
        print(len(stack))