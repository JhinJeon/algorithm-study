import sys
n=int(sys.stdin.readline())
stack=[] # 최종적으로 원하는숫자
temp=[] # 임시저장소
clac=[] # + - 저장공간
cnt=1 #숫자 
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
