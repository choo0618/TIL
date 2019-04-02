import sys
sys.stdin=open('input.txt','r')

# 상원이의 생일파티
def Find(x):
    if x==P[x]:return x
    else:return Find(P[x])
def Union(x,y):
    P[Find(y)]=Find(x)
T=int(input())
for n in range(T):
    L=[int(x)for x in input().split()]
    A=[[int(x)for x in input().split()]for y in range(L[1])]
    P=[0]+[0]*(L[0])
    for j in range(L[0]+1):
        P[j]=j
    for i in range(L[1]):
        Union(A[i][0],A[i][1])
    print(P)
    cnt=[]
    for c in range(len(P)):
        if Find(c):cnt.append(Find(c))
    print(cnt)
    print('#%d %d'%((n+1),len(cnt)-1))


# # 격자판의 숫자 이어 붙이기
# def DFS(x,c,r):
#     if c==7:
#         if not r in R:
#             R.append(r)
#         return
#     if x==16:return
#     DFS(x+1,c+1,r+str(L[x]))
#     DFS(x+1,c,r)
# dy=[0,1,0,-1]
# dx=[1,0,-1,0]
# def IsSafe(y,x):
#     if -1<y<4 and -1<x<4:return True
#     else: return False
# def DFS(y,x,c,r):
#     if c==8:
#         if not r in R:
#             R.append(r)
#         return
#     r+=str(A[y][x])
#     for dir in range(4):
#         newY=y+dy[dir]
#         newX=x+dx[dir]
#         if IsSafe(newY,newX):
#             DFS(newY,newX,c+1,r)
# T=int(input())
# for n in range(T):
#     A=[[int(x)for x in input().split()]for y in range(4)]
#     R=[]
#     for y in range(4):
#         for x in range(4):
#             DFS(y,x,1,'')
#     print(R)
#     print('#%d %d'%((n+1),len(R)))

# # 올림픽 종목투표
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     L1=[int(x)for x in input().split()]
#     L2=[int(x)for x in input().split()]
#     R=[0]*(L[0])
#     for y in L2:
#         t=0
#         while L1[t]>y:t+=1
#         R[t]+=1
#     print('#%d %d'%(n+1,R.index(max(R))+1))