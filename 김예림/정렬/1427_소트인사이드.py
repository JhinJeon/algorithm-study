import sys
s=sys.stdin.readline().strip()
num=[]
for i in s:
    num.append(int(i)) #한자리씩 배열에 넣기

def QuickSort(arr): # 퀵소트
    if len(arr)<=1:
        return arr
    pivot,tail=arr[0],arr[1:] #피봇=배열의 첫번째 값, tail은 나머지값

    leftSide=[x for x in tail if x <= pivot] #피봇보다 작은 값들 넣을 배열 
    rightSide = [x for x in tail if x > pivot] #피봇보다 큰 값을 넣을 배열

    return QuickSort(rightSide)+[pivot]+QuickSort(leftSide) 
    #재귀적으로 왼쪽,오른쪽배열 계속 정렬(이 문제에선 내림차순이기 때문에 왼쪽에 rightSide가옴!)

answer=QuickSort(num)
for i in answer: #정답 출력
    print(i,end='')
