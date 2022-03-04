# 암기왕

from sys import stdin

def search(seq,key):
    pl = 0
    pr = len(seq)-1
    while True:
        pc = (pl + pr) // 2
        if seq[pc] == key:
            return 1
        elif seq[pc] < key:
            pl = pc + 1
        else :
            pr = pc - 1
        if pl > pr:
            break
    return 0

tc = int(input())
for t in range(tc):    
    n = int(input())
    memo1 = sorted(map(int,stdin.readline().split()))
    m = int(input())
    memo2 = map(int,stdin.readline().split())
    for k in memo2:
        print(search(memo1,k))