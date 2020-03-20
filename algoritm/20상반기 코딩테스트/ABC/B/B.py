import sys
sys.stdin = open('B.txt','r')

# for t in range(int(input())):
#     S=input()
#     N=int(input())
#     L=eval(input())
#     if S.count('D')>N:print('error');continue
#     r,f,b=0,0,N
#     for s in S:
#         if s=='R':r=(r+1)%2
#         else:
#             if r:b-=1
#             else:f+=1
#     L=L[f:b]
#     if r:L.reverse()
#     print('['+','.join(map(str,L))+']')

# from collections import deque
# Q=deque()
# for t in range(int(input())):
#     a,*b=map(str,input().split())
#     if a=='push':Q.append(b[0])
#     elif a=='pop':print(Q.popleft() if Q else -1)
#     elif a=='size':print(len(Q))
#     elif a=='empty':print(0 if Q else 1)
#     elif a=='front':print(Q[0] if Q else -1)
#     else:print(Q[-1] if Q else -1)

# Q=[]
# for t in range(int(input())):
#     n=int(input())
#     if n:Q.append(n)
#     else:Q.pop()
# print(sum(Q))

# while True:
#     S=input()
#     if S=='.':break
#     Q=[]
#     R='yes'
#     for s in S:
#         if s=='(':Q.append(1)
#         elif s==')':
#             if Q:
#                 tmp=Q.pop()
#                 if tmp==2:R='no';break
#             else:R='no';break
#         elif s=='[':Q.append(2)
#         elif s==']':
#             if Q:
#                 tmp=Q.pop()
#                 if tmp==1:R='no';break
#             else:R='no';break
#     if Q:R='no'
#     print(R)

# N=int(input())
# Q=[0]
# i=1
# R=[]
# for t in range(N):
#     n=int(input())
#     while Q[-1]!=n and i<=N:
#         Q.append(i)
#         R.append('+')
#         i+=1
#     if Q[-1]!=n:break
#     Q.pop()
#     R.append('-')
# if Q==[0]:
#     for p in R:print(p)
# else:print('NO')

# A,B=map(int,input().split())
# if A>B:A,B=B,A
# r1,r2=0,0
# for t in range(1,A+1):
#     if A%t==B%t==0:r1=t
# print(r1)
# b=B
# while B%A:B+=b
# print(B)

# A,B=map(int,input().split())
# L=A*B
# while B:A,B=B,A%B
# print(A,L//A)