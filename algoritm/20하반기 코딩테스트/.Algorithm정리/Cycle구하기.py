def dfs(adj,node,visited,tmp):
    if (visited[node]):
        chk=0
        for x in tmp:
            if x==node:chk=1
            Cycle[x]=chk
        return
    visited[node]=1
    tmp.append(node)
    for child in adj[node]:
        dfs(adj,child,visited,tmp)
    visited[node]=0
    tmp.pop()
Dic = {1:[2],2:[3],3:[4],4:[2]}
Cycle=[0]*6
dfs(Dic, 1, [0]*6, [])
print(Cycle)