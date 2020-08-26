from collections import defaultdict
def solution(user_id, banned_id):
    answer=set()
    Lenuser=len(user_id)
    Lenbanned=len(banned_id)
    Dic=defaultdict(list)
    Check=[0]*Lenuser
    for i,u in enumerate(user_id):
        Dic[len(u)].append((u,i))
    def Find(a,b,l):
        for i in range(l):
            if b[i]=='*':continue
            if a[i]!=b[i]:return True
        return False
    def DFS(x,List):
        if x==Lenbanned:
            print(List)
            List.sort()
            answer.add(tuple(List))
            return
        Len=len(banned_id[x])
        tmp=List[:]
        for u,i in Dic[Len]:
            if Check[i] or Find(u,banned_id[x],Len):continue
            tmp.append(i)
            Check[i]=1
            DFS(x+1,tmp)
            tmp.pop()
            Check[i]=0
    DFS(0, [])
    print(answer)
    return len(answer)
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])