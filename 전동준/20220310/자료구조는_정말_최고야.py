# 자료구조는 정말 최고야

# 직접 작성해 본 코드(시간 초과)
from sys import stdin

n,m = map(int,stdin.readline().split())
stacked = []
result = 1
for i in range(m):
    texts = int(input())
    stacked = list(map(int,stdin.readline().split()))
    for a in range(texts-1):
        if stacked[a] < stacked[a+1]:
            result = 0
            break

print('Yes' if result==1 else 'No')

# 구글링 결과(스택을 안 쓰고 풀기)
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = True
for _ in range(m):
    i = int(input())
    k = list(map(int, input().split()))
    for j in range(i-1):
        if k[j] < k[j+1]:
            p = False
            break
    if not p: break

print('Yes' if p else 'No') 
'''

