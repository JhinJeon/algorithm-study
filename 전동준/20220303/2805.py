# 나무 자르기(미해결)
'''
from sys import stdin
n, m = map(int,input().split())
trees = map(int,stdin.readline().split())

# 원리가 뭔지 잘 모르겠다
'''
# 구글링 한 코드
'''
import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


h = 0
start = 0
end = max(tree)

while start<=end:
    s = 0
    middle = (start + end) // 2
    s = sum(i-middle if i > middle else 0 for i in tree)

    if s >= M:
        h = middle
        start = middle + 1
    else:
        end = middle - 1
print(h)
'''
# 얘도 원리가 뭔지 잘 모르겠다