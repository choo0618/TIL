import sys
sys.stdin = open('bj9095.txt','r')

for i in range(int(input())):
    N=int(input())
    Map=[0,1,2,4]+[0]*(N-3)
    for i in range(4,N+1):Map[i]=(Map[i-3]+Map[i-2]+Map[i-1])%100000009
    print(Map[N])

