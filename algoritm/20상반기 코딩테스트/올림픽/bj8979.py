import sys
sys.stdin = open('bj8979.txt','r')

N,K=map(int,input().split())
L=[]
for _ in range(N):
    n,g,s,b=map(int,input().split())
    if n==K:M=(n,g,s,b)
    L.append((n,g,s,b))
R=1
for n,g,s,b in L:
    if n==K:continue
    if g>M[1]:R+=1
    elif g==M[1] and s>M[2]:R+=1
    elif g==M[1] and s==M[2] and b>M[3]:R+=1
print(R)
