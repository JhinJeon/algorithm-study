import sys
from typing import MutableSequence

# 버블정렬 
# def bubble_sort(a:MutableSequence) -> None:
#     n=len(a)
#     for i in range(n-1):
#         for j in range(n-1,i,-1):
#             if a[j-1]<a[j]:
#                 a[j-1],a[j]=a[j],a[j-1]
                
# 삽입정렬
def insert_sort(a:MutableSequence) -> None:
    n=len(a)
    for i in range(1,n):
        j=i
        tmp=a[i]
        while j>0 and a[j-1] <tmp:
            a[j]=a[j-1]
            j-=1
        a[j]=tmp
        

N=list(sys.stdin.readline().strip())
# bubble_sort(N)
insert_sort(N)
for i in N:
    print(i,end='')