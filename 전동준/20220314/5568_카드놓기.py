# 직접 작성해 본 코드
# (정확하지 않은 결과-12번째 줄에서 두 자리 이상의 수를 분리해서 입력해야 함)

from sys import stdin
import itertools
n = int(stdin.readline())
k = int(stdin.readline())
def cardsort(a,b):
    numlist = []
    cardlist = []
    for i in range(a):
        numlist.append((str(stdin.readline())))
    print(len(list(map(' '.join, itertools.combinations(numlist, b)))))

cardsort(n,k)

# 참고한 코드
'''
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) 
# 이상 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) 
# 이상 2개의 원소로 수열 만들기
'''

#구글링 결과(순열 문제라고 함, 브루트포스 사용)
'''
from sys import stdin
from itertools import permutations as p

arr = []
n, k = int(stdin.readline()), int(stdin.readline())
for i in range(n):
    arr.append(int(stdin.readline()))

res = set()
for i in list(p(arr, k)):
    res.add(''.join(list(map(str, i))))

print(len(res))
'''