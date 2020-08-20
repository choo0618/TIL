import sys
sys.stdin = open('10202.txt','r')

for t in range(int(input())):
    N=int(input())
    A,B,C,R=input(),input(),input(),0
    for i in range(N):
        a,b,c=A[i],B[i],C[i]
        if a==b==c:continue
        elif a==b or b==c or a==c:R+=1
        else:R+=2
    print('#%d %d'%(t+1,R))

