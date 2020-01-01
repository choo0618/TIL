import sys
sys.stdin = open('bj17825.txt','r')

import itertools,copy

Dic = {0: [int(x)for x in range(0,41,2)], 10: [10,13,16,19,25,30,35,40], 20: [20,22,24,25,30,35,40], 30: [30,28,27,26,25,30,35,40]}
List = [int(x)for x in input().split()]
Per = list(itertools.product([1,2,3,4], repeat=10))
R = 0

for per in Per:
    r = 0
    Map = [[0,Dic[0]]for _ in range(5)]
    for idx,p in enumerate(per):
        nMap = copy.deepcopy(Map[p])
        if not nMap or nMap==40:break
        nMap[0]+=List[idx]
        try:
            s = nMap[1][nMap[0]]
            if s==40 and 40 in Map:break
        except:
            Map[p]=0
            break
        if nMap[1]==Dic[0] and s in Dic:
            nMap[0]=0
            nMap[1]=Dic[s]
        if not nMap in Map:
            Map[p]=nMap
            if s==40:Map[p]=40
            r += s
        else:break
    if r>R:R=r
print(R)