import sys
sys.stdin=open('bj1194.txt','r')

# print(ord('a'))
# print(ord('b'))
# print(ord('A'))
# print(ord('B'))
# print(ord('.'))
# print(ord('#'))

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
N,M=map(int,input().split())
Arr,R=[],0
Map=[[[-1]*M for _ in range(N)] for _ in range(1<<6)]
for i in range(N):
    I=input()
    if '0'in I:
        idx=I.index('0')
        Que=[(i,idx,0)]
        Map[0][i][idx]=0
    Arr.append(I)
R=0
while Que and not R:
    Q=[]
    for q in Que:
        if Arr[q[0]][q[1]]=='1':R=Map[q[2]][q[0]][q[1]];break
        for d in range(4):
            Y,X=q[0]+dy[d],q[1]+dx[d]
            if IS(Y,X) and Map[q[2]][Y][X]<0 and Arr[Y][X]!='#':
                k=ord(Arr[Y][X])
                if 97<=k:
                    Map[q[2]|(1<<(k-97))][Y][X]=Map[q[2]][q[0]][q[1]]+1
                    Q.append((Y,X,q[2]|(1<<(k-97))))
                elif 65<=k:
                    if q[2]&(1<<k-65):
                        Map[q[2]][Y][X]=Map[q[2]][q[0]][q[1]]+1
                        Q.append((Y,X,q[2]))
                else:
                    Map[q[2]][Y][X]=Map[q[2]][q[0]][q[1]]+1
                    Q.append((Y,X,q[2]))
    Que=Q
if R:print(R)
else:print(-1)
