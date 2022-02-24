# 재귀함수
# 1.팩토리얼
'''
N = int(input())
result = 1
for i in range(N,1,-1):
    result = result * i
print(result)
'''
# 구글링 한 결과(재귀함수 사용)
'''
def factorial(n):
    result = 1
    if n > 0 :
        result = n * factorial(n-1)
    return result

n = int(input())
print(factorial(n))
'''
# 2. 피보나치 수열
'''
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))
'''
# 3. 별 찍기
'''
# 나름 해본 코드
def drawer(n):
    if n < 9:
        print('*'*n)
        print('*'+' '+'*')
        print('*'*n)
    
n = int(input())
print(drawer(n))
'''
'''
# 구글링 결과
n = int(input())

for _ in range(n):
    print('* '* (n - n//2))
    print(' *'* (n//2))
'''
# 에라 모르겠다

# 4. 하노이 탑 이동 순서

'''
def hanoi(n, a, b):
    if n > 1:
        hanoi(n-1, a, 6-a-b)             
    print(a, b)

    if n > 1:
        hanoi(n-1, 6-a-b, b)

n = int(input())
print(2**n -1)               
hanoi(n, 1, 3)
'''