import sys
sys.stdin = open('bj1592.txt','r')

N,M,L=map(int,input().split())
idx,R=1,0
State={}
for n in range(N):
    State[n+1]=0
while True:
    State[idx] += 1
    if State[idx] == M: break
    if State[idx]%2:
        idx+=L
        if idx>N:idx-=N
    else:
        idx-=L
        if idx<1:idx+=N
    R+=1
print(R)