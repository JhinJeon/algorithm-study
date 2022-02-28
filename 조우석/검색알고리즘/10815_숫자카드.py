#10815 숫자카드(이진검색문제)
from typing import Sequence,Any
import sys


N=int(input())
ls1=list(map(int,sys.stdin.readline().split()))
M=int(input())
ls2=list(map(int,sys.stdin.readline().split()))
ls1.sort()
    
def bin_search(a:Sequence,key:Any)->int:        
    pl = 0
    pr = len(a)-1
    
    while True:
        pc=(pl+pr)//2
        if a[pc]==key:
            return 1
        elif a[pc]<key:
            pl=pc+1
        else:
            pr=pc-1
        if pl>pr:
            break
    return 0


for i in ls2:
    print(bin_search(ls1,i),end=" ")



