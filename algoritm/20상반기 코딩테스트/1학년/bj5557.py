import sys
sys.stdin = open('bj5557.txt','r')

def DFS(x,r):
    global R
    if r>20 or r<0:return
    if x==N-2:
        if r==L[x]:R+=1
        return
    DFS(x+1,r+L[x+1])
    DFS(x+1,r-L[x+1])
N=int(input())
L=[int(x)for x in input().split()]
R=0
DFS(0,L[0])
print(R)

N=int(input())
L=[int(x)for x in input().split()]
R=0
Map=[[0]*21for __ in range(N+1)]
Map[1][L[0]]=1
for i in range(1,N):
    for j in range(21):
        if Map[i][j]:
            if j+L[i]<=20:Map[i+1][j+L[i]]+=Map[i][j]
            if j-L[i]>=0:Map[i+1][j-L[i]]+=Map[i][j]
print(Map[N-1][L[N-1]])