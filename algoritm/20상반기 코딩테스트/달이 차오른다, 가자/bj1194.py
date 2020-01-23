import sys
sys.stdin=open('bj1194.txt','r')

# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
# Dic={'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F'}
# def IS(y,x):
#     return -1<y<N and -1<x<M
# def Check(door,key):
#     for k in key:
#         if Dic[k]==door:return True
#     return False
# N,M=map(int,input().split())
# Arr,R=[],0
# Map=[[[] for x in range(M)]for y in range(N)]
# for i in range(N):
#     I=list(map(str,input()))
#     if '0'in I:Que=[(i,I.index('0'),'',0)]
#     Arr.append(I)
# while Que and not R:
#     Q=[]
#     for q in Que:
#         if Arr[q[0]][q[1]]=='1':R=q[3];break
#         for d in range(4):
#             nY=q[0]+dy[d]
#             nX=q[1]+dx[d]
#             nC=q[2]
#             if IS(nY,nX) and Arr[nY][nX]!='#' and not q[2] in Map[nY][nX]:
#                 if Arr[nY][nX] in 'abcdef' and not Arr[nY][nX] in nC:nC+=Arr[nY][nX]
#                 if Arr[nY][nX] in 'ABCDEF':
#                     if not Check(Arr[nY][nX],nC):continue
#                 Map[nY][nX].append(nC)
#                 Q.append((nY,nX,nC,q[3]+1))
#     Que=Q
# if R:print(R)
# else:print(-1)
# print(ord('a'))
# print(ord('b'))
# print(ord('A'))
# print(ord('.'))
# print(ord('#'))



dx=[1,-1,0,0]
dy=[0,0,1,-1]
N,M=map(int,input().split())
vst=[[[-1]*M for _ in range(N)] for _ in range(1<<6)]
g=[]
ed=[]
for j in range(N):
    k=input()
    for i in range(M):
        if k[i]=='0':q=[(i,j,0)];vst[0][j][i]=0
        elif k[i]=='1':ed.append((i,j))
    g.append(k)
for x,y,key in q:
    for i in range(4):
        X,Y=x+dx[i],y+dy[i]
        if 0<=X<M and 0<=Y<N and vst[key][Y][X]<0 and g[Y][X]!='#':
            k=ord(g[Y][X])
            if 97<=k:
                vst[key|(1<<(k-97))][Y][X]=vst[key][y][x]+1
                q.append((X,Y,key|(1<<(k-97))))
            elif 65<=k:
                if key&(1<<k-65):
                    vst[key][Y][X]=vst[key][y][x]+1
                    q.append((X,Y,key))
            else:
                vst[key][Y][X]=vst[key][y][x]+1
                q.append((X,Y,key))
ans=10**9
for i in range(1<<6):
    for x,y in ed:
        if vst[i][y][x]>0:ans=min(ans,vst[i][y][x])
print(-1 if ans==10**9 else ans)