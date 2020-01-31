import sys
sys.stdin= open('bj6118.txt','r')

N,M=map(int,input().split())
Map=[[]for _ in range(N)]
for i in range(M):
    x,y=map(int,input().split())
    Map[x-1].append(y-1)
    Map[y-1].append(x-1)
V=[1]+[0]*(N-1)
C=[]
Que=[0]
while Que:
    Q=[]
    for q in Que:
        for d in Map[q]:
            if not V[d]:V[d]=1;Q.append(d)
    Q.sort()
    C.append(Q)
    Que=Q
L=len(C)-1
print('%d %d %d'%(C[L-1][0]+1,L,len(C[L-1])))
