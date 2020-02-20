import sys
sys.stdin = open('bj12100.txt','r')

import copy,itertools
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
Per=list(itertools.product(([0,1,2,3]),repeat=5))
for C in Per:
    M=copy.deepcopy(A)
    for c in C:
        for _ in range(c):M=list(map(list,zip(*M[::-1])))
        for y in range(N):
            for x in range(0,N-1):
                if M[y][x]:
                    for Q in range(x+1,N):
                        if M[y][Q]:
                            if M[y][x]==M[y][Q]:
                                M[y][x]*=2
                                M[y][Q]=0
                            break
        for j in range(N):
            for i in range(N-1):
                if not M[j][i]:
                    cnt=i+1
                    while cnt!=N:
                        if M[j][cnt]:
                            M[j][i]=M[j][cnt]
                            M[j][cnt]=0
                            break
                        cnt+=1
        if not c:
            for _ in range(4-c):M=list(map(list,zip(*M[::-1])))
    for y in range(N):
        for x in range(N):
            if M[y][x] and M[y][x]>R:R=M[y][x]
print(R)