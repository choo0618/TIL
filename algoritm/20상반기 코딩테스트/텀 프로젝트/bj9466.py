import sys
sys.stdin = open('bj9466.txt','r')

import sys
sys.setrecursionlimit(10**8)
def DFS(idx,List):
    global Result
    if not R[idx]:
        List.append(idx)
        R[idx]=1
        DFS(L[idx]-1,List)
    else:
        tmp=-1
        for l in List:
            if l==idx:tmp=1
            if tmp==-1:Result+=1
            R[l]=1
for t in range(int(input())):
    N=int(input())
    L=[int(x)for x in input().split()]
    Result=0
    R=[0]*N
    for i in range(N):
        if not R[i]:DFS(i,[])
    print(Result)