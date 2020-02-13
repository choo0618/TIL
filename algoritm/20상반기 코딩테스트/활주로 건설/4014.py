import sys
sys.stdin = open('4014.txt','r')

def Check(List):
    idx,Map=0,[0]*N
    while idx!=N-1:
        if List[idx]==List[idx+1]:idx+=1;continue
        elif abs(List[idx]-List[idx+1])>=2:return 0
        elif List[idx]>List[idx+1]:a,b,c=idx+1,idx+X,1
        else:a,b,c=idx,idx-X+1,-1
        for t in range(a,b,c):
            if t+c==-1 or t+c==N or List[t]!=List[t+c] or Map[t] or Map[t+c]:return 0
            Map[t]=1
        if c==1:idx+=X;Map[idx]=1
        else:idx+=1;Map[idx-X]=1
    return 1
for t in range(int(input())):
    N,X=map(int,input().split())
    A=[[int(x)for x in input().split()]for y in range(N)]
    A+=list(map(list,zip(*A[::-1])))
    R=0
    for a in A:R+=Check(a)
    print('#%d %d'%(t+1,R))