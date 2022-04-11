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

N=int(sys.stdin.readline())

result=[]

for i in range(N):
    ls=list(map(int,sys.stdin.readline().split()))
    #내림차순성렬
    shell_sort(ls)
    # 맨앞의 숫자제거
    ls.remove(ls[-1])
    # 갭 차이
    gap_ls=[]
    for j in range(len(ls)-1):
        diff=ls[j]-ls[j+1]
        gap_ls.append(diff)
    result.append((ls[0],ls[-1],max(gap_ls)))
    # print('Class {}'.format(i+1))
    # print("Max {}, Min {}, Largest gap {}".format(ls[0],ls[-1],max(gap_ls)))
    

for i in range(len(result)):
    print('Class {}'.format(i+1))
    print("Max {}, Min {}, Largest gap {}".format(result[i][0],result[i][1],result[i][2]))
