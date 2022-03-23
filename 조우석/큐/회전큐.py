#이문제는 원하는 index를 맨앞까지 옮긴다음에 빼야된다.

import queue
import sys
from collections import deque

from soupsieve import select
N, M = map(int, sys.stdin.readline().split())  # 큐의크기,뽑을개수
idx = list(map(int, sys.stdin.readline().split()))
que = deque([i for i in range(1, N+1)])
cnt = 0  # 옮기는횟수

# 3 4 5 6 7 8 10 1
# 5 6 7 8 10 1 3 4
for i in range(M):
    ls = que.copy()
    mid = len(que)//2  # que의길이//2로 이진탐색해봄
    choice = que.index(idx[i])  # 찾으려는 값의 index
    if mid < choice:  # que의 중앙값 < 뽑으려는 수
        if que[0] !=ls[choice]:
            num=len(que)-choice
            que.rotate(num)   # 오른쪽->왼쪽
            cnt+=num
        que.popleft()    # idx값 빼기  

    else:
        if que[0] !=ls[choice]:
            num=len(que)-choice-1
            que.rotate(-num)
            cnt+=num  
        que.popleft()    # idx값 빼기
              
        
                                          #왼쪽->오른쪽
        
print(cnt)

#que.rotate(1) # 1 2 3 4-> 4 1 2 3
#que.rotate(-1) # 1 2 3 4-> 2 3 4 1  이거쓰면 런타임에러 나옴.
