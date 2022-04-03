# 3번 초안
# from sys import stdin
# tanks = list(map(int,stdin.readline().split()))

# n = len(tanks)
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         attack = tanks[j] * 2
#         if tanks[i] < 0:
#             continue
#         else:
#             if tanks[j] == max(tanks):
#                 tankscp = tanks.copy()
#                 tankscp.remove(max(tankscp))
#                 val = max(tankscp)
#                 tanks[tanks.index(val)] = tanks[tanks.index(val)] - attack
#             else:
#                 tanks[tanks.index(max(tanks))] = max(tanks) - tanks[j] * 2

# print(tanks.index(max(tanks)))

#3번 수정안

from sys import stdin
a = list(map(int,stdin.readline().split()))

def solutions(tanks):
    n = len(tanks)
    checker = 0
    while checker < len(tanks) - 1:
        for j in range(n - 1):
            attack = tanks[j] * 2
            target = max(tanks)
            pointer = tanks.index(target)
            if tanks[j] < 0:
                checker += 1
                continue
            elif tanks[j] == target:
                checker = 0
                tankscp = tanks.copy()
                target = max(tankscp)
                tankscp.remove(target)
                target - max(tankscp)
                tanks[tanks.index(target)] = tanks[tanks.index(target)] - attack
            else:
                checker = 0
                tanks[pointer] = target - attack
    return tanks.index(max(tanks))

print(solutions(a))

# 1번

# import itertools
# from sys import stdin

# n = str(stdin.readline().rstrip())

# def solution(a):
#     cmd = []
#     for A,B,C,D in itertools.permutations(['L','R','U','D'],4):
#         cmd.append(A+B+C+D)
#     cmd.append('LR')
#     cmd.append('RL')
#     cmd.append('UD')
#     cmd.append('DU')
#     cnt = 0

#     for i in range(len(cmd)):
#         cnt += a.count(cmd[i])
#     return cnt

# print(solution(n))
