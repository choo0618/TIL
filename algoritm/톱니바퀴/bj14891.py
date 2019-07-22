import sys
sys.stdin = open('bj14891.txt','r')

T=[list(int(x) for x in input()) for y in range(4)]
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
for t in A:
    m=[0]*3
    H=[0]*4
    for c in range(3):
        if T[c][2]!=T[c+1][6]:m[c]=1
    H[t[0]-1]=t[1]
    for f in range(3):
        if H[f] and m[f]:H[f+1]=-H[f]
    for b in range(-1,-4,-1):
        if H[b] and m[b]:H[b-1]=-H[b]
    for h in range(4):
        if H[h]==1:T[h].insert(0,T[h].pop(-1))
        elif H[h]==-1:T[h].append(T[h].pop(0))
print(T[0][0]+2*T[1][0]+4*T[2][0]+8*T[3][0])