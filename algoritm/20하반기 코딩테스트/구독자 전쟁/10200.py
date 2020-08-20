import sys
sys.stdin = open('10200.txt','r')

for t in range(int(input())):
    N,a,b=map(int,input().split())
    print('#%d %d %d'%(t+1,min(a,b),max(0,a+b-N)))