# 1 소수 찾기
'''
N = int(input())
numlist = map(int,input().split())
numcount = 0
for n in range(N):
    for k in numlist:
        noprime = 0
        if k > 1:
            for i in range(2,k):
                if k % i == 0:
                    noprime += 1
            if noprime == 0:
                numcount += 1
print(numcount)
'''
# 2 소수
'''
# 초안(시간 초과)
M = int(input())
N = int(input())

total = []
for n in range(N+1):  
    noprime = 0
    if n >= M:
        for i in range(2,N+1):
            if n != i:
                if n % i == 0:
                    noprime += 1
        if noprime == 0:
            total.append(n)
if len(total) != 0:
    total = set(total)
    print(sum(total))
    print(min(total))
else:
    print(-1)
'''
'''
# 수정안
M = int(input())
N = int(input())

total = []
for n in range(M, N+1):  
    noprime = 0
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                noprime += 1
                break   # break를 넣지 않으면 시간초과 문제 발생
        if noprime == 0:
            total.append(n)

if len(total) != 0:
    print(sum(total))
    print(min(total))
else:
    print(-1)
'''
# 3 소인수분해
'''
N = int(input())
divider = 2
while divider <= N:
    if N % divider == 0:
        print(divider)
        N = N / divider
    else:
        divider += 1
'''
# 7 직사각형에서 탈출
'''
x, y, w, h = map(int,input().split())

length = [x, abs(w-x)]
height = [y, abs(h-y)]
garo = min(length)
sero = min(height)
if garo > sero:
    print(sero)
else:
    print(garo)
'''
# 8 네 번째 점
'''
point1, point2 = map(int,input().split())
point3, point4 = map(int,input().split())
point5, point6 = map(int,input().split())

if point1 == point3:
    if point6 == point4:
        print(point5,point2)
    else:
        print(point5,point4)
elif point3 == point5:
    if point2 == point6:
        print(point1,point4)
    else:
        print(point1,point6)
else:
    if point2 == point4:
        print(point3,point6)
    else:
        print(point3,point2)
'''
# 9 직각삼각형
'''
# 직접 만들어 본 코드(예시문 넣었을 때는 맞았는데 채점해 보니 틀림)
a, b, c = map(int,input().split())
A = a**2
B = b**2
C = c**2
right = 'right'
wrong = 'wrong'
if A>0 and B>0 and C>0:
    if A + B == C:
        print(right)
    elif B + C == A:
        print(right)
    elif A + C == B:
        print(right)
    else:
        print(wrong)
# 이하 구글링한 정답
while True :
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break  # 세 수가 0이면 break
    max_num = max(nums)
    nums.remove(max_num)
    if nums[0]**2 + nums[1]**2 == max_num**2:
        print('right')
    else:
        print('wrong')
'''

# 질문 : 9번 위에거는 왜 틀린 거지