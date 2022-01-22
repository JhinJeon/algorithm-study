# #10818
'''
from operator import index


n = int(input())
array = list(map(int, input().split()))
array.sort()
print(array[0],array[-1])
'''
#2562
'''
list = []
for i in range(9) :
    list.append(int(input()))
print(max(list))
print(list.index(max(list))+1)
'''
#2577
'''
a = int(input())
b = int(input())
c = int(input())
number = str(a*b*c)
for i in range(10) :
    print(number.count(str(i)))
'''
#3052
'''
a = set()
for i in range(10) :
    a.add(int(input())%42)

print(len(a)) 
'''
#1546
'''
N = int(input())
score = list(map(int,input().split()))

max_score = max(score)

after_score = []
for i in score:
        i = (i/max(score))*100
        after_score.append(i)
        
print(sum(after_score)/len(after_score))
# 어떤 평균을 구하는 것일까?(질문)
'''
# 8958
'''
num = int(input())

for _ in range(num):
   quiz = list(map(str, input()))
   result = 0
   score = 0

   for i in range(len(quiz)):
       if quiz[i] == 'O':
           score += 1
           result += score
       elif quiz[i] == 'X':
           score = 0

   print(result)
'''
# 4344
'''
n = int(input())

for i in range(n):
    a = list(map(int,input().split()))
    avg =(sum(a) - a[0]) / a[0]
    count = 0
    for x in a[1:]:
        if x > avg:
            count += 1
    print('%.3f%%' % ((count / a[0]) * 100))
'''
# 15596
'''
def solve(a):
    sum = 0
    for i in a :
        sum += i
    return sum
'''
#4673
'''
numbers = set(range(1, 10000))
num = set()
 
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num.add(i)
 
self_num = sorted(numbers-num)
for i in self_num:
    print(i)
'''
#1065
'''
def new_func():
    n = int(input())
    total = 0

    for i in range(1, n + 1) :
        if i < 100:
            total += 1 
        else:
            a = list(map(int, str(i)))
            if a[1] - a[0] == a[2] - a[1] :
                tatal += 1
        print(total)
'''