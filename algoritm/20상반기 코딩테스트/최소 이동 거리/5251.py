import sys
sys.stdin = open('5251.txt','r')

for t in range(int(input())):
    N,E=map(int,input().split())
    Map=[[]for _ in range(N+1)]
    for i in range(E):
        s,e,w=map(int,input().split())
        Map[s].append((e,w))
    R=[0]+[10**9]*N
    Q=[(0,0)]
    while Q:
        now,l=Q.pop()
        for next,c in Map[now]:
            if l+c>=R[next]:continue
            R[next]=l+c
            Q.append((next,l+c))
    print('#%d %d'%(t+1,R[N]))
