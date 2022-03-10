import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())

stack=[] 

for i in range(M):
    num=int(sys.stdin.readline())
    ls=list(map(int,sys.stdin.readline().split()))
    if ls !=sorted(ls,reverse=True):
        stack.append(1)
if not stack: # 빈리스트는 기본이 False
    print('Yes')
else:print('No')
#스택은 파이썬에서는 리스트로 