import sys
sys.stdin = open('bj10872.txt','r')

N=int(input())
R=1
for n in range(1,N+1):R*=n
print(R)