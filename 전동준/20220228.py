# 수 찾기
'''
# 초안(for loop로 구현하는 과정에서 문제가 있는 것 같음)
from sys import stdin


n = int(input())
N = sorted(map(int,stdin.readline().split()))
m = int(input())
M = sorted(map(int,stdin.readline().split()))

from typing import Any, Sequence

def search(key : Any, seq : Sequence):
    pl = 0
    pr = len(seq)-1
    while True:
        pc = (pl+pr) // 2
        print('pc:',pc)
        if seq[pc] == key:
            return 1
        elif seq[pc] < key:
            pl = pc + 1
        else :
            pr = pc - 1
        if pl > pr:
            break
    return 0


for l in M:
    print(search(l,N))
'''
'''
# 구글링 정답
from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))
'''

# 2. 숫자카드
'''
from sys import stdin
N = int(input())
intlist = sorted(map(int,stdin.readline().split()))
intlist.sort()
M = int(input())
checker = sorted(map(int,stdin.readline().split()))

def search(size,seq,key):
    pl = 0
    pr = size-1
    while True:
        pc = (pl + pr) // 2
        if seq[pc] == key:
            return 1
        elif seq[pc] < key:
            pl = pc + 1
        else :
            pr = pc - 1
        if pl > pr:
            break
    return 0

temp = []
for k in checker:
    temp.append(search(N,intlist,k))
print(temp)
'''
# 이게 왜 틀리는지 모르겠다

# 구글링 정답
'''
import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
'''
# 3. 숫자카드 2
'''
# 구글링 한 결과
import sys
input = sys.stdin.readline

N = int(input())
cards = sorted([*map(int, input().split())])
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def binarySearch(arr, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid+1, end)
    else:
        return binarySearch(arr, target, start, mid-1)
    
for target in candidate:
    print(binarySearch(cards, target, 0, len(cards)-1), end=" ")
'''

#4. 듣보잡

'''
# 구글링 결과
import sys

N, M = map(int, sys.stdin.readline().split())
N_list = [sys.stdin.readline().strip() for i in range(N)]
M_list = [sys.stdin.readline().strip() for i in range(M)]

# 교차하는 이름들을 찾는다
duplicate = list(set(N_list) & set(M_list))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)
'''
# 문자형 데이터의 이진문제는 어떻게 푸는 건지?

# 5. 랜선 자르기
 
# 구글링 결과
'''
import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan) #이분탐색 처음과 끝위치

while start <= end: #적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 #중간 위치
    lines = 0 #랜선 수
    for i in lan:
        lines += i // mid #분할 된 랜선 수
        
    if lines >= N: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)
'''
# 정답 코드를 봐도 원리가 뭔지 잘 모르겠다(이진분석이랑 어떤 상관이 있는지 모르겠다)

# 6. 게임

import sys
X, Y = map(int, input().split())
winrate = round((Y / X) * 100)
result = 0
vanced = 0
temp = 0
while winrate != vanced:
    if X == Y:
        result = -1
        break
    else:
        Y += 1
        X += 1
        vanced = round((Y / X) * 100)
        temp += 1
    result = temp

print(result)
