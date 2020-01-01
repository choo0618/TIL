import sys
sys.stdin = open('bj18137.txt','r')

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[-2,-1,1,2,2,1,-1,-2]
N=int(input())
Now = [1,1,1]
p=set()
p.add(1)
while N:
    can=[]
    for dir in range(8):
        nY=Now[1]+dy[dir]
        nX=Now[2]+dx[dir]
        if nY<=0 or nX<=0:continue
        s=(nX+nY-1)*(nX+nY-2)//2+nY
        can.append([s,nY,nX])
    can.sort()
    Lan=len(p)
    check = 0
    for c in can:
        p.add(c[0])
        if Lan!=len(p):
            check=1
            Now = c
            break
    if not check:break
    N-=1
print(Now[0])