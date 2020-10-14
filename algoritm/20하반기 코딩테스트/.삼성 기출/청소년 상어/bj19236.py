import sys
sys.stdin = open('bj19236.txt','r')

dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
def Move(F,A):
    for i in range(1,17):
        if i not in F:continue
        y,x,d=F[i]
        while (y+dy[d],x+dx[d]) not in A or A[(y+dy[d],x+dx[d])]==0:d=(d+1)%8
        Y,X=y+dy[d],x+dx[d]
        if A[(Y,X)]==-1:F[i]=(Y,X,d)
        else:F[i],F[A[(Y,X)]]=(Y,X,d),(y,x,F[A[(Y,X)]][2])
        A[(Y,X)],A[(y,x)]=i,A[(Y,X)]
def DFS(r,F,A):
    global R
    R=max(R,r)
    Move(F,A)
    y,x,d=F[0]
    for i in range(1,4):
        Y,X=y+i*dy[d],x+i*dx[d]
        if (Y,X) not in A:return
        if A[(Y,X)]==-1:continue
        f,a=F.copy(),A.copy()
        tmp=a[(Y,X)]
        a[(y,x)],a[(Y,X)],f[0]=-1,0,f.pop(tmp)
        DFS(r+tmp,f,a)
Fish={}
Area={}
for i in range(4):
    L=[int(x)for x in input().split()]
    for j in range(0,8,2):
        Fish[L[j]],Area[(i,j//2)]=(i,j//2,L[j+1]-1),L[j]
Fish[0] = Fish.pop(Area[(0, 0)])
R=Area[(0,0)]
Area[(0,0)]=0
DFS(R,Fish,Area)
print(R)