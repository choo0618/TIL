import sys
sys.stdin = open('bj1070.txt','r')

def BFS(c,t):
    Que=[(c,t)]
    m[c]=t
    while Que:
        Q=[]
        for q in Que:
            nt=q[1]+1
            if nt==3:nt=1
            for n in Map[q[0]]:
                if not m[n]:
                    m[n]=nt
                    Q.append((n,nt))
                if m[n] and m[n]!=nt:return False
        Que=Q
    return True
T=int(input())
for t in range(T):
    K,V=map(int,input().split())
    Map=[[]for _ in range(K)]
    for i in range(V):
        s,e=map(int,input().split())
        Map[s-1].append(e-1)
        Map[e-1].append(s-1)
    R='YES'
    m=[0]*K
    for n in range(K):
        if not m[n]:
            if not BFS(n,1):R='NO';break
    print(R)