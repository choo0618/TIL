import sys
sys.stdin = open('A.txt','r')

# I=[-1]*26
# for i,c in enumerate(input()):
#     n=ord(c)-97
#     if I[n]==-1:I[n]=i
# print(' '.join(map(str,I)))

# for t in range(int(input())):
#     N,S=map(str,input().split())
#     N=int(N)
#     R=''
#     for c in S:R+=c*N
#     print(R)

# C=[0]*26
# for c in input():
#     n=ord(c)
#     if n>=97:n-=97
#     else:n-=65
#     C[n]+=1
# Max=C.count(max(C))
# if Max!=1:print('?')
# else:print(chr(C.index(max(C))+65))

# print(len([s for s in input().split()]))

# A,B=map(str,input().split())
# a,b='',''
# for n in range(2,-1,-1):a+=A[n];b+=B[n]
# print(max(int(a),int(b)))

# R,I=0,'22233344455566677778889999'
# for c in input():R+=int(I[ord(c)-65])+1
# print(R)

# R=0
# for t in range(int(input())):
#     S=[0]*26
#     s=input()
#     i=0
#     while i!=len(s):
#         n=ord(s[i])-97
#         if S[n]:break
#         S[n]=1
#         tmp=s[i]
#         while True:
#             i+=1
#             if i==len(s) or s[i]!=tmp:break
#     if i==len(s):R+=1
# print(R)

# N=int(input())
# DP=[0,1]+[0]*(N-1)
# for i in range(2,N+1):DP[i]=DP[i-2]+DP[i-1]
# print(DP[N])

# N=int(input())
# n=1
# while n*(n+1)//2<N:n+=1
# a,b=n,1
# N-=n*(n-1)//2
# while N!=1:
#     a-=1
#     b+=1
#     N-=1
# if not n%2:a,b=b,a
# print('%d/%d'%(a,b))

# N=int(input())
# R=tmp=1
# while True:
#     if tmp>=N:break
#     tmp+=6*R
#     R+=1
# print(R)

# A,B,C=map(int,input().split())
# if B>=C:print(-1)
# else:print(A//(C-B)+1)

# for t in range(int(input())):
#     N=int(input())
#     K=int(input())
#     DP=[list(range(K+1))]+[[0]*(K+1) for _ in range(N)]
#     for n in range(1,N+1):
#         for k in range(1,K+1):
#             DP[n][k]=DP[n-1][k]+DP[n][k-1]
#     print(DP[N][K])

# X=0
# Y=0
# for _ in range(3):
#     x,y=map(int,input().split())
#     X^=x
#     Y^=y
# print(X,Y)

# for t in range(int(input())):
#     x1,y1,r1,x2,y2,r2=map(int,input().split())
#     d=(abs(x1-x2)**2+abs(y1-y2)**2)**0.5
#     if (x1,y1)==(x2,y2):
#         if r1==r2:print(-1)
#         else:print(0)
#     elif abs(r1-r2)<d and r1+r2>d:print(2)
#     elif abs(r1-r2)==d or r1+r2==d:print(1)
#     else:print(0)

# Map=[1]*1001
# Map[0]=Map[1]=0
# for i in range(2,500):
#     if not Map[i]:continue
#     Map[i]=1
#     for n in range(2*i,1001,i):Map[n]=0
# N,R=int(input()),0
# for n in map(int,input().split()):R+=Map[n]
# print(R)

# N=int(input())
# M=int(input())
# Map=[1]*(M+1)
# Map[0]=Map[1]=0
# for i in range(2,(M+1)//2):
#     if not Map[i]:continue
#     Map[i]=1
#     for n in range(2*i,M+1,i):Map[n]=0
# R,r=0,0
# for n in range(M,N-1,-1):
#     if Map[n]:R+=n;r=n
# if R:print(R);print(r)
# else:print(-1)

# Map=[1]*10001
# Map[0]=Map[1]=0
# for i in range(2,5000):
#     if not Map[i]:continue
#     Map[i]=1
#     for n in range(2*i,10001,i):Map[n]=0
# for t in range(int(input())):
#     N=int(input())
#     for i in range(N//2,1,-1):
#         if Map[i] and Map[N-i]:print(i,N-i);break


N=int(input())
n=665
while N:
    n+=1
    tmp=str(n)
    if '666' in tmp:N-=1
print(n)

