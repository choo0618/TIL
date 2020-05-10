import sys
sys.stdin = open('bj2061.txt','r')

K,L=map(int,input().split())
tmp=0
for l in range(2,L+1):
    if l==1:continue
    if l!=L and K%l==0:tmp=l;break
if tmp:print('BAD',tmp)
else:print('GOOD')
