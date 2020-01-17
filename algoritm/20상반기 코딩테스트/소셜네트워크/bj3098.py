import sys
sys.stdin = open('bj3098.txt','r')

def Check():
    for y in range(N):
        for x in range(y+1,N):
            if not Map[y][x]:return True
    return False
N,M=map(int,input().split())
Map = [[0]*N for _ in range(N)]
for i in range(M):
    y,x=map(int,input().split())
    Map[y-1][x-1]=1
    Map[x-1][y-1]=1
day=1
R=[]
while Check():
    r=set()
    for i in range(N):
        for j in range(N):
            if Map[i][j]==day:
                for f in range(N):
                    if i!=f and Map[j][f] and not Map[i][f]:r.add((i,f))
    R.append(len(r)//2)
    day+=1
    for m in list(r):Map[m[0]][m[1]]=day
print(day-1)
for p in R:print(p)