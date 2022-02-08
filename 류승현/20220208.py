# 소수 찾기
"""
num = int(input())
count = 0

a = list(map(int, input().split()))

for i in a:
    b = list()
    for j in range(1, i+1):
        c = i % j
        b.append(c)
    if b.count(0) == 2:
         count+=1

print(count)
"""

# 소수
# -fail-
"""
M = int(input())
N = int(input())
sosu = list()

for i in range(M,N+1): # 소수 구하기
    b = list()
    for j in range(1,i+1):
        c = i % j
        b.append(c)
        
    if b.count(0) == 2:    
        sosu.append(i)

if len(sosu) > 0 :
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
"""
# -pass
"""
min_num = int(input())
max_num = int(input())
decimal_list = []
 
for i in range(min_num, max_num+1):     # 첫 입력값과 두번째 입력값 사이만 진행
    count = 0
    for j in range(1, i+1):             # 1부터 i항까지 진행
        if i % j == 0:
            count += 1                  # 나뉘면 count증가
            if count > 2:               # 2보다 크면 소수가 아니므로(소수는 1과 자기자신으로만 나뉨) 바로 다음식 진행
                break
    if count == 2:                      # 소수
        decimal_list.append(i)
if len(decimal_list) != 0:              # 소수리스트에 값이 있다면 밑의 값을 출력
    print(sum(decimal_list))
    print(decimal_list[0])
else:                                   # 소수가 하나도 없다면
    print('-1')

"""

# 소인수분해 - 시간초과

# num = N = int(input())
# sosu = list()

# for i in range(2,N+1):     
#     count = 0
#     for j in range(1, i+1):             
#         if i % j == 0:
#             count += 1                  
#             if count > 2:               
#                 break
#     if count == 2:                     
#         sosu.append(i)
    


# for j in sosu:    
#     while True :
#         if num % j != 0:
#             break

#         else :
#             num = num/j
#             print(j)

N = int(input())

for i in range(2,N+1):
    while True:
        if N % i == 0:
            N = N//i
            print(i)
        else :
            break
        
    

# 직사각형에서 탈출
"""
x, y, w, h = map(int, input().split())

width = w-x
high = h-y

print(min(x, y, width, high))
"""

# 네 번째 점
"""
x_list = list()
y_list = list()

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)


for j in range(3):
    if x_list.count(x_list[j]) == 1:
        final_x = x_list[j]
    if y_list.count(y_list[j]) == 1:
        final_y = y_list[j]
print(final_x,final_y)
"""
# 직각삼각형
"""
while True:
    x = list(map(int, input().split()))
    
    if x.count(0) == 3:
        break
    
    x.sort()
    
    if x[0]**2 + x[1]**2 == x[2]**2:
        print('right')
    else :
        print('wrong')
"""

