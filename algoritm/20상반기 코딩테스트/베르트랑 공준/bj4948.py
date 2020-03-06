import sys
sys.stdin = open('bj4948.txt','r')

n=123456*2+1
Map=[0,0]+[1]*n
for i in range(2,n//2):
    if not Map[i]:continue
    t=2*i
    while t<=n:
        Map[t]=0
        t+=i
while True:
    N=int(input())
    if not N:break
    print(sum(Map[N+1:2*N+1]))


