import sys 

cnt = int(sys.stdin.readline())
stack=[]

for i in range(cnt):
    command = sys.stdin.readline().split()

    if command[0] = 'push':
        stack.append(command[1])

    elif command[0] = 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)

    elif command[0] = 'size':
        print(len(stack))

    elif command[0] = 'empty':
        if len(stack):
            print(0)
        else:
            print(1)

    elif command[0] = 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)