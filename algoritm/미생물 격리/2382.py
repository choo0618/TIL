import sys
sys.stdin = open('2382.txt','r')

C=[[-1,0],[1,0],[0,-1],[0,1]]
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[2])]
print(L)
print(A)
while L[2]:
    for i in range(L[2]):
        A[i][0]+=C[A[i][3]-1][0]
        A[i][1]+=C[A[i][3]-1][1]
        if A[i][0]==0 or A[i][1]==0 or A[i][0]==L[0]-1 or A[i][1]==L[0]-1:
            A[i][2]//=2
            c=A[i][3]
            if c==1:A[i][3]=2
            elif c==2:A[i][3]=1
            elif c==3:A[i][3]=4
            else:A[i][3]=3

    L[2]-=1