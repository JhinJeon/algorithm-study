import sys
from  typing import Sequence,Any 

def binary_search(ls:Sequence)->int:
    left=0
    right=max(ls)
    # 4 7
    # 20 15 10 17
    while True:
        total=0
        mid=(left+right)//2
        #각나무길이-중간값 의 총합 구하기
        for tree_len in tree:
            if tree_len>mid:
                total+=tree_len-mid

        #총합이 M보다 클면 mid를 더큰수로 만들기위해 left를 중앙값뒤로 이동한다.
        if total>=M:
            result=mid
            left=mid+1
        else:
            right=mid-1    # 찾으려는 길이의 최대값을 중앙값 앞쪽으로 이동.
        if left>right:    #왼쪽이 오른쪽초과하면 탈출
            break
    return result

N,M=map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))
left=0
right=max(tree)
result=0
print(binary_search(tree))

