from typing import MutableSequence
import sys

N=int(sys.stdin.readline().strip())
que=[]
#삽입정렬 시간초과
# def insert_sort(a:MutableSequence) -> None:
#     n=len(a)
#     for i in range(1,n):
#         j=i
#         tmp=a[i]
#         while j>0 and a[j-1] <tmp:
#             a[j]=a[j-1]
#             j-=1
#         a[j]=tmp
# 쉘정렬  통과 
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
    
for i in range(N):
    input=int(sys.stdin.readline())
    que.append(input)
# insert_sort(que)
# que.sort(reverse=True)
shell_sort(que)
sum=0
for i in range(N):
    if i%3 !=2:  # 0으로떨어지게(3의배수) , 1이 남게( 4,7,10..)
        sum+=que[i]
print(sum)