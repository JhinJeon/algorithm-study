'''정렬을 이용한 접근법
1. '책 더미'(스택)의 정보를 M회 입력 받는다.
2. '책 더미'를 입력받을 때마다 각 책 더미가 내림차순으로 정렬되어있는지 확인한다.
3. 만약 단 하나의 '책 더미'라도 내림차순 정렬되어있지 않다면, 문제에서 요구하는 정렬 연산은 불가능하다. 
4. 'is_order_possible'이라는 변수에 '정렬이 불가능하다'는 정보를 기입한다.
5. 반복문을 종료한다. 
6. '정렬' 가능 여부를 파악한다.
7. 조건에 맞게 콘솔에 출력한다.
'''   
from sys import stdin

# 1. 입력
# 1) 초기값 입력
N, M = map(int, stdin.readline().split())

# 2. 선언
# 1) is_order_possible: 정렬 가능 여부
is_order_possible = True

# 3. 연산 
for _ in range(M):
    stdin.readline()
    # 1) 책 더미 입력
    input_list = list(map(int, stdin.readline().split()))
    # 2) 책 더미의 정렬 여부 확인
    if input_list != sorted(input_list, reverse=True):
        # (1) 정렬 불가할 때 
        # 2 - 1 에 기입 후 break
        is_order_possible = False
        break

# 4. 출력
if is_order_possible:
    print('Yes')
else:
    print('No')