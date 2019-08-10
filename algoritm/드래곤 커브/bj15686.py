import sys
sys.stdin = open('bj15685.txt','r')

dx=[1,0,-1,0]
dy=[0,-1,0,1]
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
M=[[0]*101for _ in range(101)]
R=0
for a in A:
    c=0
    d=[a[2]]
    M[a[1]][a[0]]=1
    l=1
    while c!=a[3]+1:
        dd=[]
        for t in range(l):
            if d[t]==3:dd=[0]+dd
            else:dd=[d[t]+1]+dd
            a[1]+=dy[d[t]]
            a[0]+=dx[d[t]]
            M[a[1]][a[0]]=1
        c+=1
        d=dd+d
        l=len(d)-1
for y in range(100):
    for x in range(100):
        if  M[y][x] and M[y+1][x] and M[y][x+1]and M[y+1][x+1]:
            R+=1
print(R)