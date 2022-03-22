import sys
from itertools import combinations, permutations
n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
num=[]
for _ in range(n):
    num.append(int(sys.stdin.readline()))

tmp=[]
for i in list(permutations(num,k)):
    s=''
    for j in range(0,k):
        s+=str(i[j])
    tmp.append(s)

answer=set(tmp)
print(len(answer))

