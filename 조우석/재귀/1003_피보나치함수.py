from sys import stdin

ls=[0,0]   # 0의개수, 1의개수

def fibo(n:int) -> int : #피보나치 수열 함수구현
    if (n == 0) : # fibo(0) 이면 0 출력갯수 +1
        ls[0]+=1
        return 0
    elif (n == 1) :# fibo(1) 이면 1 출력갯수 +1
        ls[1]+=1
        return 1
    else: 
        fibo(n-1)
        fibo(n-2)

T=int(stdin.readline())
for i in range(T):
    num=int(stdin.readline())
    fibo(num)
    print(ls[0],ls[1])
    ls = [0, 0]     #초기화
