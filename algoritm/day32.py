import sys
sys.stdin=open('input.txt','r')

# # 최대상금
# def yup(r):
#     for c in range(len(r)):
#         for c1 in range(c+1,len(r)):
#             r[c],r[c1]=r[c1],r[c]
#             if not int(''.join(r)) in R:R.append(int(''.join(r)))
#             r[c],r[c1]=r[c1],r[c]
# T=int(input())
# for n in range(T):
#     L=[int(x) for x in input().split()]
#     R=[L[0]]
#     for t in range(L[1]):
#         l=len(R)
#         for i in range(l):
#             a=R.pop(0)
#             yup(list(str(a)))
#     print('#%d %d'%(n+1,max(R)))

# # 정사각형
# dy=[0,1,0,-1]
# dx=[1,0,-1,0]
# def IS(y,x):
#     if -1<y<N and -1<x<N:return True
#     return False
# def DFS(y,x,c):
#     for dir in range(4):
#         ny=y+dy[dir]
#         nx=x+dx[dir]
#         if IS(ny,nx) and A[y][x]+1==A[ny][nx]:
#             V[j][i]+=1
#             DFS(ny,nx,c+1)
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[[int(x)for x in input().split()]for y in range(N)]
#     V=[[1]*N for _ in range(N)]
#     M=[0]*(N*N+1)
#     for j in range(N):
#         for i in range(N):
#             DFS(j,i,0)
#             M[A[j][i]]=V[j][i]
#     print('#%d %d %d'%(n+1,M.index(max(M)),max(M)))

# 사랑의 카운슬러
# def C(y,x):
#     global R
#     s=y*y+x*x
#     if sum(V)==N:
#         if s<R:R=s;return
#     if s>R:return
#     for i in range(N):
#         if V[i]:continue
#         for j in range(N):
#             if not V[j] and not V[i] and i!=j:
#                 V[j]=V[i]=1
#                 C(M[i][j][0]y,M[i][j][1]-x)
#                 V[j]=V[i]=0
T=int(input())
for n in range(T):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    # M=[[0]*(N) for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         M[i][j]=[A[j][0]-A[i][0],A[j][1]-A[i][1]]
    # print(M)
    # V=[0]*N
    # R=987654321987654321
    # C(0,0)
    # print('#%d %d'%(n+1,R))
    C=[['+']*(N//2)+['-']*(N//2)]
    for i in range(N//2-1):
        k=N//2-i-1
        while k!=N-i-1:
            a=C[-1].copy()
            a[k],a[k+1]=a[k+1],a[k]
            C.append(a)
            k+=1
    print(A)
    print(C)
    R=987654321987654321
    for j in range(len(C)):
        d=A.copy()
        s=[0,0]
        for l in range(N):
            if C[j][l]=='-':
                d[l][0]*=-1
                d[l][1]*=-1
            s[0]+=d[l][0]
            s[1]+=d[l][1]
        #     print(s,end=' ')
        # print()
        r=s[0]**2+s[1]**2
        if r<R:R=r
    print(n+1,R)