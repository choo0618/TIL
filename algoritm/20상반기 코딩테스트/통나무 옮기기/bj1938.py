import sys
sys.stdin=open('bj1938.txt','r')

# dx=[0,0,-1,1]
# dy=[-1,1,0,0]
# def IS(y,x):
#     return -1<y<N and -1<x<N and Arr[y][x]!='1'
# def Lotate(C):
#     for c in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
#         if not IS(C[0]+c[0],C[1]+c[1]):return False
#     return True
# N=int(input())
# Arr=[input()for y in range(N)]
# T,E,V=[],[],[]
# for i in range(N):
#     for j in range(N):
#         if Arr[i][j]=='B':T.append((i,j))
#         elif Arr[i][j]=='E':E.append((i,j))
# Que,Check,tmp=[T],0,0
# while Que and not Check:
#     Q=[]
#     tmp+=1
#     for t in Que:
#         if t==E:Check=1;break
#         for move in range(5):
#             nT,ch,Re=[],1,0
#             if move==4:
#                 if not Lotate(t[1]):continue
#                 if t[0][1]==t[1][1]:Re=1;lo=[(1,1),(0,0),(-1,-1)]
#                 else:lo=[(-1,1),(0,0),(1,-1)]
#                 for idx,d in enumerate(t):
#                     ny=d[0]+lo[idx][0]
#                     nx=d[1]+lo[idx][1]
#                     if IS(ny,nx):nT.append((ny,nx))
#                     else:ch=0;break
#                 if Re:nT.reverse()
#             else:
#                 for d in t:
#                     ny=d[0]+dy[move]
#                     nx=d[1]+dx[move]
#                     if IS(ny,nx):nT.append((ny,nx))
#                     else:ch=0;break
#             if ch and not nT in V:
#                 V.append(nT)
#                 Q.append(nT)
#     Que=Q
# if Check:print(tmp-1)
# else:print(0)

dx=[0,0,-1,1]
dy=[-1,1,0,0]
def IS(y,x):
    return -1<y<N and -1<x<N and Arr[y][x]!='1'
def Center(c):
    for y in range(N):
        for x in range(N):
            if Arr[y][x]==c:
                if x<N-1 and Arr[y][x+1]==c:return y,x+1,0
                else:return y+1,x,1
def Check(y,x,d):
    if not d:
        if IS(y,x-1) and IS(y,x) and IS(y,x+1):return True
        return False
    else:
        if IS(y-1,x) and IS(y,x) and IS(y+1,x):return True
        return False
def Lotate(C):
    for c in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
        if not IS(C[0]+c[0],C[1]+c[1]):return False
    return True
N=int(input())
Arr=[input() for _ in range(N)]
y,x,d=Center('B')
ty,tx,td=Center('E')
tmp,R=0,0
Map=set((y,x,d))
Que=[(y,x,d)]
while Que and not R:
    Q=[]
    tmp+=1
    while Que:
        y,x,d=Que.pop()
        if (y,x,d)==(ty,tx,td):R=tmp;break
        for dir in range(4):
            nY,nX=y+dy[dir],x+dx[dir]
            if (nY,nX,d) not in Map and Check(nY,nX,d):
                Q.append((nY,nX,d))
                Map.add((nY,nX,d))
        if (y,x,1-d) not in Map and Lotate((y,x)):
            Q.append((y,x,1-d))
            Map.add((y,x,1-d))
    Que=Q
if R:print(tmp-1)
else:print(0)



