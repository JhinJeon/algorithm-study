import sys



def draw(n, idx):
    if n == 1:
        stars[idx][idx] = '*'
        return
    l = 4*n-3

    for i in range(idx, l+idx):
        stars[idx][i] = '*'
        print(stars)
        stars[idx+l-1][i] = '*'
        print(stars)
        stars[i][idx] = '*'
        print(stars)
        stars[i][idx+l-1] = '*'
        print(stars)
    return draw(n-1, idx+2)


n = int(sys.stdin.readline())

lens = 4*n-3
#파이썬 이중리스트 만들기 
stars = [[' ']*lens for i in range(lens)]

# 파이썬 이중리스트 만들기
ls1=[]
for i in range(lens):
    ls2=[]
    for j in range(lens):
        ls2.append(' ')
        if j == lens:
            print()
    ls1.append(ls2)
print(ls1)



draw(n,0)

for i in range(lens):
    for j in range(lens):
        print(stars[i][j],end='')
    print()

