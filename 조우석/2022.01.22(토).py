#1차원 배열 1번(최소, 최대)
import sys
#num=int(input()) 으로하면 안됨.
num = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
print(min(ls), max(ls))


#1차원 배열 2번(최대값)
ls = []
for i in range(9):
    ls.append(int(sys.stdin.readline()))
print(max(ls), ls.index(max(ls))+1)

#1차원 배열 3번(숫자의개수)
ls1 = []
ls2 = [i for i in range(10)]
for i in range(3):
    num = int(sys.stdin.readline())  # map(int,sys.stdin.readline())
    ls1.append(num)

total = list(str(ls1[0]*ls1[1]*ls1[2]))
for i in range(len(ls2)):
    print(total.count(str(i)))

#1차원 배열 4번(나머지)
ls1 = []
ls2 = [i for i in range(10)]
for i in range(3):
    num = int(sys.stdin.readline())  # map(int,sys.stdin.readline())
    ls1.append(num)


total = list(str(ls1[0]*ls1[1]*ls1[2]))
for i in range(len(ls2)):
    print(total.count(str(i)))

#1차원 배열 5번(평균)
num = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
maxi = max(score)
total = 0
for i in range(len(score)):
    total += score[i]/maxi*100

avg = total/len(score)
print(avg)

#1차원 배열 6번(OX퀴즈)
num = int(sys.stdin.readline())
for i in range(num):
    text = list(map(str, sys.stdin.readline()))
    count = 0
    total = 0
    for j in range(len(text)):
        if text[j] == 'O':
            count += 1
            total += count
        elif text[j] == 'X':
            count = 0
    print(total)

#1차원 배열 7번(평균은 넘겠지)
n = int(sys.stdin.readline())

def sum2(ls):
    sum = 0
    for i in range(1, len(ls)):
        sum += ls[i]
    return sum

for i in range(n):
    ls = list(map(int, sys.stdin.readline().split()))
    avg = sum2(ls)/ls[0]
    percent = 0
    for j in range(len(ls)):
        if ls[j] > avg:
            percent += 100/ls[0]
    print('{:.3f}%'.format(percent))

#함수 1번(정수N개의합)
import sys
def solve(a: list):
    sum = 0
    for i in a:
        sum += i
    return sum


#함수 2번(셀프넘버)
def d(num):
    num = num+sum(map(int, str(num)))
    return num

ls = []
for i in range(1, 10001):
    ls.append(d(i))

for i in range(1, 10001):
    if i not in ls:
        print(i)
        
#함수 3번(한수) #어려워서 일단 놔두었음.


