import sys
sys.stdin = open('bj1065.txt','r')

N=int(input())
if N<100:print(N)
else:
    R=0
    for i in range(100,N+1):
        a,b,c=i//100,(i%100)//10,i%10
        if a-b==b-c:R+=1
    print(99+R)