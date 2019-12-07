import sys
sys.stdin = open('bj17825.txt','r')

import itertools

Dic = {0: [int(x)for x in range(0,41,2)], 10: [10,13,16,19,25,26,27,28], 20: [20,24,25,30,35,40], 25: [25,30,35,40], 30: [30,28,27,26,25,19,16,13,10]}
Dic[10] += Dic[0][Dic[0].index(30):]
Dic[30] += Dic[0][Dic[0].index(10):]

List = [int(x)for x in input().split()]
Per = list(itertools.product([1,2,3,4], repeat = 10))

R = 0

for per in Per:
    r = 0
    Map = {1: [Dic[0], 0], 2: [Dic[0], 0], 3: [Dic[0], 0], 4: [Dic[0], 0]}
    IdxMap = [0] * 41
    for l, p in List, per:
        LoadMap = Map[p][0]
        IdxMap[Map[p][1]] = 0
        Map[p][1] += l
        score = LoadMap[Map[p][1]]
        if IdxMap[score]:
            break
        IdxMap[score] = 1
        if Map[p][1] >= len(LoadMap):
            break
        r += LoadMap[Map[p][1]]
        if LoadMap[Map[p][1]] in Dic:
            LoadMap = Dic[LoadMap[Map[p][1]]]
            Map[p][1] = 0
        Map[p][0] = LoadMap
    if r > R:
        R = r
print(R)