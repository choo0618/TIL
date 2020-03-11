import sys
sys.stdin = open('bj1941.txt')

from collections import deque
def IS(y,x):
    return -1<y<5 and -1<x<5
def Check(List):
    Map=[[0]*5 for _ in range(5)]
    r=0
    Q=deque([List[0]])
    while Q:
        y,x=Q.popleft()
        for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
            if IS(Y,X) and not Map[Y][X]and (Y,X) in List:
                r+=1
                Map[Y][X]=1
                Q.append((Y,X))
    if r==7:return 1
    return 0
def DFS(idx,s,List):
    global R
    if len(List)==7:
        if s>=4:R+=Check(List)
        return
    for i in range(idx,25):
        y,x=i//5,i%5
        List.append((y,x))
        DFS(i+1,s+1 if A[y][x]=='S'else s,List)
        List.pop()
A=[input()for _ in range(5)]
R=0
DFS(0,0,[])
print(R)

# 시간효율 좋음
import itertools,collections
def BFS(List):
    Map=[0]*25
    Map[List[0]],r=1,1
    Q=collections.deque([List[0]])
    while Q:
        n=Q.popleft()
        if n%5==4:L=[(n-1),(n+5),(n-5)]
        elif not n%5:L=[(n+1),(n+5),(n-5)]
        else:L=[(n+1),(n-1),(n+5),(n-5)]
        for next in L:
            if -1<next<25 and not Map[next]and next in List:
                r+=1
                Map[next]=1
                Q.append(next)
    if r==7:return 1
    return 0
def Check(C):
    S=0
    for n in C:
        y,x=n//5,n%5
        S+=1 if A[y][x]=='S' else 0
    if S<4:return 1
    return 0
A=[input()for _ in range(5)]
R=0
for C in itertools.combinations(range(25),7):
    if Check(C):continue
    R+=BFS(C)
print(R)