import sys
sys.stdin = open('bj1110.txt','r')

N=tmp=int(input())
R=0
while True:
    R+=1
    r=10*(tmp%10)+(tmp//10+tmp%10)%10
    if r==N:break
    tmp=r
print(R)

