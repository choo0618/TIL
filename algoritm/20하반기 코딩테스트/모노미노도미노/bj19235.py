import sys
sys.stdin = open('bj19235.txt','r')

def IS(y,x):
    return -1<y<10 and -1<x<10
def Cnt(List):
    c=0
    while True:
        c+=1
        for y,x in List:
            if not IS(y+c,x) or Map[y+c][x]:return c-1
    return c
def Check():
    for i in range(9,3,-1):
        for j in range(4):
            if not Map[i][j]:continue
            tmp,b=Map[i][j],[(i,j)]
            Map[i][j]=0
            for y,x in (i,j+1),(i+1,j),(i,j-1),(i-1,j):
                if IS(y,x) and Map[y][x]==tmp:b.append((y,x));Map[y][x]=0;break
            cnt=Cnt(b)
            for y,x in b:Map[y+cnt][x]=tmp
def Play(List,n):
    global S,B
    cnt=Cnt(List)
    for y,x in List:Map[y+cnt][x]=n
    while True:
        tmp=S
        for i in range(9,3,-1):
            if all(Map[i][:4]):S+=1;B-=4;Map.pop(i)
        if S==tmp:break
        for _ in range(S-tmp):Map.insert(4,[0]*10)
        Check()
    if any(Map[4][:4]):tmp=2
    elif any(Map[5][:4]):tmp=1
    else:return
    for _ in range(tmp):
        B-=10-Map[-1].count(0)
        Map.pop()
        Map.insert(4,[0]*10)
S,B,Map=0,0,[[0]*10 for _ in range(10)]
for n in range(1,int(input())+1):
    t,y,x=map(int,input().split())
    B+=2
    B1,B2=[(y,x)],[(x,y)]
    if t==2:B1.append((y,x+1));B2.append((x+1,y));B+=2
    elif t==3:B1.append((y+1,x));B2.append((x,y+1));B+=2
    Play(B1,n)
    Map=list(map(list,zip(*Map[::])))
    Play(B2,n)
    Map=list(map(list,zip(*Map[::])))
print(S)
print(B)