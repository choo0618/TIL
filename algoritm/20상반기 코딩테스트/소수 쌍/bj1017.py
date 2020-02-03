import sys
sys.stdin = open('bj1017.txt','r')

def Prime(x):
    tmp=2*x
    while tmp<=2000:
        Pr[tmp]=1
        tmp+=x
def DFS(x):
    V[x]=1
    for i in Map[x]:
        if b[i]==-1 or (not V[b[i]] and DFS(b[i])):
            a[x]=i
            b[i]=x
            return 1
    return 0
Pr=[1,1]+[0]*1999
for i in range(2001):
    if not Pr[i]:Prime(i)
N=int(input())
L=[int(x)for x in input().split()]
A,B=[],[]
for l in L:
    if l%2:A.append(l)
    else:B.append(l)
if A[0]!=L[0]:A,B=B,A
if len(A)!=len(B):print(-1);exit(0)
LA,LB=len(A),len(B)
Map=[[]for _ in range(LA)]
for a in range(LA):
    for b in range(LB):
        if not Pr[A[a]+B[b]]:Map[a].append(b)
R=[]
for d in Map[0]:
    a=[-1]*LA
    b=[-1]*LB
    a[0]=d
    b[d]=0
    r=1
    for i in range(1,LA):
        V=[0]*LA
        V[0]=1
        if DFS(i):r+=1
    if r==LA:R.append(B[d])
R.sort()
if R:print(' '.join(map(str,R)))
else:print(-1)