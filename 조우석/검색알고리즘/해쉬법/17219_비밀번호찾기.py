import sys
N,M=map(int,sys.stdin.readline().split())
dic={}
for i in range(N):
    key,value=map(str,sys.stdin.readline().strip().split())
    dic[key]=value

for i in range(M):
    print(dic[sys.stdin.readline().strip()])


#내풀이

# result=[]
# for j in range(M):
#     key=sys.stdin.readline().strip()
#     if key in dic:
#         result.append(dic[key])
# for i in result:
#     print(i)