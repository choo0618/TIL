import sys
sys.stdin=open('bj5021.txt','r')

from collections import defaultdict
def DFS(n,s,d):
    tmp=0
    if n==s:return tmp+0.5**d
    for i in Dic[n]:tmp+=DFS(i,s,d+1)
    return tmp
N,M=map(int,input().split())
Dic=defaultdict(list)
K=input()
for _ in range(N):
    s,f,m=map(str,input().split())
    Dic[f].append(s)
    Dic[m].append(s)
R,d='',0
for _ in range(M):
    s=input()
    p=DFS(K,s,0)
    if p>d:R,d=s,p
print(R)