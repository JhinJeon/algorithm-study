# 직접 구현한 코드(16번째 줄에 기술적인 문제가 있음)
from sys import stdin

n = int(stdin.readline())
serialno = []   #시리얼 넘버 저장 리스트

for x in range(n):
    serialno.append(str(stdin.readline().rstrip()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if len(serialno[j]) > len(serialno[j + 1]): # 앞 번호의 길이가 뒷 번호의 길이보다 길면
            serialno[j], serialno[j + 1] = serialno[j + 1], serialno[j] # 앞 번호와 뒷 번호의 위치 교환
        elif len(serialno[j]) == len(serialno[j + 1]):  # 앞 번호의 길이와 뒷 번호의 길이가 같으면
            for k in range(len(serialno[j])):
                if ord(serialno[j][k]) > ord(serialno[j][k+1]): # 앞 번호의 아스키 코드가 뒷 번호보다 크면 - range() 값 수정 필요(인덱스 범위 초과)
                    serialno[j], serialno[j + 1] = serialno[j + 1], serialno[j] # 앞 번호와 뒷 번호의 위치 교환

for x in range(n):
    print(serialno[x])
             

# 구글링 결과
'''
n = int(input())

serialno = []
for i in range(n):
    a = input()
    serialno.append(a)


for i in range(n-1):
    for j in range(i+1, n):
        # 짧은 것이 먼저
        if len(serialno[i]) > len(serialno[j]):
            serialno[i], serialno[j] = serialno[j], serialno[i]

        elif len(serialno[i]) == len(serialno[j]):
            suma=0
            sumb=0
            for x,y in zip(serialno[i],serialno[j]):
                if x.isdigit():
                    suma+=int(x)
                if y.isdigit():
                    sumb+=int(y)
            if suma > sumb:
                serialno[i],serialno[j] = serialno[j], serialno[i]

            elif suma == sumb:
                for x,y in zip(serialno[i], serialno[j]):   #zip : 두 개 이상의 리스트에서 원소를 하나씩 가져오기 위함
                    if x > y:
                        serialno[i],serialno[j] = serialno[j], serialno[i]
                        break
                    elif x < y:
                        break


for i in serialno:
    print(i)
'''