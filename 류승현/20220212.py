# 소수 구하기

# M, N = map(int, input().split())

# for i in range(M,N+1):
#     if i == 1:
#         pass
#     else :
        
# 베르트랑 공준  # 시간초과

# while True:
#     n = int(input())
    

#     if n == 0:
#         break
#     else:
#         count = 0
#         for num in range(n,2*n+1):
#             error = 0
#             if num > 1 :
#                 for i in range(2, num):
#                     if num % i == 0:
#                         error += 1
#                 if error == 0:
#                     count += 1
                    
#         print(count)



    


# 골드바흐의 추측

# 택시 기하학
"""
from math import pi

R = int(input())

print(f'{R**2*pi:.6f}')
print(f'{(2*R)**2/2:.6f}')
"""

# 터렛
"""
N = int(input())

for i in range(N):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())

    d1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
    d2 = r1 + r2
    d3 = abs(r1-r2)
    
    if d1 == 0 and r1 == r2:
        print(-1)
    elif d3 == d1 or d2 == d1:
        print(1)
    elif d3 < d1 < d2 :
        print(2)
    else :
        print(0)
"""


# 팩토리얼
"""
N = int(input())

def f(n):
    num = 1
    if n >1:
        num = n *f(n-1)
    return num

print(f(N))
"""

# 피보나치 수 5

"""
n = int(input())
def a(n):
    if n <= 1:
        return n
    else :
        return a(n-1) +a(n-2)

print(a(n))
"""


# 별 찍기 - 10
# N = int(input())


# 하노이 탑 이동 순서
