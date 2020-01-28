import sys
sys.stdin = open('bj17136.txt','r')

def Check(y,x,c):
    for i in range(c):
        for j in range(c):
            if not A[y+i][x+j]:return False
    return True
def Paper(y,x,c,t):
    for i in range(c):
        for j in range(c):
            A[y+i][x+j]=t
def DFS(y,x,r):
    global R
    if r==R and (y,x)!=(9,9):return
    while (y,x)!=(9,10):
        if x==10:
            y+=1
            x=0
        if A[y][x]:
            for c in range(5,0,-1):
                if not c:continue
                if y+c<=10 and x+c<=10 and List[c] and Check(y,x,c):
                    List[c]-=1
                    Paper(y,x,c,0)
                    DFS(y,x+c,r+1)
                    List[c]+=1
                    Paper(y,x,c,1)
                if c==1:return
        x+=1
    if min(R,r)==r:R=min(R,r);return
A=[[int(x)for x in input().split()]for y in range(10)]
R=987654321
List=[0,5,5,5,5,5]
DFS(0,0,0)
if R==987654321:print(-1)
else:print(R)