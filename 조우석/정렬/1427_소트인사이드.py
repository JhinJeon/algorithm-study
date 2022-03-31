import sys
from typing import MutableSequence

def bubble_sort(a:MutableSequence) -> None:
    n=len(a)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
N=list(sys.stdin.readline().strip())
bubble_sort(N)
print(N)