def prime(n):
    cnt=0
    sieve = [True] * (2*(n+1))
    sieve[1]=False
    m = int((2*n) ** 0.5)
    for i in range(2,m+1):
        if sieve[i]==True:
            for j in range(i+i,(2*n)+1,i):
                sieve[j]=False

    for i in range(n+1,(2*n)+1):
        if sieve[i]==True:
            cnt+=1
    return cnt

answer=[]  
while True:
    n=int(input())
    if n==0:
        break
    else:
        answer.append(prime(n))
        
for i in answer:
    print(i)
