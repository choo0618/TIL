def DFS(x):
    D[x]-=1
    T[x]+=R[x]      # 현재위치까지 오는데 걸리는 최소 시간을 저장
    for i in A[x]:
        D[i]-=1
        R[i]=max(R[i],T[x])     # 현재 위치에서 필요한 최대 시간을 저장한다.
        if not D[i]:DFS(i)

N,K=map(int,input().split())
T=[0]+[int(x)for x in input().split()]
A=[[]for _ in range(N+1)]
D=[0]*(N+1)         # Depth
R=[0]*(N+1)         # 현재 시간에서 추가로 필요한 시간의 최대값
for i in range(K):
    a,b=map(int,input().split())
    A[a].append(b)
    D[b]+=1
for i in range(1,N+1):
    if not D[i]:DFS(i)
print(T[int(input())])
