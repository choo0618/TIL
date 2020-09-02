from collections import deque
def MST(List,N):
    if N==2:return 0
    P=list(range(N))
    def Find(x):
        if P[x]!=x:P[x]=Find(P[x])
        return P[x]
    def Union(a,b):
        P[a]=b
    R,cnt=0,0
    for d,a,b in List:
        A,B=Find(a),Find(b)
        if A!=B:
            R+=d
            cnt+=1
            Union(A,B)
            if cnt==N-2:return R

def solution(land, height):
    N=len(land)
    Map=[[0]*N for _ in range(N)]
    tmp=1
    def BFS(y,x,tmp):
        Map[y][x]=tmp
        Q=deque([(y,x)])
        while Q:
            y,x=Q.popleft()
            for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
                if -1<Y<N and -1<X<N and Map[Y][X]==0 and abs(land[Y][X]-land[y][x])<=height:
                    Q.append((Y,X))
                    Map[Y][X]=tmp
    for i in range(N):
        for j in range(N):
            if Map[i][j]==0:BFS(i,j,tmp);tmp+=1
    List=set()
    for i in range(N):
        for j in range(N):
            for I,J in (i,j+1),(i+1,j),(i,j+1),(i+1,j):
                if -1<I<N and -1<J<N and Map[i][j]!=Map[I][J]:
                    List.add((abs(land[i][j]-land[I][J]),min(Map[i][j],Map[I][J]),max(Map[i][j],Map[I][J])))
    return MST(sorted(List),tmp)

solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1)
solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)