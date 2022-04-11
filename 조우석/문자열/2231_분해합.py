import sys 
N=int(sys.stdin.readline()) # 자연수 입력
# N_list=list(map(int,str(N))) # 각자리 숫자를 리스트화

for create_num in range(N+1):
    num=sum(map(int,str(create_num))) # 생성자(create_num) 자릿수 합산
    if N==(num+create_num): # 분해합 == 생성자+ 생성자자릿수
        print(create_num)
        break
    if create_num == N: # 생성자 마지막까지 못찾을떄
        print(0)


# 216 -> 198
# 분해합(216) = 생성자(198) + 생성자1의자리(8) + 생성자 10의자리(9) + 생성자 100의자리(1)
# 생성자= 분해합-생성자 1,10,100자리 
