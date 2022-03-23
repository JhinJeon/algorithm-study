import queue
import sys
num = int(sys.stdin.readline())
queue = []
result = []
for i in range(num):
    keyword = list(sys.stdin.readline().split())
    if keyword[0] == 'push':
        queue.append(keyword[1])
    elif keyword[0] == 'front':
        if len(queue) == 0:
           result.append(-1)
        else:
            result.append(queue[0])

    elif keyword[0] == 'back':
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[-1])

    elif keyword[0] == 'size':
        result.append(len(queue))
    elif keyword[0] == 'empty':
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif keyword[0] == 'pop':
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])
            queue.pop(0)

for _ in result:
    print(_)
