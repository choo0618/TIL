import sys
sys.stdin = open('bj17136.txt','r')

def Chk(y,x,p):
    tmp=[]
    for i in range(y,y+p):
        for j in range(x,x+p):
            if A[i][j]==0:return []
            tmp.append((i,j))
    return tmp
def DFS(y,x,r):
    global R
    while y!=10:
        if A[y][x]==0:
            x+=1
            if x==10:y,x=y+1,0
            continue
        for p in range(1,6):
            if P[p]==0 or x+p>10 or y+p>10:continue
            L=Chk(y,x,p)
            if not L:continue
            P[p]-=1
            for i,j in L:A[i][j]=0
            DFS(y,x,r+1)
            P[p]+=1
            for i,j in L:A[i][j]=1
        return
    R=min(R,r)
A=[[int(x)for x in input().split()]for y in range(10)]
P=[0,5,5,5,5,5]
R=10**9
DFS(0,0,0)
if R==10**9:R=-1
print(R)