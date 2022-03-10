# n = int(input())
# s = []
# op = []
# count = 1
# temp = True
# for i in range(n):
#     num = int(input())
#     while count <= num:
#         s.append(count)
        
#         count += 1
#     if s[-1] == num:
#         s.pop()
#         op.append(num)
#     else:
#         temp = False
# if temp == False:
#     print('NO')
# else:
#     for i in op:
#         print(i)
import sys
n=int(sys.stdin.readline())
stack=[]
temp=[]
clac=[]
cnt=1
for i in range(n):
    num=int(sys.stdin.readline())
    while cnt<=num:
        temp.append(cnt)
        clac.append('+')
        cnt+=1
    if temp[-1]==num:
        clac.append('-')
        stack.append(temp.pop())
#불가능이면 NO
if len(stack)!=n:
    print('NO')
    exit()

#각각 +,- 출력
if len(clac)!=0:
    for i in clac:
        print(i)