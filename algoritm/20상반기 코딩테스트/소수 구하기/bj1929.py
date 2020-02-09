import sys
sys.stdin=open('bj1929.txt','r')

M,N=map(int,input().split())
*s,=range(N+1)
for i in s[2:]:
    if s[i]:
        s[2*i::i]=[0]*(N//i-1)
        if(i>=M):print(i)

N,M=map(int,input().split())
Map=[1,1]+[0]*(M-1)
for i in range(2,(M+1)//2):
    if Map[i]:continue
    tmp=i
    while True:
        tmp+=i
        if tmp>M:break
        Map[tmp]=1
for p in range(N,M+1):
    if not Map[p]:print(p)