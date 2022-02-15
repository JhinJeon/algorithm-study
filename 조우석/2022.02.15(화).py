#10872 팩토리얼
'''
def factorial(n):
    sum=1
    if n>0: #n이 1일때까지 
        return factorial(n-1) *n
    else:
        return sum
num=int(input())
print(factorial(num))'''

#10870 피보나치수5
'''def pibona(n):
    if n<=1:
        return n
    else:
        return pibona(n-1)+pibona(n-2)
num=int(input())
print(pibona(num))
'''


#11729 하노이 탑이동 순서
'''
import sys
def h_tower(n,start,end): #n은 옮길 막대번호
    if n==1:
        print(start,end)
        return 0
    h_tower(n-1,start,6-start-end)
    print(start,end)
    h_tower(n-1,6-start-end,end)
num=int(sys.stdin.readline())
print(2**num-1)
h_tower(num,1,3)''' 
