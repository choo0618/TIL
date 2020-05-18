import sys
sys.stdin = open('bj15685.txt','r')

dx=[1,0,-1,0]
dy=[0,-1,0,1]
Map=[[0]*101 for y in range(101)]
R=0
for t in range(int(input())):
    x,y,d,g=map(int,input().split())
    Map[x][y]=1
    x+=dx[d];y+=dy[d]
    Map[x][y]=1
    D=[d]
    for _ in range(g):
        tmp=[]
        for d in D:
            d=(d+1)%4
            x+=dx[d];y+=dy[d]
            Map[x][y]=1
            tmp.append(d)
        tmp.reverse()
        D=tmp+D
for i in range(100):
    for j in range(100):
        R+=Map[i][j]==Map[i][j+1]==Map[i+1][j]==Map[i+1][j+1]==1
print(R)

dx=[1,0,-1,0]
dy=[0,-1,0,1]
Map=[[0]*101 for y in range(101)]
R=0
for t in range(int(input())):
    x,y,d,g=map(int,input().split())
    Map[x][y]=1
    D=[d]
    for i in range(g):
        for j in range(len(D)-1,-1,-1):
            D.append((D[j]+1)%4)
    for d in D:
        x+=dx[d];y+=dy[d]
        Map[x][y]=1
for i in range(100):
    for j in range(100):
        R+=Map[i][j]==Map[i][j+1]==Map[i+1][j]==Map[i+1][j+1]==1
print(R)