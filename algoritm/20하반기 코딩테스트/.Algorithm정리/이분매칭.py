# N>>B 1:1로 매칭시키
# R : 매칭 수
def DFS(x):
    V[x]=1
    for a in Map[x]:
        if B[a]==-1 or (not V[B[a]] and DFS(B[a])):
            A[x]=a
            B[a]=x
            return 1
    return 0

N=int(input())
M=int(input())
Map=[[1,2,3,4,5],[],[],[]]  # Map[x] : x 가 갈수있는 위치
A=[-1]*N
B=[-1]*M
R=0
for n in range(N):
    V=[0]*N
    if DFS(n):
        R+=1