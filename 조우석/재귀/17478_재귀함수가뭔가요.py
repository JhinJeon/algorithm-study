import sys 
N=int(sys.stdin.readline())
text='____'
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

first_line='"재귀함수가 뭔가요?"'

second_line='"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
third_line='마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
four_line='그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
solution_line1='"재귀함수는 자기 자신을 호출하는 함수라네"'
solution_line2='라고 답변하였지.'

for i in range(N+1):
    if i==N:
        print(text*i+first_line)
        print(text*i+solution_line1)
        for j in range(i,-1,-1):
            print(text*j+solution_line2)
            


    else:
        print(text*i+first_line)
        print(text*i+second_line)
        print(text*i+third_line)
        print(text*i+four_line)
    


