import sys
sys.stdin = open('bj20061.txt','r')

def Check(List,c):
    for y,x in List:
        if y+c==10 or Map[y+c][x]:return 0
    return 1
def PI(i):
    Map.pop(i)
    Map.insert(4,[0]*10)
def Game(List):
    global S,C
    tmp,p=0,0
    while Check(List,tmp):tmp+=1
    for y,x in List:
        C+=1
        Map[y+tmp-1][x]=1
    for i in range(6,10):
        if all(Map[i][:4]):
            S+=1
            C-=4
            PI(i)
    if any(Map[4]):p=2
    elif any(Map[5]):p=1
    for _ in range(p):
        C-=Map[-1].count(1)
        PI(-1)
N=int(input())
S,C=0,0
Map=[[0]*10for _ in range(10)]
for _ in range(N):
    t,y,x=map(int,input().split())
    L1,L2=[(y,x)],[(x,y)]
    if t==2:L1.append((y,x+1));L2.append((x+1,y))
    elif t==3:L1.append((y+1,x));L2.append((x,y+1))
    Game(L1)
    Map=list(map(list,zip(*Map[::])))
    Game(L2)
    Map=list(map(list,zip(*Map[::])))
print(S)
print(C)