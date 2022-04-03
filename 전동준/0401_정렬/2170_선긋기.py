#구글링 결과
#선 긋기나 2차원 면적 계산 같은 문제는 어떻게 푸는지 감을 못 잡겠다
import sys
input = sys.stdin.readline
 
N = int(input())
lines = []
 
for _ in range(N):
    s, n = map(int, input().split())
    lines.append((s, n))
 
lines.sort()
ans = 0
bS = bE = 0
 
for s, e in lines:
    if not ans:
        ans = abs(e - s)
        bS = s
        bE = e
        continue
 
    if bS <= s and bE >= e:
        continue
    
    ans += abs(e - s)
 
    if bE > s:
        ans -= abs(bE - s)
    
    bS = s
    bE = e
 
print(ans)