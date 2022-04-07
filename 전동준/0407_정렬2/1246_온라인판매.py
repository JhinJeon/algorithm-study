# 작성한 코드
# 예제와 임의로 선정한 테스트 케이스는 맞게 나오는데 채점 결과 틀림

from sys import stdin

n,m = map(int,stdin.readline().split())
customer = []   # 소비자의 희망구매가
income = [] # 판매 수익(가격 * 수량)
price = []  # 판매 가격

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
        break   # 판매할 계란이 없으면 for loop 종료
    else:
        wtb = customer.pop()    # customer 리스트에서 최고가부터 값 추출
        price.append(wtb)   # 소비자의 희망구매가 저장
        income.append((wtb * x))    # 희망 구매가 * 구매하는 소비자 값 저장
        n = n - 1

# 결과 표시 - 이익 최대값 인덱스로 판매가 출력, 이익 최대값 출력
print(price[income.index(max(income))],max(income))