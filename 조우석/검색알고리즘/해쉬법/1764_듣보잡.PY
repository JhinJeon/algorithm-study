import sys
N, M = map(int, sys.stdin.readline().split())
dic = {}
cnt = 0
for i in range(N):
    key = sys.stdin.readline().strip()  # 문자열 입력방식
    if key not in dic:
        dic[key] = 1
    else:
        dic[key] += 1

result = []
cnt = 0
for key, value in dic.items():
    if value == 2:
        cnt += 1
        result.append(key)

result.sort()
print(cnt)
for j in result:
    print(j)

#풀이2: 시간이 더 느려 
# dic=dict(sorted(dic.items()))
# print(cnt)
# for key,value in dic.items():
#     if value==2:
#         print(key)