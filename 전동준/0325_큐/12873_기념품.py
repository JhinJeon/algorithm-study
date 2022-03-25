# 직접 작성해 본 코드(뭔가 알 것 같으면서도 모르겠다)

from sys import stdin
#from collections import deque

n = int(stdin.readline())

while n > 1:
    turns = n ** 3
    ls = []
    for i in range(turns):
        ls.append(i % n)
    rm = turns % n + 1
    while rm in ls:
        ls.remove(rm)
    n -= 1

print(ls)
