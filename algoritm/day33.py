import sys
sys.stdin=open('input.txt','r')

# # 셀프넘버
# def hi(x):
#     r=int(''.join(x))
#     for i in range(len(x)):
#         r+=int(x[i])
#     if r<=10000:R[r]=0
# r=[int(x)for x in range(1,10001)]
# R=[int(x)for x in range(10001)]
# for i in r:
#     hi(list(str(i)))
# for y in R:
#     if y:print(y)

# # 공통조상
# def Find(x):
#     global p
#     if x==P[x] or x in p:p+=[x];
#     else:p+=[x];return Find(P[x])
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     L1=[int(x)for x in input().split()]
#     P=[0]+[1]*L[0]
#     for i in range(0,len(L1),2):
#         P[L1[i+1]]=L1[i]
#     p=[]
#     Find(L[2])
#     Find(L[3])
#     cnt=1
#     R=[p[-1]]
#     while R:
#         a=R.pop(0)
#         for i in range(0,len(L1),2):
#             if L1[i]==a:R.append(L1[i+1]);cnt+=1
#     print('#%d %d %d'%(n+1,p[-1],cnt))

# # 숫자만들기
# c=['+','-','*','/']
# def P(depth,x):
#     global mm, nn
#     if depth==N-1:
#         # print(r)
#         if x>mm:mm=x;return
#         if x<nn:nn=x;return
#     for i in range(len(l)):
#         if not V[i]:
#             V[i]=True
#             r[depth]=l[i]
#             P(depth+1,SUM(r[depth],x,depth))
#             V[i]=False
#             r[depth]=0
# def SUM(x,s,j):
#     if x=='+':return s+L[j+1]
#     elif x=='-':return s-L[j+1]
#     elif x=='*':return s*L[j+1]
#     elif x=='/':return s//L[j+1]
# T=int(input())
# for n in range(T):
#     N=int(input())
#     L1=[int(x)for x in input().split()]
#     L=[int(x) for x in input().split()]
#     l=[]
#     C=[]
#     for i in range(4):
#         l+=c[i]*L1[i]
#     V=[0]*len(l)
#     r=[0]*len(l)
#     mm=-987654321
#     nn=987654321
#     P(0,L[0])
#     print('#%d %d'%(n+1,mm-nn))

# # 가능한 시험점수
def P(y,s):
    if R[s]:return
    R[s]=1
    for i in range(N):
        if not V[i]:
            V[i]=1
            P(y,s+L[i])
            V[i]=0
T=int(input())
for n in range(T):
    N=int(input())
    L=[int(x)for x in input().split()]
    r=sum(L)
    V=[0]*N
    R=[0]*(r+1)
    P(r,0)
    print('#%d %d'%(n+1,sum(R)))
    print(R)


# T=int(input())
# for n in range(T):
#     N=int(input())
#     L=[int(x)for x in input().split()]
#     r=sum(L)
#     V=[0]*N
#     R=[1]+[0]*(r)
#     for i in range(r):
#         for j in range(N):
#             if R[i+L[j]]<r and not V[j]:
#                 V[j]=1
#                 R[i+L[j]]=1
#             V[j]=0
#     print(R)