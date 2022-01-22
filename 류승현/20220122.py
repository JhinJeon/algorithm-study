# 최소 최대
"""
a = int(input())
num = list(map(int,input().split()))
max = num[0]
min = num[0]
for i in range(1,len(num)):
    if max < num[i]:
        max = num[i]
    else:
        max = max
    if min > num[i]:
        min = num[i]
    else:
        min = min

print(min, max)
"""

# 최댓값
"""
num = list()
cnt = 0
max = 0
for i in range(9):
    a = int(input())
    num.append(a)

for j in range(len(num)):
    if max < num[j]:
        max = num[j]
    
print(max)
print(num.index(max)+1)
"""

# 숫자의 개수 
'''
A = int(input())
B = int(input())
C = int(input())

total = str(A*B*C)

for i in range(10):
    print(total.count(str(i)))
print(total)
'''

# 나머지
"""
a = list()

for i in range(10):
    num = int(input())
    a.append(num % 42)

result = set(a)
print(len(result))
"""

# 평균
"""
a = int(input())
score = list(map(int,input().split()))

new_score = list()
for i in score:
    new_score.append(i/max(score)*100)
avr = sum(new_score)/a

print(avr)
"""

# OX퀴즈
"""
a = int(input())

for i in range(a):
    c = input()
    b = list(c)
    sum = 0
    count = 1
    
    for j in b:
        if j == 'O':
            sum += count
            count += 1
        else:
            count = 1
    print(sum)
"""

# 평균은 넘겠지
"""
a = int(input())

for i in range(a):
    b = input()
    score = list(map(int,b.split()))
    avr = sum(score[1:])/score[0]
    new_score = []
    for j in range(1,len(score)):
        if score[j] > avr:
            new_score.append(score[j])
    total = len(new_score)/score[0]*100
    print(f'{total:.3f}%')
"""

# 정수 N개의 합
"""
def solve(a):
    
    return sum(a)

a = solve([10, 20, 30])
print(a)
"""

# 셀프 넘버 - 문제 이해가 안되여....
"""
def d(a):
    a = a + sum(list(map(int,str(a))))
    return a

a = list()
for i in range(1,10001):
"""

# 한수 - 문제 이해가 안되여....
