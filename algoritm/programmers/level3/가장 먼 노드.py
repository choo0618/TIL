def solution(n, edge):
    answer = [0]*(n+1)
    Map=[[] for i in range(len(edge)+1)]
    for i in range(len(edge)):
        if not edge[i][1] in Map[edge[i][0]]:
            Map[edge[i][0]].append(edge[i][1])
            Map[edge[i][0]].sort()
        if not edge[i][0] in Map[edge[i][1]]:
            Map[edge[i][1]].append(edge[i][0])
            Map[edge[i][1]].sort()
    answer[0],answer[1]= -1,-1
    Q=[1]
    c=1
    while not all(answer):
        temp=[]
        for start in Q:
            for i in Map[start]:
                if answer[i] ==0:
                    answer[i]+=c
                    temp.append(i)
        Q=temp
        c+=1
    ans=answer.count(max(answer))
    return ans