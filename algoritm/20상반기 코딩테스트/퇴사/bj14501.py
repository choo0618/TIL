import sys
sys.stdin = open('bj14501.txt','r')

# def DFS(x,d,m):
#     global R
#     if x==N-1 and d==1 or x+d==N:
#         m+=A[x][1]
#         if R<m:R=m
#         return
#     if x+d>N-1:
#         if R<m:R=m
#         return
#     for _ in range(x+d,N):
#         DFS(_,A[_][0],m+A[x][1])
# N=int(input())
# A=[[int(x)for x in input().split()]for y in range(N)]
# R=0
# for _ in range(N):
#     DFS(_,A[_][0],0)
# print(R)

N=int(input())
Map=[0]*1500051
for i in range(N):
    d,p=map(int, input().split())
    Map[i+1]=max(Map[i],Map[i+1])
    Map[i+d]=max(Map[i]+p, Map[i+d])
print(Map[N])