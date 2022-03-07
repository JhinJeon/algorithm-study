import sys
N, M = map(int, sys.stdin.readline().split())


def get_key(data):
    return (hash(data)/(N+M))
hash_table=[0 for i in range(N+M)]
dic={}
count = 0
for i in range(N):
    key = (sys.stdin.readline().strip())  # 문자열 입력방식
    result=0
    for j in key:
        result+=ord(j)
    if key not in dic:
        # hash_table[result%(N)].append(key)
        dic[key]=result%(N)

print(hash_table)
print(dic)
count=0
for i in range(M):
    key = sys.stdin.readline().strip()
    if key in dic:
        hash_table.append(hash_table[dic[key]])
for i in range(N+1,len(hash_table)):
    print(hash_table[i])
     

#시간이 더 느려 
# dic=dict(sorted(dic.items()))
# print(cnt)
# for key,value in dic.items():
#     if value==2:
#         print(key)


#내풀이
# result = []
# cnt = 0
# for key, value in dic.items():
#     if value == 2:
#         cnt += 1
#         result.append(key)

# result.sort()
# print(cnt)
# for j in result:
#     print(j)
