#2742번(for문 6번)
num=int(input())
for i in range(num,0,-1):
    print(i)

# 11021번(for문 7번 )
import sys
num=int(input())
ls1=[]
ls2=[]
for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    ls1.append(a)
    ls2.append(b)
for i in range(num):
    print('Case #{}: {}'.format(i+1,ls1[i]+ls2[i]))


#11022번(for문 8번)
import sys
num=int(input())
ls1=[]
ls2=[]
for i in range(num):
    a,b=map(int,sys.stdin.readline().split())
    ls1.append(a)
    ls2.append(b)
for i in range(num):
    print('Case #{}: {} + {} = {}'.format(i+1,ls1[i],ls2[i],ls1[i]+ls2[i]))

# 2438번( for문 9번)
num=int(input())

for i in range(num):
    print("*"*(i+1))

# 2439번(for문  10번)
num=int(input())
for i in range(num):
    print(str("*"*(i+1)).rjust(num))
#10871번(for문 11번)
import sys
a,b=map(int,sys.stdin.readline().split())
ls=list(map(int,sys.stdin.readline().split()))
for i in ls:
    if b>i:
        print(i,end=' ')

#10952번(while문 1번)
import sys
ls1=[]
ls2=[]
while(True):
    a,b=map(int,sys.stdin.readline().split())
    if a==0 and b==0:
        break
    ls1.append(a)
    ls2.append(b)
for i in range(len(ls1)):
    print(ls1[i]+ls2[i])
#10951번(while문 2번)
import sys
while(True):
    try:
        a,b=map(int,sys.stdin.readline().split())
        print(a+b)
    except:
        break
#1110번(while문 3번) 

num=int(input())
start=num
count=0

while(True):
    a=start//10
    b=start%10
    c=(a+b) % 10
    start=(b*10) +c
    count+=1
    if(num==start):
        break
print(count)


