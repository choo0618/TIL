import sys
sys.stdin = open('bj16955.txt','r')

dx=[1,-1,-1,1,1,-1,0,0]
dy=[-1,1,-1,1,0,0,-1,1]
def IS(y,x):
    return -1<y<10 and -1<x<10
def Check(y,x):
    for d in range(8):
        Y,X=y+dy[d],x+dx[d]
        if IS(Y,X) and A[Y][X]=='X':return 1
    return 0
def Five(y,x):
    for i in [0,2,4,6]:
        cnt=1
        for d in range(i,i+2):
            Y,X=y+dy[d],x+dx[d]
            while IS(Y,X) and cnt<=5:
                if A[Y][X]=='X':cnt+=1
                else:break
                Y,X=Y+dy[d],X+dx[d]
        if cnt>=5:return 1
    return 0
A=[input()for y in range(10)]
L=[]
for i in range(10):
    for j in range(10):
        if A[i][j]=='.' and Check(i,j):L.append((i,j))
R=0
for y,x in L:
    if Five(y,x):R=1;break
print(R)