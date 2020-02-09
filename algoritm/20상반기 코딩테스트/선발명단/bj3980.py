import sys
sys.stdin = open('bj3980.txt','r')

def DFS(idx,r):
    global R
    if idx==11:
        R=max(R,r)
        return
    for i in range(11):
        if not A[idx][i] or V[i]:continue
        V[i]=1
        DFS(idx+1,r+A[idx][i])
        V[i]=0
for t in range(int(input())):
    A=[[int(x)for x in input().split()]for y in range(11)]
    V=[0]*11
    R=0
    DFS(0,0)
    print(R)