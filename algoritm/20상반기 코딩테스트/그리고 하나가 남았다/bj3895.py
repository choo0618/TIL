import sys
sys.stdin = open('bj3985.txt','r')

while True:
    N,K,M=map(int,input().split())
    if not N+K+M:break
    L=[int(x)+1for x in range(N)]
    Idx=M-1
    L.pop(Idx)
    while len(L)!=1:
        Idx-=1
        if Idx<0:Idx = len(L)-1
        tmp = K%len(L)
        Idx+=tmp
        if Idx>=len(L):Idx-=len(L)
        L.pop(Idx)
    print(L[0])