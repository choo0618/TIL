import sys
sys.stdin = open('bj3190.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
C=[3,0,1,2]
def IS(y,x):
    return -1<y<N and -1<x<N
def Move(t,c):
    global R,d
    for _ in range(t):
        y,x=S[0]
        y+=dy[d];x+=dx[d];R+=1
        if not IS(y,x) or (y,x) in S:return 0
        if _==t-1:
            if c=='D':d=(d+1)%4
            else:d=C[d]
        S.insert(0,(y,x))
        if A[y][x]:A[y][x]=0
        else:S.pop()
    return 1
N=int(input())
A=[[0]*N for _ in range(N)]
S=[(0,0)]
for a in range(int(input())):
    y,x=map(int,input().split())
    A[y-1][x-1]=1
M,tmp=[],0
K=int(input())
for m in range(K):
    t,c=map(str,input().split())
    M.append((int(t)-tmp,c))
    tmp=int(t)
R,I,d=0,0,0
while Move(M[I][0],M[I][1]):I=(I+1)%K
print(R)
