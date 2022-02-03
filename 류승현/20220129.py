# 아스키 코드
"""
a = input()

print(ord(a))
"""

# 숫자의 합
"""
n = input()
print(sum(map(int,n)))
"""

# 알파벳 찾기
"""
a = input()
b = 'abcdefghijklmnopqrstuvwxyz'
for i in b:
    if i in a:
        print(a.index(i), end= ' ')
    else:
        print( -1, end =' ')
"""

# 문자열 반복
"""
n = int(input())

for i in range(n):
    num, word = input().split()
    for x in word:
        print(x*int(num), end='')    
    print()
"""

# 단어 공부
"""
a = list(input().lower())

b = list(set(a))
cnt = list()

for i in b:
    c = a.count(i)
    cnt.append(c)


if cnt.count(max(cnt)) >=2:
    print("?")
else :
    print(b[cnt.index(max(cnt))].upper())
"""

# 단어의 개수 - 괄호 안에 " " 넣으면 왜 틀릴까?
"""
a = list(input().split())
print(len(a))
"""

# 상수
"""
a, b = input().split()

a = a[::-1]
b = b[::-1]

if a > b:
    print(a)
else :
    print(b)
"""
# 다이얼
"""
Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

a = input()
result = 0
for i in a:
    for j in Number:
        if i in j:
            result += Number.index(j) + 3

print(result)
"""

# 크로아티아 알파벳
"""
alpabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = input()
count = 0

for i in alpabet:
    if i in a :
        a = a.replace(i,"a")
        

for j in a:
    count+= 1
print(count)
"""

# 그룹 단어 체커
"""
a = int(input())
count = 0
b = list()
c = list()

for i in range(a):
    d = input()
    
    e = d[0]
    b = [e,]
    for j in d:
            
        if e != j:
            b.append(j)
            e = j
    b = sorted(b)
    c = sorted(set(b))
    
    if b == c:
        count+=1
print(count) 
"""