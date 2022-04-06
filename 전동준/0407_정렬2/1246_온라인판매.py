# 직접 작성한 코드 - 예시는 맞게 나오는데 채점 결과 틀림

from sys import stdin

n,m = map(int,stdin.readline().split())
customer = []
income = []
price = []

for z in range(m):
    customer.append(int(stdin.readline()))

# 판매가 오름차순 정렬
q = len(customer)
for i in range(q-1):    # 단순 정렬 알고리즘 사용(오름차순)
    lowest = i
    for j in range(i+1, q):
        if customer[j] < customer[lowest]:
            lowest = j
        customer[i], customer[lowest] = customer[lowest], customer[i]

# 판매이익 극대화
for x in range(1,len(customer)):
    if n == 0:
        break
    else:
        wtb = customer.pop()
        price.append(wtb)
        income.append((wtb * x))
        n = n - 1

print(price[income.index(max(income))],max(income))