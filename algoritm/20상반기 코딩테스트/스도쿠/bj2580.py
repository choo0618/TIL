import sys
sys.stdin = open('bj2580.txt','r')

# def DFS(idx):
#     global check
#     if idx==l:
#         check=1
#         for p in A:print(' '.join(map(str,p)))
#         return
#     y,x=L[idx]
#     tmp=y//3*3+x//3
#     for n in range(1,10):
#         if Map[0][y][n] or Map[1][x][n] or Map[2][tmp][n]:continue
#         A[y][x]=n
#         Map[0][y][n]=Map[1][x][n]=Map[2][tmp][n]=1
#         DFS(idx+1)
#         A[y][x]=0
#         Map[0][y][n]=Map[1][x][n]=Map[2][tmp][n]=0
#         if check:return
# A=[[int(x)for x in input().split()]for y in range(9)]
# Map=[[[0]*10 for _ in range(9)]for __ in range(3)]
# L,l,check=[],0,0
# for i in range(9):
#     for j in range(9):
#         if not A[i][j]:L.append((i,j));l+=1;continue
#         Map[0][i][A[i][j]]=1
#         Map[1][j][A[i][j]]=1
#         Map[2][i//3*3+j//3][A[i][j]]=1
# DFS(0)

import pprint

Map=[[0]*12 for _ in range(9)]
for i in range(9):
    for j in range(12):
        Map[i][j]=i//3*3+j//3
pprint.pprint(Map)