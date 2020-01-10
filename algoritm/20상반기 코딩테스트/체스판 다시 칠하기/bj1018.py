import sys
sys.stdin = open('bj1018.txt','r')

C = {'W':'B','B':'W'}
def paint(y,x,color):
    c=0
    for i in range(8):
        for j in range(8):
            if (not j%2 and Arr[y+i][x+j]!=color) or (j%2 and Arr[y+i][x+j]==color):
                c+=1
        color = C[color]
    return c

N,M = map(int,input().split())
Arr = [list(map(str,input()))for y in range(N)]
R = 987654321
for i in range(0,N-7):
    for j in range(0,M-7):
        r = [paint(i,j,Arr[i][j]),paint(i,j,C[Arr[i][j]])]
        if min(r)<R:R=min(r)
print(R)
