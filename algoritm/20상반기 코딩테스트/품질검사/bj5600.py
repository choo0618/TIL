import sys
sys.stdin = open('bj5600.txt','r')

a,b,c=map(int,input().split())
N=int(input())
Arr=[[int(x)for x in input().split()]for y in range(N)]
Arr.sort(key = lambda t:t[3])
Arr.reverse()
Map = [0]+[2]*(a+b+c)
for a in Arr:
    if a[3]:
        for i in range(3):Map[a[i]]=1
    else:
        B=[]
        for i in range(3):
            if Map[a[i]]==1:continue
            else:B.append(a[i])
        if len(B)==1:Map[B[0]]=0
for idx,r in enumerate(Map):
    if idx:print(r)


