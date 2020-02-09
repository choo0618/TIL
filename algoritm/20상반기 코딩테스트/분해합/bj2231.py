import sys
sys.stdin=open('bj2231.txt','r')

N=int(input())
R=0
for i in range(N):
    Sum=i
    for n in str(i):Sum+=int(n)
    if Sum==N:R=i;break
print(R)