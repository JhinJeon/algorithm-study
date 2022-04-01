import sys
from typing import MutableSequence
from collections import deque
N=int(sys.stdin.readline())
que=deque()
                
# 삽입정렬

for i in range(N):
    que.append(sys.stdin.readline().split())

print(que[0])