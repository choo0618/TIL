import sys
sys.stdin = open('bj13418.txt','r')

def MST():
    P=list(range(N+1))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(b)]=find(a)
    R=0
    for a,b,c in A:
        if find(a)!=find(b):R+=1 if not c else 0;union(a,b)
    return R**2
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(M+1)]
A.sort(key=lambda x:x[2])
Max=MST()
A.reverse()
Min=MST()
print(Max-Min)
