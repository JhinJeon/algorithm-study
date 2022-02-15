def pibo(n):
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1
    return pibo(n-1)+pibo(n-2)

n=int(input())
print(pibo(n+1))
