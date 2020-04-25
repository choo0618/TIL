import sys
sys.stdin = open('2382.txt','r')

dx=[0,0,-1,1]
dy=[-1,1,0,0]
def Check(l,y,x):
    for i in range(len(l)):
        if (l[i][1],l[i][2])==(y,x):return i
    return -1
def Move():
    q=[]
    while Q:
        c,y,x,d=Q.pop()
        y+=dy[d];x+=dx[d]
        if y==0 or y==N-1 or x==0 or x==N-1:
            c//=2
            if not c:continue
            d+=1
            if d==2:d=0
            elif d==4:d=2
        i=Check(q,y,x)
        if i!=-1:q[i][0]+=c
        else:q.append([c,y,x,d])
    return q
for t in range(int(input())):
    N,M,K=map(int,input().split())
    Q,R=[],0
    for k in range(K):
        y,x,c,d=map(int,input().split())
        Q.append([c,y,x,d-1])
    for m in range(M):Q.sort();Q=Move()
    for s,y,x,d in Q:R+=s
    print('#%d %d'%(t+1,R))