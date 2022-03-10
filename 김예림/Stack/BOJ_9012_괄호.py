import sys
T=int(sys.stdin.readline())
ans=''
for _ in range(T):
    check=0
    s=sys.stdin.readline().strip()
    for i in range(0,len(s)):
        if s[i]=='(':
            check+=1
        else:
            check-=1
        
        if check==-1:
            ans="NO"
            break

    if check==0 and s[len(s)-1]==')':
        ans="YES"
    else:
        ans="NO"
    print(ans)
