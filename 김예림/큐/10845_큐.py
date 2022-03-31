import sys
from collections import deque
N=int(sys.stdin.readline())
q=deque([])
for _ in range(N):
    cmd=sys.stdin.readline().strip()
    if 'push' in cmd:
        q.append(cmd.split()[1])
    elif cmd=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd=='size':
        print(len(q))
    elif cmd=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif cmd=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif cmd=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
        
