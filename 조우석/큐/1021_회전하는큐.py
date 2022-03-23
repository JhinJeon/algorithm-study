
#이문제는 원하는 index를 맨앞까지 옮긴다음에 빼야된다.

import queue
import sys
from collections import deque

from soupsieve import select
N,M=map(int,sys.stdin.readline().split()) # 큐의크기,뽑을개수
idx=list(map(int,sys.stdin.readline().split()))
que=deque([i for i in range(1,N+1)])
cnt=0 # 옮기는횟수

# 3 4 5 6 7 8 10 1
# 5 6 7 8 10 1 3 4 
for i in range(M):
    ls=que.copy()
    mid=len(que)//2 # que의길이//2로 이진탐색해봄
    choice=que.index(idx[i]) # 찾으려는 값의 index
    if mid<choice: # que의 중앙값 < 뽑으려는 수
        for _ in range(len(que),1,-1):
            if que[0] == ls[choice]:
                break
            cnt += 1
            que.appendleft(que.pop())  #오른쪽->왼쪽 이동
        que.popleft()           # idx값 빼기
    else:
        for _ in range(len(que)):
            if que[0] == ls[choice]:
                break
            cnt += 1  # 이동한횟수
            que.append(que.popleft()) #왼쪽->오른쪽 이동    
        que.popleft()    # idx값 빼기
print(cnt)

#que.rotate(1) # 1 2 3 4-> 4 1 2 3
#que.rotate(-1) # 1 2 3 4-> 2 3 4 1  이거쓰면 런타임에러 나옴.
