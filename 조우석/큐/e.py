from collections import deque


dq=deque([1,2,3,4,5,6,7,8,9])
# print(s.pop())
# print(s.appendleft('h')) #맨앞에 저장
# s.extendleft('h') 이것도 맨앞에저장
#print(s.pop()) # 맨뒤에꺼 뺀다
# print(s.popleft()) # 맨앞꺼 빼낸다
# print(s.index(2))
# print(s)
dq.remove(7)
dq.remove(8)
dq.remove(9)
print(dq)