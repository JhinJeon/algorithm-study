from ast import keyword
import sys
   

N=int(sys.stdin.readline())

stack=[]
result=[]
for i in range(N):
    keyword=sys.stdin.readline().split()
    if keyword[0]=='push':
        stack.append(keyword[1])
    elif keyword[0]=='pop':
        if not stack:
            result.append(-1)
        else:
            result.append(stack.pop())
        
    elif keyword[0]=='size':
        result.append(len(stack))
    elif keyword[0]=='empty':
        if not stack:     # 스택 비어있을떄
            result.append(1)
        else:               #스택 안비어있을떄 
            result.append(0)
    elif keyword[0]=='top':
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
for i in result:
    print(i)