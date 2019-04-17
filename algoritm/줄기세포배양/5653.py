import sys
sys.stdin = open('5653.txt', 'r')

dy=[-1,0,1,0]
dx=[0,1,0,-1]

def V(y,x):
    global Q
    for dir in range(4):
        nY=y+dy[dir]
        nX=x+dx[dir]
        if not M[nY][nX]:
            A[nY][nX]=A[y][x]
            Q.append([nY,nX,A[y][x]])
T=int(input())
for n in range(T):
    L=[int(x)for x in input().split()]
    A=[[0]*(300+L[1])for _ in range(150)]+[[0]*150+[int(x)*2for x in input().split()]+[0]*150for y in range(L[0])]+[[0]*(300+L[1])for _ in range(150)]
    M=[[0]*len(A[0])for m in range(len(A))]
    for my in range(len(A)):
        for mx in range(len(A[0])):
            if A[my][mx]:M[my][mx]=A[my][mx]
    Q=[]
    while L[2]:
        L[2]-=1
        for j in range(len(A)):
            for i in range(len(A[0])):
                if M[j][i] and type(M[j][i])==int:
                    if M[j][i]==A[j][i]//2:V(j,i)
                    if M[j][i]==1:M[j][i]='d'
                    else:M[j][i]-=1
        while Q:
            tmp=Q.pop(0)
            if tmp[2]>M[tmp[0]][tmp[1]]:
                M[tmp[0]][tmp[1]]=tmp[2]
    cnt=0
    for ry in range(len(A)):
        for rx in range(len(A[0])):
            if M[ry][rx] and not M[ry][rx]=='d':cnt+=1
    print('#%d %d'%(n+1,cnt))