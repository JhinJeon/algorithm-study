# 1 손익분기점
'''
# for loop로 구현해 본 코딩(종종 오류가 있음)
A = int(input())
B = int(input())
C = int(input())

answer = 0
n = 0
while True:
    n += 1
    cost = A + B * n
    income = C * n
    if cost < income :
        answer = n
        break
print(answer)

# 구글링 결과(정답)
A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(int(A//(C-B)+1))
'''
# 2 벌집
'''
num = int(input())
cabin = 1
distance = 1
while num > cabin:
    cabin += 6 * distance
    distance += 1
print(distance)
'''
# 3 분수찾기
'''
X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')
'''
# 4 달팽이는 올라가고 싶다
'''
numlist = input().split()
A = int(numlist[0])
B = int(numlist[1])
V = int(numlist[2])
start = 0
day = 1
while start < V:
    start += A
    if start < V:
        start -= B
        day += 1
print(day)
# math 함수 이용(시간초과 방지)
import math

a, b, v = map(int, input().split())
day = math.ceil((v-a)/(a-b)) + 1
print(day)
'''
#5 ACM 호텔
'''
t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')
'''
#6 부녀회장이 될테야
'''
#직접 만들어 본 코드(시간초과)
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    temp2 = 1
    temp3 = 0
    while temp2 < n:
        temp3 += n
        n += 1
        temp2 += 1
    print(temp3)
#정답(구글링 결과)
t = int(input())

for w in range(t):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num):
            f0[i] += f0[i-1]
        print(f0)
    print(f0[-1])
'''
#7 설탕 배달
'''
order = int(input())
bag = 0
while order >= 0:
    if order % 5==0:
        bag += order//5
        print(bag)
        break
    order -= 3
    bag += 1
else:
    print(-1)
'''
#8 큰 수 A+B
'''
A, B = map(int, input().split())
print(A+B)
'''
# 8번은 큰 수 계산 시 별도의 math 함수를 사용해야 하는 줄 알았는데 
# 파이썬 특징 알려주는 문제였다

#9 Fly me to the Alpha Centauri
# 직접 작성한 코드(채점 결과 틀림)
'''
T = int(input())
for t in range(T):
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    distance = y-x-2
    if distance == 0:
        distance = 2
    elif distance < 0:
        distance = 1
    elif distance == 1:
        distance = 3
    else:
        movecount = 0
        gab = 1
        while distance > 0:
            distance -= gab * 2
            gab += 1
            movecount += 1
        distance = movecount + 2
    print(distance)
'''
# 구글링 결과(정답)
'''
t = int(input())

for w in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)
'''
# 질문 : 내가 볼 땐 위 코드도 원하는 내용을 출력해주는 것 같은데 뭐가 문제인가