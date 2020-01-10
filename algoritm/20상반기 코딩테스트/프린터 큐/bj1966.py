import sys
sys.stdin = open('bj1966.txt','r')

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    L = [int(x)for x in input().split()]
    P = [int(x)for x in range(N)]
    R=0
    while True:
        if L[0]==max(L):
            R += 1
            if P[0]==M:break
            L=L[1:]
            P=P[1:]
        else:
            L+=[L.pop(0)]
            P+=[P.pop(0)]
    print(R)
