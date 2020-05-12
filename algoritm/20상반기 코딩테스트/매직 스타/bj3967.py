import sys
sys.stdin = open('bj3967.txt','r')

def Check():
    for s in Sum:
        if sum(s)!=26:return 0
    return 1
def DFS(idx,cnt):
    global Chk
    if not cnt:
        if Check():
            Chk=1
            for p in A:print(''.join(p))
        return
    i=I[idx]
    y,x=L[i]
    Min=13
    for Y,X in Idx[i]:Min=min(Min,26-sum(Sum[Y])+1)
    for j in range(1,Min):
        if j in V:continue
        for Y,X in Idx[i]:Sum[Y][X]=j
        V[i]=j
        A[y][x]=chr(j+64)
        DFS(idx+1,cnt-1)
        if Chk:return
        V[i]=0
        A[y][x]='x'
        for Y,X in Idx[i]:Sum[Y][X]=0
A=[list(input())for _ in range(5)]
L=[-1,(0,4),(1,1),(1,3),(1,5),(1,7),(2,2),(2,6),(3,1),(3,3),(3,5),(3,7),(4,4)]
Idx=[-1,[(0,0),(1,0)],[(2,0),(3,0)],[(0,1),(2,1)],[(1,1),(2,2)],[(2,3),(4,0)],[(0,2),(3,1)],[(1,2),(4,1)],[(0,3),(5,0)],[(3,2),(5,1)],[(4,2),(5,2)],[(1,3),(5,3)],[(3,3),(4,3)]]
Sum=[[0]*4 for _ in range(6)]
V=[0]*13
al=12
I=[]
for i in range(1,13):
    y,x=L[i]
    a=A[y][x]
    if a!='.':
        if a=='x':I.append(i);continue
        tmp=ord(a)-64
        V[i]=tmp
        for Y,X in Idx[i]:Sum[Y][X]=tmp
        al-=1
Chk=0
DFS(0,al)