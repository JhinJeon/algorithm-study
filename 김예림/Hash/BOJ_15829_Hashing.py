import sys
import string
N=int(sys.stdin.readline())
D=dict()
s=sys.stdin.readline().rstrip()
numbering=string.ascii_lowercase
result=0

for i in range(0,len(numbering)):
    D[numbering[i]]=i+1
for i in range(0,len(s)):
    result+=D[s[i]]*(31**i)
print(result%1234567891)
