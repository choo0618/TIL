import sys
sys.stdin=open('input.txt','r')

# # 상원이의 생일파티
def BFS(y,x):
    global cnt
    Q.append([y,x])
    while Q:
        tmp=Q.pop(0)
        hy=tmp[0]
        hx=tmp[1]
        here=V[hy][hx]
        if here==1 or here==2:
            cnt+=1
        for i in range(2,len(M[1])):
            if M[hx][i] and not V[hx][i]:
                Q.append([hx,i])
                V[hx][i]=here+1
T=int(input())
for n in range(T):
    L=[int(x)for x in input().split()]
    A=[[int(x)for x in input().split()]for y in range(L[1])]
    M=[[0]*(L[0]+1)for _ in range(L[0]+1)]
    V=[[0]*(L[0]+1)for _ in range(L[0]+1)]
    for y in range(L[1]):
        M[A[y][0]][A[y][1]]=1
        M[A[y][1]][A[y][0]]=1
    Q=[]
    cnt=0
    for i in range(len(M[1])):
        if M[1][i]:BFS(1,i)
    print('#%d %d'%(n+1,cnt))

# # 격자판의 숫자 이어 붙이기
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