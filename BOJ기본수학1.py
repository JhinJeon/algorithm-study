#1712 [손익분기점]
a,b,c= map(int,input().split())
ans=0
if b>=c:
    print(-1)
else:
   ans=(a//(c-b))+1
   print(ans)
  
#2292 [벌집]
cnt=1
room=1
n=int(input())
if n==1:
    print(1)
else:
    while True:
        room+=6*cnt
        cnt+=1
        if room>=n:
            print(cnt)
            break

#1193 [분수찾기]
x=int(input())
num=0
num_cnt=0
numberth=0
while True:
    num_cnt+=1
    num+=num_cnt
    if num>=x:
        numberth=num-x+1
        break
if num_cnt%2==0: #짝수
    i=numberth
    j=num_cnt-numberth+1
    print(f"{j}/{i}")
else:
    i=num_cnt-numberth+1
    j=numberth
    print(f"{j}/{i}")

#10757 [큰 수 A+B]
a,b=map(int,input().split())
print(a+b)
