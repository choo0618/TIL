import sys
sys.stdin = open('bj1684.txt','r')

# def GCD(a,b):
#     while b:
#         tmp=a%b
#         a=b
#         b=tmp
#     return a
# N=int(input())
# L=[int(x)for x in input().split()]
# L.sort()
# for i in range(1,N):L[i-1]=L[i]-L[i-1]
# R=L[0]
# for i in range(1,N-1):R=GCD(L[i],R)
# print(R)

N=input()
L=[int(x)for x in input().split()]
R=0
for n in L:
    n=abs(n-L[0])
    while n:
        R,n=n,R%n
print(R)