# 제곱근
'''
# 직접 해 본 코드(런타임 에러)
from math import sqrt

n = int(input())
m = sqrt(n)
print(m)
'''
# 구글링 한 코드
'''
def binary_search(s, e):
    target = e
    while True:
        mid = (s + e) // 2
        if (mid ** 2) == target:
            return mid
        if mid ** 2 > target:
            e = mid
        elif mid ** 2 < target:
            s = mid

N = int(input())
print(binary_search(1, N))
'''
# 구글링 한 코드 응용해서 만들어 본 코드(무한루프 걸림)
'''
import sys
sys.setrecursionlimit(10**7)

def binary_search(s, e):
    target = e
    mid = (s + e) // 2
    while (mid**2) != target:
        if mid ** 2 > target:
            e = mid
            binary_search(s,e)
        elif mid ** 2 < target:
            s = mid
            binary_search(s,e)
    return mid

N = int(input())
print(binary_search(1, N))
'''