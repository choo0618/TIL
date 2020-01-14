import sys
sys.stdin = open('bj1043.txt','r')

N,M=map(int,input().split())
L = [int(x)for x in input().split()]
L=L[1:]
P = []
party = [1]*M
for I in range(M):
    i=[int(x) for x in input().split()]
    P.append(i[1:])
while True:
    tmp=1
    for idx,p in enumerate(P):
        for l in L:
            if l in p and party[idx]:
                tmp=0
                party[idx]=0
                nL = set(L)
                for know in p:
                    nL.add(know)
                L=list(nL)
                break
    if tmp:break
print(sum(party))





