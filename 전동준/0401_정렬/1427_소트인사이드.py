<<<<<<< HEAD
# 작성해 본 코드
from sys import stdin
n = str(stdin.readline().rstrip())

lst = []    #정렬할 수 있도록 문자열로 받은 후 리스트로 전환
for i in str(n):
    lst.append(int(i))

def bubble_sort(array): #버블 정렬 알고리즘을 함수 형태로 표시
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j + 1] > array[j]: #뒤의 수가 앞의 수보다 크면
                array[j + 1], array[j] = array[j], array[j +1] #앞쪽에 더 큰 수가 오도록 순서 변경
    return array

lst_str = list(map(str,lst))
print(''.join(bubble_sort(lst_str)))

# 참고한 코드(버블 정렬)
'''
# array = [8,4,6,2,9,1,3,7,5]
array = [9,8,7,6,5,4,3,2,1]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(array)

print("before: ",array)
bubble_sort(array)
print("after:", array)
'''

# 문자열로 전환한 후 리스트로 정리하는 아이디어 참고
'''
# array = [8,4,6,2,9,1,3,7,5]
array = [9,8,7,6,5,4,3,2,1]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(array)

print("before: ",array)
bubble_sort(array)
print("after:", array)
=======
# 작성해 본 코드
from sys import stdin
n = str(stdin.readline().rstrip())

lst = []    #정렬할 수 있도록 문자열로 받은 후 리스트로 전환
for i in str(n):
    lst.append(int(i))

def bubble_sort(array): #버블 정렬 알고리즘을 함수 형태로 표시
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j + 1] > array[j]: #뒤의 수가 앞의 수보다 크면
                array[j + 1], array[j] = array[j], array[j +1] #앞쪽에 더 큰 수가 오도록 순서 변경
    return array

lst_str = list(map(str,lst))
print(''.join(bubble_sort(lst_str)))

# 참고한 코드(버블 정렬)
'''
# array = [8,4,6,2,9,1,3,7,5]
array = [9,8,7,6,5,4,3,2,1]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(array)

print("before: ",array)
bubble_sort(array)
print("after:", array)
'''

# 문자열로 전환한 후 리스트로 정리하는 아이디어 참고
'''
# array = [8,4,6,2,9,1,3,7,5]
array = [9,8,7,6,5,4,3,2,1]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(array)

print("before: ",array)
bubble_sort(array)
print("after:", array)
>>>>>>> upstream/main
'''