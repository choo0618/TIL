import sys
sys.stdin = open('bj1587.txt','r')

nA,nB=map(int,input().split())
r=0
if nA%2 and nB%2:
    for i in range(int(input())):
        a,b=map(int,input().split())
        if a%2 and b%2:r+=1;break
print(nA//2+nB//2+r)
