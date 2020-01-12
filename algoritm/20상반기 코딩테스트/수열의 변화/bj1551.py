import sys
sys.stdin = open('bj1551.txt','r')

N,K=map(int,input().split())
L=input().split(',')
while K:
    l=[]
    for r in range(0,N-1):
        l.append(str(int(L[r+1])-int(L[r])))
    L=l
    N-=1
    K-=1
print(','.join(L))