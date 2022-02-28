#1920번 수찾기(선형탐색)
from typing import Any,Sequence
import sys
import copy

def seq_search(b: Any, seq: Sequence) -> int:
    for i in seq:
        if b==i:
            return 1
    return 0

N=int(sys.stdin.readline())
ls1=list(map(int,sys.stdin.readline().split()))    
M=int(sys.stdin.readline())
ls2=list(map(int,sys.stdin.readline().split()))

result=[]
for i in ls2:
    result.append(seq_search(i,ls1))
    print(result[-1])



