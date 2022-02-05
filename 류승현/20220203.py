# 손익분기점 - 왜 런타임 에러가 나지

"""
A,B,C = map(int,input().split())

n = A/(C-B)

if C-B <= 0:
    print(-1)

else :
    print(int(n)+1)

A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))
"""

# 벌집
"""
a = int(input())
b = 1
count = 1
while a > b:
    b += 6*count
    count+=1

print(count)
"""

# 분수찾기 - 모르것소
# n = int(input())

# count = 1
# a = 1
# b = 1

# while n > count :
#     if b == 1 and a == 1:
#         b += 1
#         count += 1

#     elif b == 1:
#         a += 1
#         count += 1
#         if a % 2 == 1:
#             while True:
#                 a-=1
#                 b+=1
#                 count+=1
#                 if a == 1:
#                     break    
    
#     elif a == 1:
#         b += 1
#         count +=1
#         if a % 2 == 1:
#             while True:
#                 a-=1
#                 b+=1
#                 count+=1
#                 if a == 1:
#                     break
    
    
    
                
    
# print(a,'/',b)

# 달팽이는 올라가고 싶다
"""
A, B, V = map(int, input().split())

n = (V-B) / (A-B)

if n > int(n):
    print(int(n) + 1)
else :
    print(int(n))
"""
# ACM 호텔
"""
num = int(input())

for a in range(num):
    room = list()
    H, W, N = map(int, input().split())
    for i in range(1,W+1):
        for j in range(1,H+1):
            n = j*100+i
            room.append(n)
    print(room[N-1])
"""

# 부녀회장이 될테야
"""
num = int(input())

for i in range(num):
    k = int(input())
    n = int(input())

    room = list(range(1, n+1)) # 0층
    
    for j in range(k): # k층까지 반복
        for i in range(1, n): # n-1호까지 더하기
            room[i] += room[i-1]
    print(room[-1])
"""

# 설탕 배달
"""
N = int(input())
count = 0

while N >= 0 :
    if N % 5 == 0 :
        count += (N // 5)
        print(count)
        break
    N -= 3 
    count += 1

    if N < 0:
        print(-1)
        break
"""

# 큰 수 A+B
"""
A, B= map(int, input().split())

print(A+B)
"""

# Fly me to the Alpha Centauri - 못풀었음 (아직 푸는 중)
"""
T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    count = 2
    dis = (y - x) - 2
    mov = 1

    while dis  < 0 :
        if dis > mov :
            mov += 1
            dis -= mov
            count += 1
            print(dis)
        elif dis == mov :
            count+=1
            print(dis)
        else :
            mov -= 1
            dis -= mov
            count += 1
            print(dis)
    print(count)
"""