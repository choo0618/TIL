# from collections import defaultdict
# from collections import deque
# def solution(info, query):
#     answer = []
#     Dic=defaultdict(dict)
#
#     def Insert(word, Cur):
#         cur=Cur
#         for idx,c in enumerate(word):
#             if idx==4:cur.append(int(c));return
#             if not c in cur:
#                 if idx==3:cur[c]=[]
#                 else:cur[c]={}
#             cur=cur[c]
#     def Find(Dic,q):
#         r=0
#         Q=deque([(0,Dic)])
#         while Q:
#             idx,Dic=Q.popleft()
#             if idx==4:
#                 num=int(q[idx])
#                 for n in Dic:
#                     if n>=num:r+=1
#                 continue
#             if q[idx]=='-':
#                 for v in Dic.values():
#                     Q.append((idx+1,v))
#             elif q[idx] in Dic:Q.append((idx+1,Dic[q[idx]]))
#         return r
#
#     for inf in info:
#         List=inf.split(' ')
#         Insert(List,Dic)
#
#     for q in query:
#         q=q.replace(' and ',' ').split(' ')
#         answer.append(Find(Dic,q))
#
#     return answer

Dic=[{'java':0,'cpp':1,'python':2,'-':3},{'backend':0,'frontend':1,'-':2},{'junior':0,'senior':1,'-':2},{'pizza':0,'chicken':1,'-':2}]
def solution(info, query):
    answer = []
    Map=[[[[[]for _ in range(3)]for __ in range(3)]for ___ in range(3)]for ____ in range(4)]

    def DFS(idx,tmp):
        global Map
        if idx==4:
            tmp.append(int(List[idx]))
            return
        for _ in (List[idx],'-'):
            if _=='-':
                DFS(idx+1,tmp[-1])
            else:DFS(idx+1,tmp[Dic[idx][_]])

    for inf in info:
        List=inf.split(' ')
        DFS(0,Map)
    for q in query:
        r=0
        q=q.replace(' and ',' ').split(' ')
        tmp=int(q[-1])
        for n in Map[Dic[0][q[0]]][Dic[1][q[1]]][Dic[2][q[2]]][Dic[3][q[3]]]:
            if n>=tmp:r+=1
        answer.append(r)
    print(answer)
    return answer

solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])