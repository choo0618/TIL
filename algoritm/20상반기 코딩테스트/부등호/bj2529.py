import sys
sys.stdin = open('bj2529.txt','r')


def DFS(n,idx,List):
    if idx==N+1:
        R.append(''.join(map(str,List)))
        return
    a,b=0,10
    if idx:
        if L[idx]=='>':b=n
        else:a=n
    for i in range(a,b):
        if V[i]:continue
        V[i]=1
        List.append(i)
        DFS(i,idx+1,List)
        V[i]=0
        List.pop()

N=int(input())
L=[0]+list(map(str,input().split()))
V=[0]*10
R=[]
DFS(0,0,[])
print(R[-1])
print(R[0])