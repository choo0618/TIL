import sys
sys.stdin = open('bj12100.txt','r')
def C():
    r=0
    for y in range(N):
        for x in range(N):
            if A[y][x]>r:r=A[y][x]
    return r
def DFS(x):
    global R
    if x==4:
        r=C()
        if r>R:R=r
    

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
print(N)
print(A)
R=0
DFS(0)