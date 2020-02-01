import sys
sys.stdin = open('bj1987.txt','r')

def IS(y,x):
    return -1<y<R and -1<x<C
def DFS(y,x,r):
    global Re
    Re=max(Re,r)
    if Re==26:return
    for d in [(0,1),(1,0),(0,-1),(-1,0)]:
        Y,X=y+d[0],x+d[1]
        if IS(Y,X) and not Map[ord(Arr[Y][X])-65]:
            Map[ord(Arr[Y][X])-65]=1
            DFS(Y,X,r+1)
            if Re==26:return
            Map[ord(Arr[Y][X])-65]=0
R,C=map(int,input().split())
Arr=[input()for _ in range(R)]
Map=[0]*26
Map[ord(Arr[0][0])-65]=1
Re=1
DFS(0,0,1)
print(Re)

# def f(x,y,v,t={}):
#     k=x,y,str(v)
#     if k in t:
#         return t[k]
#     if x<0 or y<0 or x>=R or y>=C or b[x][y] in v:
#         return 0
#     n=v+[b[x][y]]
#     t[k]=max(f(x+1,y,n),f(x,y+1,n),f(x-1,y,n),f(x,y-1,n))+1
#     return t[k]
# R,C=map(int,input().split())
# b=[list(input()) for _ in range(R)]
# print(f(0,0,[]))