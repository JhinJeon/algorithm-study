import sys
from typing import Sequence,Any 
def binary_search(ls:Sequence,key:Any)->int:
    left=0
    right=len(ls)-1
    while True:
        mid=(left+right)//2
        if ls[mid] == key:
            return 1
        elif ls[mid]>key:
            right=mid-1
        elif ls[mid]<key:
            left=mid+1
        if left>right:
            break
    return 0

T=int(sys.stdin.readline())
for i in range(T):
    M=int(sys.stdin.readline())
    ls1=sorted(list(map(int,sys.stdin.readline().split())))
    N=int(sys.stdin.readline())
    ls2=list(map(int,sys.stdin.readline().split()))
    
    for j in ls2:
        print(binary_search(ls1,j))