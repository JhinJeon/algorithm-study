from sys import stdin
n = int(stdin.readline())
lst = []
for i in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == 'front':
        if len(lst) == 0  :
            print(-1)
        else:
            print(lst[0])
    elif cmd[0] == 'back':
        if len(lst) == 0  :
            print(-1)
        else:
            print(lst[-1])
    elif cmd[0] == 'size':
        print(len(lst))
    elif cmd[0] == 'push':
        lst.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(lst) == 0  :
            print(-1)
        else:
            print(lst.pop(0))
    else:
        if len(lst) == 0  :
            print(1)
        else:
            print(0)

# 참고한 코드(push 값을 구현하는 부분 참고)
'''
from sys import stdin

N = int(stdin.readline())
Que = []
for i in range(N) :
    A = stdin.readline().split()

    if A[0] == 'push' : Que.append(A[1])

    elif A[0] == 'pop' : 
        if Que : print(Que.pop(0))
        else : print(-1)

    elif A[0] == 'size' : print(len(Que))

    elif A[0] == 'empty' :
        if len(Que) == 0 : print(1)
        else : print(0)
            
    elif A[0] == 'front' :
        if len(Que) == 0 : print(-1)
        else : print(Que[0])
    
    elif A[0] == 'back' :
        if len(Que) == 0 : print(-1)
        else : print(Que[-1])
'''