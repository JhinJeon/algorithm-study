# 직접 작성해 본 코드(뭔가 알 것 같으면서도 모르겠다)

from sys import stdin
from collections import deque

n = int(stdin.readline())

while n > 1:
    turns = n ** 3
    ls = []
    for i in range(turns): #  1 2 3 4 5 6 7 8 9 
        ls.append(i % n)     # 1 2 0 1 2 0 1 2 0 
    rm = (turns % n) + 1 # 9 % 3 + 1  = 1 
    while rm in ls: 
        ls.remove(rm) 
    n -= 1
print(ls[0])