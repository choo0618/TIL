import sys
sys.stdin = open('bj17136.txt', 'r')

def Check(y,x,s):
    for i in range(y,y+s):
        for j in range(x,x+s):
            if not A[i][j]:return 1
    return 0
def P(y,x,s,t):
    for i in range(y,y+s):
        for j in range(x,x+s):A[i][j]=t
def DFS(y,x,r):
    global R
    if r>=R:return
    while y<10:
        while x<10:
            if A[y][x]:
                for s in range(5,0,-1):
                    if not S[s] or y+s>10 or x+s>10 or Check(y,x,s):continue
                    P(y,x,s,0)
                    S[s]-=1
                    DFS(y,x+s,r+1)
                    P(y,x,s,1)
                    S[s]+=1
                return
            x+=1
        x=0
        y+=1
    R=min(R,r)
A=[[int(x)for x in input().split()]for y in range(10)]
S=[0,5,5,5,5,5]
R=26
DFS(0,0,0)
print(R if R!=26 else -1)