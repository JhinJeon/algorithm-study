# Hashing

# 구글링 한 코드(일부 변수 이름만 수정)
from sys import stdin

l = map(int,stdin.readline())
letters = input()
answer = 0

for i in range(l):
    answer += (ord(letters[i])-96) * (31 ** i)
print(answer % 1234567891)

# ord 함수 : 문자열의 아스키 코드 값 반환

# 이게 해시 검색이랑 연관성이 있는지, 원리가 무엇인지 잘 모르겠다.