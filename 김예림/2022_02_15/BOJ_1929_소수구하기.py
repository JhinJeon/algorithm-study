M,n=map(int,input().split())
sieve = [True] * (n+1)
sieve[1]=False
m = int(n ** 0.5)
for i in range(2,m+1):
    if sieve[i]==True:
        for j in range(i+i,n+1,i):
            sieve[j]=False

for i in range(M,n+1):
    if sieve[i]==True:
        print(i)
 
 
