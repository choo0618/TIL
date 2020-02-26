import sys
sys.stdin = open('bj10974.txt','r')

def DFS(c,List):
    if c==N:
        print(' '.join(map(str,List)))
        return
    for i in range(N):
        if V[i]:continue
        List.append(i+1)
        V[i]=1
        DFS(c+1,List)
        List.pop()
        V[i]=0
N=int(input())
V=[0]*N
DFS(0,[])