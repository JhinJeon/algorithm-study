import sys
def binary_search(n)-> int:
    left=1
    right=n-1
    while True:
        mid=(left+right)//2

        if (mid**2)==n: # 제곱근^2 == 입력값 
            return mid

        elif (mid**2)>n: # (제곱근^2)가 입력값보다 크면
            right=mid    # right를 mid로 이동
        else:            # (제곱근^2)가 입력값보다 작으면
            left=mid     # left를 mid로 이동

n=int(sys.stdin.readline())
print(binary_search(n))

#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16