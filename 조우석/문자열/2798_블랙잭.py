import sys
from itertools import combinations

#입력받는부분
N,M=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))

#정렬





# #브르투탐색법 응용
# def bf_match(num:int, M:int) -> int:
#     total=0   # 3장의카드 합산값
#     pp=0    # num이 커서위치
total=0
for i in combinations(num,3): # 3개를 뽑아
    total+=sum(i)
    print(i)
            
        
    
       
   
        
  

        