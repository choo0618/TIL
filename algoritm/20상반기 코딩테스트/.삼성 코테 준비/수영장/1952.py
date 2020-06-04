import sys
sys.stdin = open('1952.txt','r')

for t in range(int(input())):
    d,m,q,y=map(int,input().split())
    DP=[0]*3+[int(x)for x in input().split()]
    for i in range(3,15):
        DP[i]=min(DP[i-3]+q,DP[i-1]+min(DP[i]*d,m))
    print('#%d %d'%(t+1,min(y,DP[-1])))