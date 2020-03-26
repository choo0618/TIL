def solution(tickets):
    R=['ICN']
    Dic={}
    V=[0]*len(tickets)
    tickets.sort(key=lambda x:x[1])
    Check=0
    for idx,(a,b) in enumerate(tickets):
        if a in Dic:Dic[a].append((b,idx))
        else:Dic[a]=[(b,idx)]
    def DFS(a,cnt):
        global Check
        if not cnt:
            if all(V):return 1
            return 1
        if not a in Dic:return 0
        for b,i in Dic[a]:
            if V[i]:continue
            V[i]=1
            R.append(b)
            if DFS(b,cnt-1):return 1
            V[i]=0
            R.pop()
    DFS('ICN',len(tickets))
    print(R)
    return R
solution([['ICN', 'SFO'],['SFO','ICN'],['ICN','A']])
solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']])