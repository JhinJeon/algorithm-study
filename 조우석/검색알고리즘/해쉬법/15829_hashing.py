import sys

L=int(sys.stdin.readline())
string=sys.stdin.readline().strip()
result=0

# a~z까지 번호부여 
dic={}
count=1
for i in range(ord('a'),ord('z')+1):
    dic[chr(i)]=count
    count+=1

count=0
for i in string:
    result += (dic[i] * (31**(L-(L-count))))
    count+=1
print(result%1234567891)
