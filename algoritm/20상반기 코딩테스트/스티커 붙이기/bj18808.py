import sys
sys.stdin = open('bj18808.txt', 'r')

# def Check(y,x,Y,X,A):
#     L=[]
#     for i in range(Y):
#         for j in range(X):
#             if A[i][j]:
#                 if Map[y+i][x+j]:return []
#                 L.append((y+i,x+j))
#     return L
# N,M,K=map(int,input().split())
# Map=[[0]*M for _ in range(N)]
# for _ in range(K):
#     a,b=map(int,input().split())
#     A=[[int(x)for x in input().split()]for y in range(a)]
#     check=0
#     for t in range(4):
#         if a>N or b>M:A=list(map(list,zip(*A[::-1])));a,b=b,a;continue
#         for i in range(N-a+1):
#             for j in range(M-b+1):
#                 L=Check(i,j,a,b,A)
#                 if not L:continue
#                 for y,x in L:Map[y][x]=1
#                 check=1
#                 break
#             if check:break
#         if check:break
#         A=list(map(list,zip(*A[::-1])))
#         a,b=b,a
# print(sum(sum(x)for x in Map))


def Check(y,x,Y,X,A):
    L=[]
    for i in range(Y):
        for j in range(X):
            if A[i][j]+Map[y+i][x+j]==2:return 0
            elif A[i][j]:L.append((y+i,x+j))
    return L
def S(a,b,A):
    r=0
    for t in range(4):
        if a>N or b>M:A,a,b=list(map(list,zip(*A[::-1]))),b,a;continue
        for i in range(N-a+1):
            for j in range(M-b+1):
                L=Check(i,j,a,b,A)
                if not L:continue
                for y,x in L:Map[y][x]=1;r+=1
                return r
        A,a,b=list(map(list,zip(*A[::-1]))),b,a
    return 0
N,M,K=map(int,input().split())
Map=[[0]*M for _ in range(N)]
R=0
for _ in range(K):
    a,b=map(int,input().split())
    A=[[int(x)for x in input().split()]for y in range(a)]
    R+=S(a,b,A)
# print(sum(sum(x)for x in Map))
print(R)