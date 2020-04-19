import sys
sys.stdin = open('bj6549.txt','r')

while True:
    N,*L=map(int,input().split())
    L.append(0)
    if not N:break
    S,R=[],0
    for i,n in enumerate(L):
        while S and L[S[-1]]>n:
            h=L[S.pop()]
            w=i-S[-1]-1 if S else i
            R=max(R,h*w)
        S.append(i)
    print(R)

N=int(input())
L=[int(input())for x in range(N)]+[0]
R,S=0,[]
for i,n in enumerate(L):
    while S and L[S[-1]]>n:
        h=L[S.pop()]
        w=i-S[-1]-1 if S else i
        R=max(R,h*w)
    S.append(i)
print(R)

R,S,L=0,[],[]
for i in range(int(input())+1):
    try:n=int(input())
    except:n=0
    while S and L[S[-1]]>n:
        h=L[S.pop()]
        w=i-S[-1]-1 if S else i
        R=max(R,h*w)
    S.append(i)
    L.append(n)
print(R)