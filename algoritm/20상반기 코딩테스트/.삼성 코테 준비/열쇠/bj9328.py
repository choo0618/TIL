import sys
sys.stdin = open('bj9328.txt','r')

# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))
# print(ord('.'))
from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<M and A[y][x]!='*'
def BFS():
    global R
    V=[[0]*M for _ in range(N)]
    Q=deque([(0,0)])
    chk=0
    while Q:
        y,x=Q.popleft()
        if A[y][x]=='$':A[y][x]='.';R+=1
        for Y, X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and V[Y][X]==0:
                tmp=ord(A[Y][X])
                if tmp>=97:K[tmp-97],A[Y][X],chk=1,'.',1
                elif tmp>=65:
                    if K[tmp-65]:A[Y][X]='.'
                    else:continue
                V[Y][X]=1
                Q.append((Y,X))
    return chk
for t in range(int(input())):
    N,M=map(int,input().split())
    A=[list('.'*(M+2))]+[list('.'+input()+'.')for y in range(N)]+[list('.'*(M+2))]
    N+=2;M+=2
    K=[0]*26
    for k in input():
        if k!='0':K[ord(k)-97]=1
    for i in range(N):
        for j in range(M):
            if 65<=ord(A[i][j])<=90 and K[ord(A[i][j])-65]:A[i][j]='.'
    R=0
    while BFS():pass
    print(R)


