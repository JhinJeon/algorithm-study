# 비밀번호 찾기

from sys import stdin
from enum import Enum
#from chained_hash import ChainedHash    
# ChainedHash : 교재에 있는 코드인데 import가 안 되는 문제 발생
n, m = stdin.readline().split()

for i in range(n):
    dns, passwd = (stdin.readline().split())

#for j in range(m):


# 구글링 결과

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
add = {}

for _ in range(N):
    site, ps = input().split()
    add[site] = ps

for _ in range(M):
    print(add[input().rstrip()])
'''
