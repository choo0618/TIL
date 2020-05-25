import sys
sys.stdin = open('bj17143.txt','r')

dx=[0,0,0,1,-1]
dy=[0,-1,1,0,0]
# def IS(y,x):
#     return -1<y<R and -1<x<C
R,C,M=map(int,input().split())
A=[[0]*(C+1) for _ in range(R+1)]
S=[]
for i in range(M):
    r,c,s,d,z=map(int,input().split())
    s%=((R if d<=2 else C)-1)*2
    S.append([z,r,c,s,d])
    A[r][c]=z
S.sort()
r=0
for j in range(1,C+1):
    l=[]
    for i in range(1,R+1):
        if A[i][j]:
            r+=A[i][j]
            A[i][j]=0
            break
    Map=[[0]*(C+1) for _ in range(R+1)]
    for z,y,x,s,d in S:
        if A[y][x]!=z:continue
        y,x=y+s*dy[d],x+s*dx[d]
        while y<1 or y>R:
            if y<1:d,y=2,2-y
            if y>R:d,y=1,2*R-y
        while x<1 or x>C:
            if x<1:d,x=3,2-x
            if x>C:d,x=4,2*C-x
                # for n in range(s):
        #     y,x=y+dy[d],x+dx[d]
        #     if not IS(y,x):
        #         if d%2:d+=1
        #         else:d-=1
        #         y,x=y+2*dy[d],x+2*dx[d]
        Map[y][x]=z
        l.append((z,y,x,s,d))
    A,S=Map,l
print(r)
