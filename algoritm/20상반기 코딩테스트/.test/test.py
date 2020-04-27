import sys
sys.stdin = open('test.txt','r')

for t in range(int(input())):
    p,q=map(float,input().split())
    print('#%d %s'%(t+1,'YES' if 1-p<p*(1-q) else 'NO'))