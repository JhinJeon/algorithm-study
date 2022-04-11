import sys

N=int(sys.stdin.readline())

ls=[] # 키와몸무게정보
rank=[]

for i in range(N):
    tall,height=map(int,sys.stdin.readline().split())
    ls.append((tall,height))


for i in range(N):
    cnt=1 # 등수카운트
    for j in range(N):
        if ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]: # 특정대상의키<다른사람키 , 특정대상몸무게<다른사람몸무게
            cnt+=1 # 
    rank.append(cnt)
for i in rank:
    print(i,end=' ')            


# 첫번쨰사람 55 185  < 모든사람 키,몸무게 
