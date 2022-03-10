# 작성해 본 코드(결과가 모두 0으로 나오는 문제 발생)
t = int(input())
for i in range(t):
    a = input()
    stacked = []
    iserror = 0
    for j in range(len(a)):
        if a[j] == '(':
            stacked.append('(')
        elif a[j] == ')':
            if len(stacked) != 0:
                stacked.pop()
            else:
                iserror = 1
                break
    print('YES' if iserror==1 else 'NO')

# 구글링 결과
'''
num = int(input())

for i in range(num):
  input_data = input()
  bracket = []

  for j in input_data:
    if j == "(":
      bracket.append(j)
    elif j == ")":
      if len(bracket) != 0 and bracket[-1] == "(":
        bracket.pop()
      else:
        bracket.append(")")
        break

  if len(bracket) == 0:
    print("YES")
  else:
    print("NO")
'''