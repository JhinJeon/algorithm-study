# 피보나치 함수

# 직접 작성한 코드(미완성)
from sys import stdin
t = int(stdin.readline())

def fibo(n):
    if n == 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(t):
    k = int(stdin.readline())
    fibo(k)


# 참고한 코드(재귀함수를 안 쓴 것 같다)
'''
t = int(input())
 
for _ in range(t):
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    n = int(input())
    if n>1:
        for i in range(n-1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2]+cnt_1[-1]) 
 
    print(cnt_0[n], cnt_1[n])
'''