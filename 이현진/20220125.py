# 11654 아스키 코드
num = input()
print(ord(num))

# 11720 숫자의 합
N=int(input()) 
num_list=list(input()) 
result=0 
for i in num_list: 
    result += int(i)
print(result)

# 10809 알파벳 찾기
s = input( )
alphabet = list("abcdefghijklmnopqrstuvwxyz")
for i in alphabet:
    if i in s :
        print(s.index(i),end = '')
    else :
        print('-1',end = '')

s = input()
alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
for i in alphabet_list:
    if i in s :
        print(s.index(i), end = '')
    else:
        print('-1', end = '')

# 어디서 틀린건지.. (질문)

# 2675 문자열 반복
n = int(input())
for i in range(n):
    x, y = input().split()
    text = ''
    for i in y:
        text += int(x) * i
    print(text)

# 1157 단어 공부
