def draw(n,idx):
    if n==1:
        starMap[idx][idx]="*"
        return starMap
    l=4*n-3
    for i in range(idx,l+idx):
        starMap[idx][i]="*"    #윗벽
        starMap[idx+l-1][i]="*"  #아래벽

        starMap[i][idx]="*"  #왼쪽벽
        starMap[i][idx+l-1]="*"  #오른쪽벽
    draw(n-1,idx+2)
    return starMap

n=int(input())
lens=4*n-3
starMap=[[' ']*lens for _ in range(lens)] #2중배열 생성! 
draw(n,0)
#출력
for i in range(0,lens):
    for j in range(0,lens):
        print(starMap[i][j],end="")
    print()
