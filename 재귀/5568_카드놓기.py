# #풀이 1
# import sys
# n=int(sys.stdin.readlsne())
# k=int(sys.stdin.readlsne())
# card_num=lsst()

# for i in range(n):
#     card_num.append(input())
    
# # card_num2=[sys.stdin.readlsne().rstrip() for i in range(n)]
# result=set() #중복을없애려고 set사용

# 빽트래킹(https://han-py.tistory.com/240)
# def permu(cnt,per,visit):
#     global card_num
        
#     if cnt==k:       
#         result.add(''.join(per))
#         return
#     else:
#         for index in range(n):
#             if not visit[index]:
#                 visit[index]=1
#                 permu(cnt+1,per+[card_num[index]],visit)
#                 visit[index]=0
# permu(0,[],[0]*n)
# print(len(result))

# 코딩테스트에서는 순열,조합같은 라이브러리 제공 X 
# 1234,2431,... 같이 순서를 전부확인하는걸 backtracking 코드
# https://han-py.tistory.com/240



# 풀이 2 
# import sys
# from itertools import permutations


# n=int(sys.stdin.readlsne())
# k=int(sys.stdin.readlsne())
# card_ls = []  # 전체 카드리스트 저장소

# result=set() #중복없애려고 집합활용
# for _ in range(n):
#     # input_num=int(sys.stdin.readlsne())
#     # card_ls.append(input_num) 이거 오류
#     card_ls.append(input())

# for i in permutations(card_ls, k):
#     result.add(''.join(i)) # 'a', 'b', 'c' 리스트를 'abc' 문자열로 만듦
# print(len(result))

#풀이3 (https://jinho-study.tistory.com/1047)
def dfs(depth):
    if depth == k:
        s.add(''.join(map(str, li)))
        print('s:',s)
        return ;
    for i in range(n):
        print('check:',check)
        if check[i]:
            continue
        li.append(nums[i])
        print('ls',li)
        check[i] = 1
        
        dfs(depth+1)
        li.pop()
        check[i] = 0
        
n, k = int(input()), int(input())
nums = [int(input()) for _ in range(n)]
li, s = [], set()
check = [0]*n
dfs(0)
print(len(s))