from sys import stdin
from collections import deque

n = int(stdin.readline())
lst = deque([])

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
            print(lst.popleft())
    else: # cmd에 입력된 값이 'empty'인 경우
        if len(lst) == 0  :
            print(1)
        else:
            print(0)

# 10842_큐의 코드를 복붙하면 시간초과 문제 발생
# 참고한 코드(구글링 결과)
# 'deque'라는 라이브러리를 쓰는 게 시간 단축에 도움이 되는 것 같다.
'''
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

q = deque([])

for _ in range(n):
    query = input().split()
    if query[0] == 'push':
            q.append(query[1])
    elif query[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif query[0] == 'size':
        print(len(q))
    elif query[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif query[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif query[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
'''
