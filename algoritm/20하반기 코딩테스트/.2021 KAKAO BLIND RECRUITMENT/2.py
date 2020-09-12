from itertools import combinations
from collections import defaultdict
def Find(orders,cnt):
    Dic=defaultdict(int)
    for order in orders:
        course=combinations(order,cnt)
        for item in list(course):
            item=sorted(item)
            item=''.join(item)
            Dic[item]+=1
    SortList=sorted(Dic.items(),key=lambda x:x[1],reverse=1)
    List=[]
    if len(SortList)>0:
        key,Max=SortList[0]
        if Max>1:
            for key,value in SortList:
                if value<Max:break
                else:List.append(key)
    return List
def solution(orders, course):
    answer = []
    for n in course :
        answer+=Find(orders,n)
    answer.sort()
    return answer