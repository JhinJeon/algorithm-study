# 별 찍기- 19

# 구글링 한 내용 참고해서 작성해 본 코드(미완성)
'''
from sys import stdin
n = int(stdin.readline())
def star(n,x,y):
    len = 4 * n - 3
    if n == 1:
        star[y][x] = '*'
        return
    for i in range(len):
        star[y][x + i] = '*'
        star[y + i][x] = '*'
        star[y + len - 1][x + i] = '*'
        star[y + i][x + len - 1] = '*'
star(n,0,0)
'''
# 참고한 코드

N = int(input())
stars = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]

def fill_star(n, x, y):
    if n == 1:
        stars[y][x] = '*'
        return

    length = 4 * n - 3

    for i in range(length):
        stars[y][x + i] = '*'
        stars[y + i][x] = '*'
        stars[y + length - 1][x + i] = '*'
        stars[y + i][x + length - 1] = '*'

    fill_star(n - 1, x + 2, y + 2)

fill_star(N, 0, 0)
for s in stars:
    print(' '.join(s))

