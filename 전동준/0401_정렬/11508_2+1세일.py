# 직접 작성해 본 코드
from sys import stdin

n = int(stdin.readline())
array = []

for i in range(n):
    array.append(int(stdin.readline()))

n = len(array)
for i in range(n - 1):
    for j in range(n - i - 1):
        if array[j + 1] > array[j]: #뒤의 수가 앞의 수보다 크면
            array[j + 1], array[j] = array[j], array[j +1] #앞쪽에 더 큰 수가 오도록 순서 변경

cost = 0
for k in range(n):
    if (k % 3 != 2):
        cost += array[k]
print(cost)

# 구글링 결과
#'최소비용' 이라고만 언급하고 순서를 지키라는 내용은 없으므로, 가격을 내림차순하여 정렬
'''
from sys import stdin
n=int(input())
m=list(map(int, stdin.read().split()))
m.sort(reverse=True)
cost = 0
for i in range(n):
    if(i%3!=2):
        cost += m[i]
print(cost)
'''