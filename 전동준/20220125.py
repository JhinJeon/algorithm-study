# 문자열 1번
'''
a = input()

print(ord(a))
'''
# 문자열 2번
'''
# Case 1
idcount = int(input())
numbs = str(input())
numbsid = 0
total = 0
for i in range(idcount) :
    numbsid = int(numbs[i])
    total += numbsid

print(total)

# Case 2 (정답은 아니지만 비슷한 매커니즘)
nums = map(int,input())
print(sum(nums))
'''
# 문자열 3번
'''
S = str(input()).lower()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r' 
            's','t','u','v','w','x','y','z']
alphalist = []
for i in range(len(alphabet)):
    for l in range(len(S)):
        alpha = -1
        if alphabet[i] == S[l]:
            alpha = l
            break
    alphalist.append(alpha)
print(alphalist)
'''
'''
n = list(map(str, input()))
for i in range (97,123):
    for j in range(0, len(n)):
        a = -1
        if chr(i) == n[j]:
            a = j
            break
    print(a, end=' ')

string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')
'''

# 문자열 4번
'''
n = int(input())
for i in range(n):
    x, y = input().split()
    text = ''
    for i in y:
        text += int(x) * i
    print(text)
'''

# 문자열 5번
'''
words = input().lower()
wordlist = list(set(words))
cntlist = []
for x in wordlist :
    cnt = words.count(x)
    cntlist.append(cnt)

if cntlist.count(max(cntlist)) >= 2 :
    print('?')
else :
    print(wordlist[(cntlist.index(max(cntlist)))].upper())
'''