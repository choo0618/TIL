import sys
sys.stdin = open('bj14500.txt','r')

dx=[[[1,2,3],[0,0,0]],[[1,0,1]],[[0,0,1],[0,0,-1],[-1,0,0],[1,0,0],[0,1,2],[0,1,2],[1,2,2],[1,2,2]],[[0,1,1],[0,-1,-1],[1,1,2],[1,1,2]],[[-1,0,1],[-1,0,1],[0,-1,0],[0,1,0]]]
dy=[[[0,0,0],[1,2,3]],[[0,1,1]],[[1,2,2],[1,2,2],[0,1,2],[0,1,2],[-1,0,0],[1,0,0],[0,0,1],[0,0,-1]],[[1,1,2],[1,1,2],[0,-1,-1],[0,1,1]],[[0,1,0],[0,-1,0],[-1,0,1],[-1,0,1]]]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[1]:return True
    return False
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
R=0
for i in range(L[0]):
    for j in range(L[1]):
        r=0
        for y in range(5):
            rr=0
            for dir in range(len(dx[y])):
                rrr=A[i][j]
                for ddir in range(3):
                    if IS(i+dy[y][dir][ddir],j+dx[y][dir][ddir]):rrr+=A[i+dy[y][dir][ddir]][j+dx[y][dir][ddir]]
                    else:rrr=A[i][j];break
                if rrr>rr:rr=rrr
            if rr>r:r=rr
        if r>R:R=r
print(R)
