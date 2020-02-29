import sys
sys.stdin = open('bj10218.txt','r')

from collections import deque
Dir={'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
def move(y,x,c):
    dy,dx=Dir[c]
    while A[y][x]!='#':
        y+=dy;x+=dx
        if A[y][x]=='O':return (y,x)
    return (y-dy,x-dx)
for t in range(int(input())):
    N,M=map(int,input().split())
    A=[input()for _ in range(N)]
    L=set()
    for i in range(N):
        for j in range(M):
            if A[i][j]=='.':L.add((i,j))
    Q=deque([(L,'')])
    R='XHAE'
    while Q:
        l,S=Q.popleft()
        if not len(l):R=S;break
        if len(S)==10:continue
        for c in 'LRUD':
            s,Set=S+c,set()
            for i,j in l:
                Y,X=move(i,j,c)
                if A[Y][X]!='O':Set.add((Y,X))
            if Set!=l:Q.append((Set,s))
    print(R)

