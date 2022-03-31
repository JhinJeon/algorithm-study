# 직접 작성해 보려다가 12번째 줄부터 구글의 도움을 받은 코드

from sys import stdin
from collections import deque

n,m = map(int,stdin.readline().split())
numlist = list(map(int,stdin.readline().split()))

src = deque(list(range(1,n+1)))
cnt = 0
for i in numlist:
    while True:
        if i == src[0]:
            src.popleft()
            break
        else:
            if src.index(i) < len(src)/2:
                while src[0] != i:
                    src.append(src.popleft())
                    cnt += 1
            else:
                while src[0] != i:
                    src.appendleft(src.pop())
                    cnt += 1
print(cnt)


# 구글링 결과
# 찾으려는 숫자가 앞쪽과 뒤쪽 중 어느 쪽이 가까운지를 이용하는 것이 중요한 것 같다
'''
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
idxs = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

cnt = 0
for idx in idxs:
    while True:
        if dq[0] == idx:
            dq.popleft()
            break
        else:
            if dq.index(idx) < len(dq)/2:
                while dq[0] != idx:
                    dq.append(dq.popleft())
                    cnt += 1
            else:
                while dq[0] != idx:
                    dq.appendleft(dq.pop())
                    cnt += 1
print(cnt)
'''
