# 작성한 코드

from sys import stdin
from collections import deque # 리스트 맨 앞의 값을 쉽게 처리하기 위해 사용
k = int(stdin.readline())

for z in range(k):
    score = deque(map(int,stdin.readline().split()))
    n = score.popleft()
    a = max(score)
    b = min(score)
    gap = []
    for i in range(n-1):    # 단순 정렬 알고리즘 사용(오름차순)
        lowest = i
        for j in range(i+1, n):
            if score[j] < score[lowest]:
                lowest = j
        score[i], score[lowest] = score[lowest], score[i]
    for x in range(1,n):
        gap.append(score[x] - score[x-1])
    c = max(gap)

    print(f'Class {(z+1)}')
    print(f'Max {a}, Min {b}, Largest gap {c}')