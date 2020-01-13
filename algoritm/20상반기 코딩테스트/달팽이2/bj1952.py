import sys
sys.stdin = open('bj1952.txt','r')

# M,N=map(int,input().split())
# if M>N:print(2*N-1)
# else:print(2*M-2)

Dir=[(0,1),(1,0),(0,-1),(-1,0)]
def IS(y,x):
    return -1<y<M and -1<x<N
M,N = map(int,input().split())
R=0
Map=[[0]*N for _ in range(M)]
Q=[(0,0)]
d=0
while Q:
    y,x=Q.pop()
    Map[y][x]=1
    if not IS(y+Dir[d][0],x+Dir[d][1])or Map[y+Dir[d][0]][x+Dir[d][1]]:
        d += 1
        if d == 4: d = 0
        if Map[y+Dir[d][0]][x+Dir[d][1]]:break
        R += 1
    Q.append((y+Dir[d][0],x+Dir[d][1]))
print(R)
