import sys
sys.stdin = open('2477.txt','r')

def Start():
    r=0
    for x in range(K):
        if not t[x][1]:w.append(t[x][0]);r+=1
        t[x][1]-=1
    return r
for tc in range(int(input())):
    N,M,K,A,B=map(int,input().split())
    a=[int(x)for x in input().split()]
    b=[int(x)for x in input().split()]
    t=[int(x)for x in input().split()]
    for i in range(K):t[i]=[i+1,t[i]]
    S,w,Sa,wb,Sb,End=0,[],[0]*N,[],[0]*M,0
    La,Lb=[0]*N,[0]*M
    RA,RB=[],[]
    while End!=K:
        if S!=K:S=Start()
        for sa in range(N):
            if Sa[sa]:Sa[sa]-=1
            if not Sa[sa] and La[sa]:wb.append(La[sa]);La[sa]=0
        while not all(Sa) and w:
            idx=Sa.index(0)
            p=w.pop(0)
            La[idx]=p
            if idx==A-1:RA.append(p)
            Sa[idx]=a[idx]
        for sb in range(M):
            if Sb[sb]:Sb[sb]-=1
            if not Sb[sb] and Lb[sb]:End+=1;Lb[sb]=0
        while not all(Sb) and wb:
            idx=Sb.index(0)
            p=wb.pop(0)
            Lb[idx]=p
            if idx==B-1 and p in RA:RB.append(p)
            Sb[idx]=b[idx]
    R=sum(RB) if RB else -1
    print('#%d %d'%(tc+1,R))