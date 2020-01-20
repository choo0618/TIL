import sys
sys.stdin=open('bj1963.txt','r')

def Find(n,s):
    ns=[]
    for i in ['0','1','2','3','4','5','6','7','8','9']:
        if not n and i=='0':continue
        ss=s[:n]+i+s[n+1:]
        if not Map[int(ss)] and s!=ss and not M[int(ss)]:
            M[int(ss)]=1
            ns.append(ss)
    return ns

Map=[0]*10001
for i in range(2,10001):
    if Map[i]:continue
    tmp=i
    while True:
        tmp+=i
        if tmp>10000:break
        Map[tmp]=1
T=int(input())
for t in range(T):
    n1,n2=map(int,input().split())
    if n1==n2:print(0);continue
    Que=[str(n1)]
    M=[0]*10001
    M[n1]=1
    R,Check=0,0
    while Que and not Check:
        R+=1
        Q=[]
        for q in Que:
            if int(q)==n2:Check=1;break
            for i in range(4):
                Q+=Find(i,q)
        Que=Q
    if Check:print(R-1)
    else:print('Impossible')