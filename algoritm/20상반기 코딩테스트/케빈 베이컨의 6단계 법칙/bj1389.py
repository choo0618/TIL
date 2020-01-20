import sys
sys.stdin = open('bj1389.txt','r')

N,M=map(int,input().split())
Map=[[0]*N for _ in range(N)]
for i in range(M):
    x,y=map(int,input().split())
    Map[x-1][y-1]=1
    Map[y-1][x-1]=1
R,Sum=0,987654321
for n in range(N):
    m=[0]*N
    m[n]=1
    Que=[n]
    tmp=1
    while not all(m):
        Q=[]
        for q in Que:
            for _ in range(N):
                if Map[q][_] and not m[_]:m[_]=tmp;Q.append(_)
        tmp+=1
        Que=Q
    if sum(m)-1<Sum:
        Sum=sum(m)-1
        R=n+1
print(R)