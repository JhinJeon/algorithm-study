
# from sys import stdin
# N=int(stdin.readline())
# que=[i for i in range(1,N+1)] # 1~N까지 que에다가 값을넣는거

# round=0 
# point=0
# #                        1 2 3 4 5 6 7 8 9 10 
# while len(que) !=1:
#     print(que)
#     round+=1              # 1 
#     point+=round**3-1    #  2  
#     point=point%(len(que)) # 
#     que.pop(point)    # 
# print(que[0])



from sys import stdin
from typing import Deque
from collections import deque
n = int(stdin.readline())
cnt=1
ls=deque([i for i in range(1,n+1)]) # 1 2 3
turns=0
while len(ls)!=1:
    if cnt==1:
        ls.remove(ls[0])
        cnt += 1
        continue
    turns+=cnt**3-1   # -1은 index시작으 0부터이므로 
    turns = turns% len(ls)  #간과한건 새로시작할떄 index 0부터 시작이아니라 제거된다음숫자부터 시작.
    ls.remove(ls[turns])
    cnt+=1
print(ls[0])
