import sys
sys.stdin = open('bj3048.txt','r')

N1,N2=map(int,input().split())
F=list(map(str,input()))
S=list(map(str,input()))
T=int(input())
Idx = T
i=0
if T>N2:
    n = F[0:T-N2]
    F = F[T-N2:]
    n.reverse()
    S+=n
    Idx = T- len(n)
while F:
    S.insert(Idx,F.pop(0))
    i+=1
    Idx = max(0,Idx-1)
    T-=1
print(''.join(S))