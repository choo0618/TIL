import sys
sys.stdin = open('1952.txt','r')

# def DFS(m,c,r):
#     global R
#     if r>=R:return
#     if c==Sum:
#         R=min(R,r)
#         return
#     for i in range(m,12):
#         if not C[i]:continue
#         DFS(i+1,c+C[i],r+C[i]*M[0])
#         DFS(i+1,c+C[i],r+M[1])
#         DFS(i+3,c+sum(C[i:i+3]),r+M[2])
# for t in range(int(input())):
#     M=[int(x)for x in input().split()]
#     C=[int(x)for x in input().split()]+[0,0]
#     Sum=sum(C)
#     R=10**9
#     DFS(0,0,0)
#     print('#%d %d'%(t+1,min(R,M[3])))


for t in range(int(input())):
    d,m,q,y=map(int,input().split())
    DP=[int(x)for x in input().split()]+[0,0,0]
    for i in range(12):
        DP[i]=min(min(DP[i-1]+DP[i]*d,DP[i-1]+m),DP[i-3]+q)
    print('#%d %d'%(t+1,min(DP[11],y)))