import sys
sys.stdin = open('bj20056.txt','r')

# from collections import deque
# dx=[0,1,1,1,0,-1,-1,-1]
# dy=[-1,-1,0,1,1,1,0,-1]
# def Move():
#     for k in range(LMap[i][j]):
#         m,s,d=Map[i][j].popleft()
#         y,x=(i+s*dy[d])%N,(j+s*dx[d])%N
#         if y<0:y%N
#         if x<0:x%=N
#         tMap[y][x]+=1
#         Map[y][x].append((m,s,d))
# def Split(L):
#     global R
#     M,S,D=0,0,0
#     for _ in range(L):
#         m,s,d=Map[i][j].popleft()
#         M+=m;S+=s;D+=d%2
#     R-=M
#     M//=5;S//=L
#     if M==0:return 0
#     Dir=[0,2,4,6]
#     if D!=L and D!=0:Dir=[1,3,5,7]
#     for d in Dir:Map[i][j].append((M,S,d));R+=M
#     return 4
# N,M,K=map(int,input().split())
# Map=[[deque()for _ in range(N)]for _ in range(N)]
# LMap=[[0]*N for _ in range(N)]
# R=0
# for _ in range(M):
#     r,c,m,s,d=map(int,input().split())
#     Map[r-1][c-1].append((m,s,d))
#     LMap[r-1][c-1]+=1
#     R+=m
# while K:
#     tMap=[[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if LMap[i][j]:Move()
#     for i in range(N):
#         for j in range(N):
#             if tMap[i][j]>=2:tMap[i][j]=Split(tMap[i][j])
#     LMap=tMap
#     K-=1
# print(R)


from collections import defaultdict
dx=[0,1,1,1,0,-1,-1,-1]
dy=[-1,-1,0,1,1,1,0,-1]
def Split(k,L):
    global R
    Len,M,S,D=len(L),0,0,0
    for y,x,m,s,d in L:
        R-=m;M+=m;S+=s;D+=d%2
    tDic[k].clear()
    M//=5;S//=Len
    if M==0:return
    Dir=[0,2,4,6]
    if D!=Len and D!=0:Dir=[1,3,5,7]
    for d in Dir:tDic[k].append((y,x,M,S,d));R+=M
N,M,K=map(int,input().split())
R=0
Dic=defaultdict(list)
for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    R+=m
    Dic[(r-1,c-1)].append((r-1,c-1,m,s,d))
while K:
    tDic=defaultdict(list)
    for l in Dic.values():
        for y,x,m,s,d in l:
            y,x=(y+s*dy[d])%N,(x+s*dx[d])%N
            if y<0:y%N
            if x<0:x%=N
            tDic[(y,x)].append((y,x,m,s,d))
    for k,l in tDic.items():
        if len(l)>=2:Split(k,l)
    Dic=tDic
    K-=1
print(R)
