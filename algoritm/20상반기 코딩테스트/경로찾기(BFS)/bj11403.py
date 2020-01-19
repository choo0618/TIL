import sys
sys.stdin = open('bj11403.txt','r')

def BFS(y,x,n):
    Que=[[y,x,n]]
    Map[y][x]='1'
    while Que:
        Q=[]
        for q in Que:
            for c in range(N):
                if A[q[1]][c] and Map[n][c]=='0':
                    Map[n][c]='1'
                    Q.append([q[1],c,n])
        Que=Q
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Map=[['0']*N for m in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] and Map[i][j]=='0':BFS(i,j,i)
for p in Map:print(' '.join(p))
