def GetSome(depth,List):
    # if len(R)==3:
    #     return
    if depth == l:
        print(result)
        return
    for i in range(l):
        if not visited[i]:
            visited[i]=True
            result[depth]=L[i]
            GetSome(depth + 1)
            visited[i] = False
L=[1,2,3,4]
visited=[0]*len(L)
result=[0]*len(L)
l=len(L)
R = []
GetSome(0,)
print(R)
