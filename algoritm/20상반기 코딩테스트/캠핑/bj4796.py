import sys
sys.stdin = open('bj4796.txt','r')

for t in range(10**9):
    L,P,V=map(int,input().split())
    if L+P+V==0:break
    print('Case %d: %d'%(t+1,V//P*L+min(V%P,L)))