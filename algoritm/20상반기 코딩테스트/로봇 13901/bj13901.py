import sys
sys.stdin = open('bj13901.txt','r')

dx=[0,0,0,-1,1]
dy=[0,-1,1,0,0]
def IS(y,x):
    return -1<y<R and -1<x<C and not Map[y][x]
R,C=map(int,input().split())
Map=[[0]*C for _ in range(R)]
for k in range(int(input())+1):
    y,x=map(int,input().split())
    Map[y][x]=1
Dir=[int(x)for x in input().split()]
d,Len=0,len(Dir)
while True:
    tmp,cnt=[0]*4,0
    while not IS(y+dy[Dir[d]],x+dx[Dir[d]]):
        tmp[Dir[d]-1]=1
        cnt+=1
        if cnt==Len or sum(tmp)==4:break
        d=(d+1)%Len
    if cnt==Len or sum(tmp)==4:print(y,x);break
    while True:
        Y,X=y+dy[Dir[d]],x+dx[Dir[d]]
        if not IS(Y,X):break
        y,x=Y,X
        Map[y][x]=1