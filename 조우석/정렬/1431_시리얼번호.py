import sys
from typing import MutableSequence
N=int(sys.stdin.readline())
ls=[]



def shell_sort(a: MutableSequence) -> None:
    for i in range(N- 1): # 0번쨰부터 N-1번쨰까지 조사
        for j in range(i+1,N): # 1번째부터 N-1번째까지조사.
            if len(ls[i]) > len(ls[j]):
                ls[i],ls[j]=ls[j],ls[i]

    
    
    # n = len(a)
    # h = n // 2
    # while h > 0:
    #     for i in range(h, n):
    #         j = i - h
    #         tmp = a[i]
    #         while j >= 0 and a[j] < tmp:
    #             a[j + h] = a[j]
    #             j -= h
    #         a[j + h] = tmp
    #     h //= 2

for i in range(N):
    ls.append(sys.stdin.readline().split())

for i in range(N):
    for j in range(i+1,N):
        if len(str(ls[i])) > len(str(ls[j])):
            ls[i],ls[j]=ls[j],ls[i]
        elif len(str(ls[i])) == len(str(ls[j])):
            sum_A=0
            sum_B=0
            