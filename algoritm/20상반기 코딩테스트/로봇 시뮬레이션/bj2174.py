import sys
sys.stdin = open('bj2174.txt','r')

Dir = [(0,1),(-1,0),(0,-1),(1,0)]
S = {'N':0,'W':1,'S':2,'E':3}
def IS(x,y):
    return 0<x<A+1 and 0<y<B+1

A,B=map(int,input().split())
N,M=map(int,input().split())
Ro,Mo=[],[]
for _ in range(N):
    ro=list(map(str,input().split()))
    ro[0],ro[1],ro[2] = int(ro[0]),int(ro[1]),S[ro[2]]
    Ro.append(ro)
for _ in range(M):
    mo=list(map(str,input().split()))
    mo[0],mo[2] = int(mo[0]),int(mo[2])
    Mo.append(mo)
for m in Mo:
    Temp = 0
    tmp = m[2]
    if m[1]!='F':tmp%=4
    Ri=m[0]-1
    while tmp and not Temp:
        if m[1]=='L':
            Ro[Ri][2]+=1
            if Ro[Ri][2]==4:Ro[Ri][2]=0
        elif m[1]=='R':
            Ro[Ri][2]-=1
            if Ro[Ri][2]==-1:Ro[Ri][2]=3
        else:
            di = Dir[Ro[Ri][2]]
            Ro[Ri][0] += di[0]
            Ro[Ri][1] += di[1]
            if not IS(Ro[Ri][0], Ro[Ri][1]):
                print("Robot %d crashes into the wall" % m[0])
                Temp = 1
                break
            for c in range(N):
                if c == Ri: continue
                if (Ro[Ri][0], Ro[Ri][1]) == (Ro[c][0], Ro[c][1]):
                    print("Robot %d crashes into robot %d" % (m[0], c + 1))
                    Temp = 1
                    break
        tmp-=1
    if Temp:break
if not Temp:print("OK")

