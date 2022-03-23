# 10845 큐 로 풀었을떄는 시간초과뜸.
import sys
from collections import deque

num = int(sys.stdin.readline())
que = deque()

for i in range(num):
    keyword = list(sys.stdin.readline().split())
    if keyword[0] == 'push':
        que.append(keyword[1])

    elif keyword[0] == 'front':
        if len(que) == 0:
           print(-1)
        else:
            print(que[0])

    elif keyword[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])

    elif keyword[0] == 'size':
        print(len(que))
    elif keyword[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif keyword[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
            # https://scribblinganything.tistory.com/31
            # pop(0)은 가장앞단꺼낼때 O(n) 시간걸림
            # popleft()는 o(1) 시간이걸림

