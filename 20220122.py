# 배열 1번
'''
count = int(input())
array = list(map(int,input().split()))

print(min(array))
print(max(array))
'''
# 배열 2번
'''
array = []
for m in range(9) :
    array.append(int(input()))

print(max(array))
key = 0
for i in range(9) :
    if key < array[i] :
        key = i
print(key)
'''
# 배열 3번
'''
array = []
for m in range(3) :
    array.append(int(input()))

a = array[0]
b = array[1]
c = array[2]

abc = a * b * c
abc = str(abc)

for r in range(10) :
    print(abc.count(str(r)))
'''

# 배열 4번
'''
x = []
# for i in range(10) :
#     x.append(int(input()))

# num = len(x)
# for j in range(10) :
#     if x[j] == y :
#         num -= 1

import sys

for i in range(10) :
    x.append(int(sys.stdin.readline().rstrip()) % 42)
print(len(set(x)))
'''

#배열 5번
'''
num = int(input())
testlist = []

testlist = list(map(int,input().split()))

newavg = []
for a in range(num) :
    newavg.append(100 * testlist[a] / max(testlist))

print(sum(newavg) / len(newavg))
'''

#배열 6번
'''
test_case = int(input())
 
for i in range(test_case):
    oxList = list(input())
    score = 0
    total_score = 0
    for i in oxList:
        if i == 'O':
            score += 1
            total_score += score
        else:
            score = 0
    print(total_score)
'''
#배열 7번
'''
testcase = int(input())

for i in range(testcase):    
    count = 0
    for x in range(len(studentlist)) :
        studentlist = list(map(int,input().split()))
        if (100 * sum(studentlist) / len(studentlist)) < studentlist[x] :
            count += 1
    print(100 * count / len(studentlist))

    C = int(input())
'''
'''
for i in range(C):
    scoreList = list(map(int, input().split()))
    scoreAvg = sum(scoreList[1:]) / scoreList[0]
    student = 0
 
    for j in scoreList[1:]:
        if j > scoreAvg:
            student += 1
    studentAvg = student/scoreList[0] * 100
    print(format(studentAvg, '.3f')+'%')
'''
# 함수 1
'''
def solve(a) :
    return sum(a)

solve
# 질문 : 이게 뭐 하는 문제인지 이해가 잘 안간다
'''

# 함수 2
'''
numbers = list(range(1, 10_001))
remove_list = []  # 이후에 삭제할 숫자 list
for num in numbers :
    for n in str(num):
        num += int(n)  # 생성자가 있는 숫자
    if num <= 10_000:  # 10,000보다 작거나 같을 때만,
        remove_list.append(num)  # append: 리스트에 요소를 추가할 때

for remove_num in set(remove_list) :  # set 으로 중복값 제거
    numbers.remove(remove_num)
for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
    print(self_num)
'''
#함수 3
'''
num = int(input())

hansu = 0
for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1  # 100보다 작으면 모두 한수
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1  # x의 각 자리가 등차수열이면 한수
print(hansu)

'''