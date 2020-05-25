import sys
sys.stdin = open('bj10451.txt','r')

def DFS(x):
    V[x]=1
    if V[L[x]]==0:DFS(L[x])
for t in range(int(input())):
    N=int(input())
    L=[int(x)-1for x in input().split()]
    V=[0]*N
    C=0
    for i in range(N):
        if V[i]==0:DFS(i);C+=1
    print(C)