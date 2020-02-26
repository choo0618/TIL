import sys
sys.stdin = open('bj10819.txt','r')

def DFS(r,c,List):
    global R
    if c>0:r+=abs(List[c]-List[c-1])
    if c+1==N:
        R=max(R,r)
        return
    for i in range(N):
        if V[i]:continue
        V[i]=1
        List.append(L[i])
        DFS(r,c+1,List)
        V[i]=0
        List.pop()
N=int(input())
L=[int(x)for x in input().split()]
R,V=0,[0]*N
DFS(0,-1,[])
print(R)