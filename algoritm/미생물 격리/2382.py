import sys
sys.stdin = open('2382.txt','r')

T=int(input())
for n in range(T):
    C=[[-1,0],[1,0],[0,-1],[0,1]]
    L=[int(x)for x in input().split()]
    A=[[int(x)for x in input().split()]for y in range(L[2])]
    while L[1]:
        for i in range(L[2]):
            A[i][0]+=C[A[i][3]-1][0]
            A[i][1]+=C[A[i][3]-1][1]
            if A[i][0]==0 or A[i][1]==0 or A[i][0]==L[0]-1 or A[i][1]==L[0]-1:
                A[i][2]//=2
                c=A[i][3]
                if c==1:A[i][3]=2
                elif c==2:A[i][3]=1
                elif c==3:A[i][3]=4
                else:A[i][3]=3
        A.sort()
        tmp=0
        for h in range(L[2]-1):
            if A[h][0]!=A[h+1][0] and tmp==0:continue
            elif A[h][0]!=A[h+1][0]:
                A[h][2]+=tmp
                tmp=0
            else:
                if A[h][1]==A[h+1][1]:
                    if A[h][2]>A[h+1][2]:
                        tmp+=A[h+1][2]
                        A[h+1][2]=0
                        A[h],A[h+1]=A[h+1],A[h]
                        if h==L[2]-2:A[h][2]+=tmp
                    else:
                        tmp+=A[h][2]
                        A[h][2]=0
                        if h==L[2]-2:A[h+1][2]+=tmp
                else:
                    A[h][2]+=tmp
                    tmp=0
        L[1]-=1
    R=0
    for s in range(L[2]):
        R+=A[s][2]
    print('#%d %d'%(n+1,R))