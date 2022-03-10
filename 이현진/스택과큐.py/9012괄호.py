import sys
t = int(input())
for i in range(t):
    count = 0
    stack = list(sys.stdin.readline().strip())
    flag = 0
    while len(stack) > 0:
        bracket = stack.pop()
        if bracket == ")":
            count += 1
        elif bracket == "(":
            if count == 0:
                print("NO")
                flag = 1
                break
            count -= 1
    if flag == 0:
        if count == 0:
            print("YES")
        else:
            print("NO")

'''
스택의 뒤에서 하나씩 괄호를 꺼내게 되는데 " ) " 를 만나면 count를 +1 해주고

" ( " 를 만나면 count를 -1 해준다.

이 때, count가 0이라는 것은 닫힌 괄호가 준비되지 않았다는 뜻이므로 NO를 출력해준다.

마지막에, 모든 괄호를 빼왔을 때도, count가 0이 아니라는 것은 짝이 맞지 않는다는 뜻이므로 NO를 출력한다.
'''