import sys
sys.stdin = open('bj3678.txt','r')

dx=[1,0,-1,-1,0,1]
dy=[-1,-2,-1,1,2,1]
def check(n):
    for d in range(6):
        nY=y+dy[d]
        nX=x+dx[d]
        if Map[nY][nX]==n:return False
    return True
T = int(input())
for t in range(T):
    N=int(input())
    Map = [[0]*301 for _ in range(301)]
    Num=[2,3,4,5]
    y,x,d=150,150,0
    Map[y][x]=1
    for _ in range(N-1):
        y+=dy[d]
        x+=dx[d]
        idx=0
        while not check(Num[idx]):
            idx+=1
            if idx==len(Num):Num+=[1,2,3,4,5]
        Map[y][x]=Num.pop(idx)
        if not Num:Num+=[1,2,3,4,5]
        if not d:
            if not Map[y-1][x-1]:d+=2
            elif not Map[y-2][x]:d+=1
        elif d==1 and not Map[y-1][x-1]:d+=1
        elif d==2 and not Map[y+1][x-1]:d+=1
        elif d==3 and not Map[y+2][x]:d+=1
        elif d==4 and not Map[y+1][x+1]:d+=1
        elif d==5 and not Map[y-1][x+1]:d+=1
        d%=6
    print(Map[y][x])