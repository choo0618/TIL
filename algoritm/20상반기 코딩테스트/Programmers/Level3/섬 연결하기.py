def MST(n,List):
    P=list(range(n))
    def find(x):
        if P[x]!=x:return find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    R=0
    for a,b,c in List:
        if find(a)!=find(b):R+=c;union(a,b)
    return R

def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    return MST(n,costs)
print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))