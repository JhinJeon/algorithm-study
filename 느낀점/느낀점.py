# 20220322(재귀)
1. print(f"{text} ")
   print(f"{0}".format(text))
# 20220328(큐)
1.deque를 쓰는게 ls보다 빠르다.
2.deque를 쓸떄는 rotate(1) 은 1 2 3 4-> 4 1 2 3   # que.extendleft(que.pop())
                rotate(-1)은 1 2 3 4-> 2 3 4 1   # que.extend(que.popleft())
3.코딩테스트에서는 collections 에서 deque,stack 사용이가능
