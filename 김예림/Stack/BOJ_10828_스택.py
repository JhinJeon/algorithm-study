import sys
N=int(sys.stdin.readline())
stk=[]
cndlist=[]
for _ in range(N):
    cmd=sys.stdin.readline().strip()
    if 'push' in cmd:
        stk.append(cmd.split()[1])
    elif cmd=='top':
        if len(stk)!=0:
            print(stk[len(stk)-1])
        else:
            print(-1)
    elif cmd=='pop':
        if len(stk)!=0:
            print(stk.pop())
        else:
            print(-1)
    elif cmd=='size':
        print(len(stk))
    elif cmd=='empty':
        if len(stk)==0:
            print(1)
        else:
            print(0)        



        


    
