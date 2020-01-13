import sys
sys.stdin = open('bj5566.txt','r')

N,M = map(int,input().split())
Map = [0]+[int(input())for _ in range(N)]
Dice = [int(input())for _ in range(M)]
Idx=1
R=0
for d in Dice:
    Idx+=d
    R+=1
    if Idx>=N:break
    if Map[Idx]:
        Idx+=Map[Idx]
        if Idx>=N:break
print(R)

