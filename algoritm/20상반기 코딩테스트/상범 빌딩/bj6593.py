import sys
sys.stdin = open('bj6593.txt','r')

dh=[0,0,0,0,1,-1]
dx=[1,0,-1,0,0,0]
dy=[0,1,0,-1,0,0]

def IS(h,y,x):
    return -1<h<L and -1<y<R and -1<x<C

while True:
    L,R,C=map(int,input().split())
    if not L+R+C:break
    Arr=[]
    Map=[[[0]*C for _ in range(R)]for __ in range(L)]
    for l in range(L):
        A=[]
        for r in range(R):
            a=input()
            if 'S' in a:S=(l,r,a.index('S'),0)
            A.append(a)
        input()
        Arr.append(A)
    Que=[S]
    Result=0
    while Que and not Result:
        Q=[]
        for q in Que:
            for d in range(6):
                nH=q[0]+dh[d]
                nY=q[1]+dy[d]
                nX=q[2]+dx[d]
                cnt=q[3]+1
                if IS(nH,nY,nX) and (Arr[nH][nY][nX]=='.' or Arr[nH][nY][nX]=='E') and not Map[nH][nY][nX]:
                    if Arr[nH][nY][nX]=='E':Result=cnt
                    Map[nH][nY][nX]=1
                    Q.append((nH,nY,nX,cnt))
        Que=Q
    if Result:print('Escaped in %d minute(s).'%Result)
    else:print('Trapped!')
