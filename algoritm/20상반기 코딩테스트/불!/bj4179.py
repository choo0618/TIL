import sys
sys.stdin = open('bj4179.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<R and -1<x<C
R,C=map(int,input().split())
Arr=[list(map(str,input()))for y in range(R)]
J,F=[],[]
for i in range(R):
    for j in range(C):
        if Arr[i][j]=='J':J.append((i,j,'J'))
        elif Arr[i][j]=='F':F.append((i,j,'F'))
Que=F+J
r,tmp=0,0
while Que and not r:
    tmp+=1
    Q,j,f=[],[],[]
    for q in Que:
        if (q[0]==0 or q[0]==R-1 or q[1]==0 or q[1]==C-1) and q[2]=='J':r=tmp;break
        for d in range(4):
            Y,X=q[0]+dy[d],q[1]+dx[d]
            if IS(Y,X) and Arr[Y][X]!='#':
                if q[2]=='J' and Arr[Y][X]!='.':continue
                if q[2]=='F' and Arr[Y][X]=='F':continue
                Arr[Y][X]=q[2]
                Q.append((Y,X,q[2]))
    Que=Q
if r:print(r)
else:print('IMPOSSIBLE')


