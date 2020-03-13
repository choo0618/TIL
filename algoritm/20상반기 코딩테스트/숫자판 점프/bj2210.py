import sys
sys.stdin = open('bj2210.txt','r')

def DFS(y,x,s,c):
    if c==6:R.add(s);return
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if -1<Y<5 and -1<X<5:DFS(Y,X,s+A[Y][X],c+1)
A=[list(map(str,input().split())) for _ in range(5)]
R=set()
for i in range(5):
    for j in range(5):DFS(i,j,A[i][j],1)
print(len(R))