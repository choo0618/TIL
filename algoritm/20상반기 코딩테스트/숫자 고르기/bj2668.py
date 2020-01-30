import sys
sys.stdin = open('bj2668.txt','r')

def DFS(idx,List):
    global R,n
    if not R[idx]:
        R[idx]=1
        List.append(idx)
        DFS(A[idx],List)
    else:
        tmp=-1
        for l in List:
            if idx==l:tmp=1
            if tmp==1:n+=1
            R[l]=tmp


N=int(input())
A=[0]+[int(input())for _ in range(N)]
# Map=[0]*(N+1)
R=[0]*(N+1)
n=0
for i in range(1,N+1):
    if not R[i]:DFS(i,[])
print(n)
for m in range(N+1):
    if R[m]==1:print(m)