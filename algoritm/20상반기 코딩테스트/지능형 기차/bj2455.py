import sys
sys.stdin = open('bj2455.txt','r')

Arr = [[int(x)for x in input().split()]for y in range(4)]
R,S=0,0
for s in Arr:
    S += s[1]
    S -= s[0]
    if R < S:R=S
print(R)