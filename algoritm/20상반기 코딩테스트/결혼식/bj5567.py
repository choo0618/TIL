import sys
sys.stdin = open('bj5567.txt','r')

N=int(input())
K=int(input())
Dic={int(x)+1:[] for x in range(N)}
for i in range(K):
    a,b=map(int,input().split())
    Dic[a].append(b)
    Dic[b].append(a)
Map=[0]*(N+1)
Map[1]=1
R,tmp=0,0
Que=[(1,0)]
while Que and tmp<2:
    Q=[]
    for q in Que:
        for d in Dic[q[0]]:
            if not Map[d]:
                Map[d]=1
                Q.append((d,q[1]+1))
    R+=len(Q)
    tmp+=1
    Que=Q
print(R)