import sys
sys.stdin = open('bj1260.txt','r')

def DFS(n):
    print(n,end=' ')
    for i in Dic[n]:
        if not Map1[i]:
            Map1[i]=1
            DFS(i)
    return
def BFS(n):
    print(n,end=' ')
    Que=[n]
    while Que:
        Q=[]
        for q in Que:
            for i in Dic[q]:
                if not Map2[i]:
                    print(i,end=' ')
                    Map2[i]=1
                    Q.append(i)
        Que=Q
N,M,V=map(int,input().split())
Dic={int(x)+1:[]for x in range(N)}
for i in range(M):
    a,b=map(int,input().split())
    Dic[a].append(b)
    Dic[b].append(a)
for s in Dic.values():s.sort()
Map1=[0]*(N+1)
Map2=[0]*(N+1)
Map1[V],Map2[V]=1,1
DFS(V)
print()
BFS(V)

