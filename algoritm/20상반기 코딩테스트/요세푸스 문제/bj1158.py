import sys
sys.stdin = open('bj1158.txt','r')

N,K=map(int,input().split())
L=list(range(1,N+1))
I=K-1
R=[]
R.append(L.pop(I))
while L:
    I-=1
    Len=len(L)
    if I<0:I=Len-1
    tmp=K%Len
    I=(I+tmp)%Len
    R.append(L.pop(I))
print('<%s>'%(', '.join(map(str,R))))
