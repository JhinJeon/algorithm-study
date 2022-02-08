#1978 [소수찾기]

import sys
N=int(input())
num=list(map(int,sys.stdin.readline().split()))
answer=0
for i in num:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        answer+=1
print(answer)

#2581 [소수]
import sys
m=int(input())
n=int(input())
prime=[]

for i in range(m,n+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        prime.append(i)
if not prime:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
    
#11653 [소인수분해]

m=int(input())
if m==1:
    print("")
for i in range(2,m+1):
    if m%i==0:
        while m%i==0:
            print(i)
            m=m//i
#1085 [직사각형에서 탈출]

x,y,w,h=map(int,input().split())
print(min(x,y,w-x,h-y))

#3009 [네 번째 점]

a=[]
b=[]
answer_x=0
answer_y=0
for i in range(3):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
for i in a:
    if a.count(i)==1:
        answer_x=i
for j in b:
    if b.count(j)==1:
        answer_y=j
print(answer_x,answer_y)

#4153 [직각삼각형]
import sys
data=[]
answer=[]
while True:
    data=list(map(int,sys.stdin.readline().split()))
    if sum(data)==0:
        break
    else:
        data.sort()
        if (data[0]**2)+(data[1]**2)==data[2]**2:
            print('right')
        else:
            print('wrong')
