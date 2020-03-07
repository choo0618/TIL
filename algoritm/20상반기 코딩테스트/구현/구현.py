import sys
sys.stdin = open('구현.txt','r')

# import math
# N=float(input())
# print(N*N*math.pi)
# print(2*N*N)

# print(int(input())-sum(int(input())for _ in range(9)))

# N=int(input())
# Sum=sum(int(input())for _ in range(N))
# print("Junhee is cute!" if N//2<Sum else "Junhee is not cute!")

# N,K=map(int,input().split())
# Map=[0]*(N+1)
# r=0
# for i in range(2,N//2):
#     if Map[i]:continue
#     t=i
#     while t<=N and K:
#         if not Map[t]:
#             Map[t]=1
#             K-=1
#             r=t
#         t+=i
# print(r)

# while True:
#     L=[int(x)for x in input().split()]
#     if not sum(L):break
#     L.sort()
#     print('right' if L[0]**2+L[1]**2==L[2]**2 else 'wrong')
#
# A=[list(input())for i in range(5)]
# Len=max(len(a)for a in A)
# for j in range(Len):
#     for i in range(5):
#         try:print(A[i][j],end='')
#         except:continue

# Set=set()
# for _ in range(int(input())):
#     x,y=map(int,input().split())
#     for i in range(10):
#         for j in range(10):Set.add((x+i,y+j))
# print(len(Set))

# M=[0]+[1]*30
# for i in range(28):M[int(input())]=0
# I=M.index(1)
# print(I)
# M[I]=0
# print(M.index(1))

# for i in range(int(input())):
#     r,e,c=map(int,input().split())
#     print('advertise' if e-c>r else 'do not advertise' if e-c<r else 'does not matter')

# L,R,r=[],[],0
# for _ in range(8):L.append((int(input()),_+1))
# L.sort()
# for _ in L[3:]:r+=_[0];R.append(_[1])
# R.sort()
# print(r)
# print(' '.join(map(str,R)))

# from collections import defaultdict
# Dic,L=defaultdict(int),[]
# for i in range(int(input())):Dic[input()[0]]+=1
# for s,n in Dic.items():
#     if n>=5:L.append(s)
# L.sort()
# print(''.join(L) if L else 'PREDAJA')

# L,R=[0]*26,[]
# for i in range(int(input())):L[ord(input()[0])-97]+=1
# for i in range(26):
#     if L[i]>=5:R+=chr(i+97)
# print(''.join(R) if R else 'PREDAJA')

# L=[int(input())for x in range(5)]
# L[0]*=L[4]
# L[1]+=max(L[4]-L[2],0)*L[3]
# print(min(L[0],L[1]))
# A=int(input())
# B,C,D=int(input()),int(input()),int(input())
# P=int(input())
# print(min(P*A,B if P<C else B+D*(P-C)))

# s=0
# for _ in range(4):s+=int(input())
# print(s//60)
# print(s%60)

# print(max(sum(map(int,input().split())),sum(map(int,input().split()))))

# for _ in range(int(input())):
#     A,B=0,0
#     for t in range(int(input())):
#         a,b=map(float,input().split())
#         A+=a;B+=b*a
#     print(int(A),round(B/A,1))

# from collections import defaultdict
# Dic,L=defaultdict(list),[0]*10
# for _ in range(10):
#     L[_]=int(input())
#     if _:L[_]+=L[_-1]
# Min=10**9
# for l in L:Dic[abs(100-l)].append(l);Min=min(Min,abs(100-l))
# print(max(Dic[Min]))

# R,S=0,0
# for i in range(10):
#     S+=int(input())
#     if abs(R-100)>=abs(S-100):R=S
# print(R)

# for t in range(int(input())):
#     A,B,C,D,a,b,c,d=map(int,input().split())
#     print(max(1,A+a)+5*max(1,B+b)+2*max(0,C+c)+2*(D+d))

# N,W,H=map(int,input().split())
# M=(W**2+H**2)**0.5
# for _ in range(N):print('DA' if int(input())<=M else 'NE')

# W=[int(input())for x in range(10)]
# K=[int(input())for x in range(10)]
# W.sort()
# K.sort()
# print(sum(W[7:]),sum(K[7:]))

# e,f,c=map(int,input().split())
# R,S=0,e+f
# while S>=c:
#     R+=S//c
#     S=sum(divmod(S,c))
# print(R)

# N=int(input())
# L=[int(x)for x in input().split()]
# Map=[0]*(N+1)
# fact=[1]*N
# for i in range(1,N):
#     fact[i]=fact[i-1]*i
# if L[0]==1:
#     for i in range(1,N+1):
#         cnt=1
#         for j in range(1,N+1):
#             if Map[j]:continue
#             if cnt*fact[N-i]>=L[1]:
#                 Map[j]=1
#                 print(j,end=' ')
#                 L[1]-=(cnt-1)*fact[N-i]
#                 break
#             cnt+=1
# else:
#     K=1
#     for i in range(1,N+1):
#         cnt=1
#         for j in range(1,N+1):
#             if Map[j]:continue
#             if L[i]==j:
#                 Map[j]=1
#                 K+=(cnt-1)*fact[N-i]
#                 break
#             cnt+=1
#     print(K)

# from math import factorial
# def Q1(k):
#     if len(l)==0:return []
#     f=factorial(len(l)-1)
#     i=0
#     while f<=k:k-=f;i+=1
#     c=l.pop(i)
#     return [c]+Q1(k)
# def Q2():
#     k=0
#     for a in L:
#         idx=l.index(a)
#         k+=idx*factorial(len(l)-1)
#         l.pop(idx)
#     return k+1
# N=int(input())
# q,*L=list(map(int,input().split()))
# l=[i+1 for i in range(N)]
# if q==1:
#     k=L[0]
#     print(' '.join(map(str,Q1(k-1))))
# else:print(Q2())

N=int(input())
r=0
for i in range(1,N+1):
    for j in range(i,N+1):
        if i*j>N:break
        r+=1
print(r)


