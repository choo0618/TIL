import sys
sys.stdin = open('5653.txt', 'r')

dy=[-1,0,1,0]
dx=[0,1,0,-1]
def V(y,x):
    if not y:y+=1
    tmp=0
    while tmp!=len(A):
        if A[tmp][0]==1:x+=1;break
        tmp+=1
    for dir in range(4):
        nY=y+dy[dir]
        nX=x+dx[dir]
        if not M[nY][nX]:
            M[nY][nX]=M[y][x]
    M[y][x]='d'

L=[int(x)for x in input().split()]
print(L)
A=[[int(x)for x in input().split()]for y in range(L[0])]
print(A)
T=L[2]
M=[[1,1],[0,2]]
print(M)
while T:
    T-=1
    if 1 in A[0]:
        M.insert(0,[0]*len(M[0]))
    if 1 in A[-1]:
        M.append([0]*len(M[0]))
    for k in range(len(M)):
        M[k].insert(0,0)
        M[k].append(0)
    for j in range(len(A[0])):
        for i in range(len(A)):
            if A[j][i]==1:
                V(j,i)
                # A[j][i]='d'
            elif A[j][i]:
                A[j][i]-=1
