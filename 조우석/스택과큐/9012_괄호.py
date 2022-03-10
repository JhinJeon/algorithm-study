import sys
T = int(sys.stdin.readline())

result=[]

for i in range(T):
    stack = []
    ls = list(map(str, sys.stdin.readline().strip()))
    for j in ls:
        if j=='(':
            stack.append(j)
        if j==')':
            if len(stack)==0:
                stack.append(j)
                break
            if stack[-1]=='(':
                stack.pop()

                            

            
    if len(stack)==0:
        result.append('YES')
    else:
        result.append('NO')
for i in result:
    print(i)