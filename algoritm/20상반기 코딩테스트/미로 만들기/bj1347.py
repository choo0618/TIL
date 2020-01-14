import sys
sys.stdin = open("bj1347.txt",'r')

Dir = [(1,0),(0,-1),(-1,0),(0,1)]
N = int(input())
S = input()
Map = [[0]*101 for _ in range(101)]
hY,hX = (50,50)
Map[hY][hX]=1
D,St,En = 0,50,50
for s in S:
    if s=='L':
        D-=1
        if D==-1:D=3
    elif s=='R':
        D+=1
        if D==4:D=0
    else:
        hY+=Dir[D][0]
        hX+=Dir[D][1]
        if hX<St:St=hX
        if hX>En:En=hX
        Map[hY][hX]=1
for m in Map:
    if any(m):
        for p in range(St,En+1):
            if m[p]:print('.',end='')
            else:print('#',end='')
        print()
