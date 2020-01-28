import sys
sys.stdin = open('bj1068.txt','r')

def DFS(n):
    global R
    if not len(Dic[n]):R+=1
    for i in Dic[n]:
        DFS(i)
N=int(input())
A=[int(_)for _ in input().split()]
D=int(input())
Dic={int(x):[]for x in range(N)}
for i in range(N):
    if A[i]==-1:S=i
    elif i!=D and A[i]!=D:Dic[A[i]].append(i)
R=0
if D!=S:DFS(S)
print(R)