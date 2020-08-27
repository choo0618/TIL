answer=set()
def Find(a,b,l):
    for i in range(l):
        if a[i]=='*':continue
        if a[i]!=b[i]:return False
    return True
def DFS(i,L,List,Len):
    global answer
    if i==Len:
        answer.add(tuple(sorted(L)))
        return
    tmp=L[:]
    for idx in List[i]:
        if idx in L:continue
        tmp.append(idx)
        DFS(i+1,tmp,List,Len)
        tmp.pop()
def solution(user_id, banned_id):
    global answer
    Lenuser=len(user_id)
    Lenbanned=len(banned_id)
    List=[]
    for i in range(Lenbanned):
        tmp,Len=[],len(banned_id[i])
        for j in range(Lenuser):
            if len(banned_id[i])==len(user_id[j]) and Find(banned_id[i],user_id[j],Len):tmp.append(j)
        List.append(tmp)
    DFS(0,[],List,Lenbanned)
    return len(answer)

# solution(["a", "b", "c", "d", "ef","fg"],["*", "**"])
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])