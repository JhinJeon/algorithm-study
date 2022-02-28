import sys
from turtle import left, right
from typing import Sequence,Any 
N=sys.stdin.readline()
second_ls=list(map(int,sys.stdin.readline().split()))
M=sys.stdin.readline()
four_ls=list(map(int,sys.stdin.readline().split()))
second_ls.sort()

def bin_search(a:Sequence,key:Any)->int:
    left=0
    right=len(a)-1
    cnt=0
    while True:
        mid=(left+right)//2
        if a[mid]==key:
            cnt+1
            left=mid+1
        elif a[mid]<key:
            left=mid+1
        else:
            right=mid-1
        if left>right:
            break     
    return cnt
    
for i in four_ls:
    print(bin_search(second_ls,i),end=" ")
