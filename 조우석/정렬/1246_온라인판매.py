import sys
from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] < tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2

N,M=map(int,sys.stdin.readline().split())


ls=[] # 가격 정보
for i in range(M):
    ls.append(int(sys.stdin.readline()))

shell_sort(ls)


