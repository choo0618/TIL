def MST():
    P=list(range(N))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    R=0
    Cnt=0       # 간선 수
    for cnt,a,b in A:
        if find(a)!=find(b):
            R+=cnt
            union(a,b)
            Cnt+=1
    if Cnt==N-1:return R    # 간선==정점-1 일때 모두 연
    
N=int(input())
A=[(c,a,b)]     # 거리를 기준으로 정렬
A.sort()