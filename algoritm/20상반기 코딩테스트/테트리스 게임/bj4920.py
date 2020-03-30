import sys
sys.stdin = open('bj4920.txt','r')

t=1
while True:
    N=int(input())
    if not N:break
    L=[[int(x)for x in input().split()]for y in range(N)]
    Max=-10**9
    for l in range(4):
        for i in range(N-1):
            for j in range(N-2):
                Max=max(Max,max(L[i+1][j+1]+L[i+1][j+2],L[i][j+2]+L[i+1][j+2],L[i+1][j+1]+L[i][j+2])+L[i][j]+L[i][j+1])
        L=list(map(list,zip(*L[::-1])))
        if l==2 or l==3:continue
        for i in range(N):
            for j in range(N-3):
                Max=max(Max,L[i][j]+L[i][j+1]+L[i][j+2]+L[i][j+3])
        if l==1:continue
        for i in range(N-1):
            for j in range(N-1):
                Max=max(Max,L[i][j]+L[i][j+1]+L[i+1][j]+L[i+1][j+1])
    print('%d. %d'%(t,Max))
    t+=1