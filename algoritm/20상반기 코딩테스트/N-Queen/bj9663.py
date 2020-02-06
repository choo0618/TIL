import sys
sys.stdin = open('bj9663.txt','r')

def IS(y,x):
    return -1<y<N and -1<x<N
def Check(y,x,d):
    List=[]
    while True:
        y+=d[0]
        x+=d[1]
        if IS(y,x):
            if not Map[y][x]:List.append((y,x));Map[y][x]=1
        else:break
    return List
def DFS(i):
    global R
    if i==N:
        R+=1
        return
    for m in range(N):
        if Map[i][m]:continue
        C=[(i,m)]
        Map[i][m]=1
        for d in [(0,1),(1,1),(1,0),(1,-1),(0,-1)]:C+=Check(i,m,d)
        DFS(i+1)
        for c in C:Map[c[0]][c[1]]=0
    return
N=int(input())
Map=[[0]*N for _ in range(N)]
R=0
DFS(0)
print(R)

