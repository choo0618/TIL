# N=4
# Map=[10**9]*(N+1)
# Map[1]=0
# A=[(1,2,1),(2,3,1),(3,1,1),(1,4,3),(4,5)]
# for i in range(N):
#     for s,e,d in A:
#         if Map[i]!=10**9:Map[e]=min(Map[e],Map[s]+d)
# print(Map)

def dfs(adj,node,visited,tmp):
    if (visited[node]):
        if (node == 1):
            print("found a path",tmp)
        return
    visited[node]=1
    tmp.append(node)
    for child in adj[node]:
        dfs(adj,child,visited,tmp)
    visited[node]=0
    tmp.pop()
adj = {1:[2,4],2:[3],3:[1],4:[5],5:[1]}
Cycle=[0]*6
dfs(adj, 1, [0]*6,[])