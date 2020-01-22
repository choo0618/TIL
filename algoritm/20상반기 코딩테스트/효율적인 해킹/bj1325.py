import sys
sys.stdin = open('bj1325.txt','r')

N,M=map(int,input().split())
Dic={}
for i in range(M):
    x,y=map(int,input().split())
    try:Dic[y].append(x)
    except:
        Dic[y]=[]
        Dic[y].append(x)
R,Max=[],0
for i in range(1,N+1):
    Map=[0]*(N+1)
    Map[i]=1
    r=1
    Que=[i]
    while Que:
        Q=[]
        for q in Que:
            try:
                for hack in Dic[q]:
                    if not Map[hack]:Map[hack]=1;r+=1;Q.append(hack)
            except:pass
        Que=Q
    R.append(r)
    if r>Max:Max=r
for i in range(N):
    if R[i]==Max:print(i+1,end=' ')


