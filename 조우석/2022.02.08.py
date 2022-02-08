#기초수학2 1번(소수찾기)
'''
import sys
num=int(sys.stdin.readline())
cnt=0
ls=list(map(int,sys.stdin.readline().split(' ')))

for i in ls:
    if i!=1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            cnt+=1
print(cnt)
'''
#기초수학2 2번(2581 소수)
'''
import sys
min_num=int(sys.stdin.readline())
max_num=int(sys.stdin.readline())
ls=[]

for num in range(min_num,max_num+1):
    flag=1    
    for j in range(2,num):
        if num%j==0:
            flag=0
            break
    if flag==1 and num!=1:
        ls.append(num)
if ls:
    print(sum(ls))
    print(min(ls))
else:
    print(-1)

'''

#기초수학2 3번(소인수분해)
'''
import sys
num=int(sys.stdin.readline())
if num == 1:
    print('')
for i in range(2,num+1):
    if num%i==0:
        while num%i==0:
            print(num)
            num/=i
'''

#기초수학2 4번(1929 소수구하기)
'''
import sys
num1,num2=map(int,sys.stdin.readline().split())

for i in range(num1,num2):
    flag=True
    if i==1:
        flag=False
    else:
        for j in range(2,i):
            if i%j==0:
                flag==False
                break
    if flag==True:
        print(i)
        '''
#기초수학2 5번(4948 베르트랑 공준)

#기초수학2 6번(9020 골드바흐의추측)

#기초수학2 7번(1085 직사각형에서 탈출)
'''
import sys
x,y,w,h=map(int,sys.stdin.readline().split())
print(min(x,y,w-x,h-y))

#기초수학2 8번(3009 네번째점)
x_ls=[]
y_ls=[]
for i in range(1,4):
    x,y=map(int,sys.stdin.readline().split())
    x_ls.append(x)
    y_ls.append(y)
for j in range(1,4):
    if x_ls.count(x_ls[i])==1:
        new_x=x_ls[i]
    if x_ls.count(x_ls[i])==1:
        new_y=y_ls[i]
print(new_x,new_y)
   ''' 


#기초수학2 9번(4153 직각삼각형)
'''import math
import sys
while True:
    num=sys.stdin.readline()
    if num=="0 0 0":
        break
    triangle=list(map(int,sys.stdin.readline().split()))
    triangle.sort()   # 내림차순
    if int(math.sqrt(triangle[0]**2 +triangle[1]**2 ))==triangle[2]: #직각삼각형공식
        print('right')
    else:
        print('wrong')
'''

#기초수학2 10번(3053 택시 기하학)
'''
from math import pi
import sys
r=int(sys.stdin.readline())
taxi=r*r*2  # 원둘레
area=r*r*pi #원 넓이
print(round(area,4))
print(round(taxi,4))
'''

#기초수학2 11번(1002 터렛)
