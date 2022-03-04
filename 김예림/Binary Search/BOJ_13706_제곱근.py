N=int(input())

def search(start,end):       
    while start<=end:
        mid=(start+end)//2
        if mid*mid==N:
            print(mid)
            break
        elif mid*mid<N:
            start=mid+1
        else:
            end=mid-1
        
search(1,N)
