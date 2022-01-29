# 문자열 6번
# 1. 입력 단어 정의
'''
words = str(input()).lower().split(' ')
alphabet = list(words)

# 2. for 구문으로 문자 수 세기
countlist = []
for i in range(len(alphabet)) :
    countlist.append(alphabet[i])

# 3. 결과 출력
print(len(countlist))
'''
# 문자열 7번
'''
# 1. 입력 값 정의
a = str(input())
b = str(input())

# 2. a와 b 거꾸로 읽기
A = a[2]+a[1]+a[0]
B = b[2]+b[1]+b[0]

# 3. 숫자로 전환 및 대소 비교
A = int(A)
B = int(B)

if A > B :
    print(A)
else :
    print(B)
'''
# 문자열 8번
'''
dial = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
words = str(input()).lower()
time = 0
for i in range(len(words)):
    for x in dial:
        if words[i] in x:
            time += dial.index(x) + 3
print(time)
'''
# 문자열 9번
'''
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
words = input()

for i in croatia:
    words = words.replace(i,'*')

print(len(words))
'''
# 문자열 10번
'''
n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:  
        group_word += 1  # error가 0이면 그룹단어
print(group_word)
'''