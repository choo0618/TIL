import sys
sys.stdin=open('input.txt','r')

# # 7진수
# N=int(input())
# r=''
# while N!=0:
#     r+=str(N%7)
#     N//=7
# print(r[::-1])

# # 이진수
# T=int(input())
# for n in range(T):
#     L=[x for x in input().split()]
#     R=''
#     A,B,C,D,E,F=10,11,12,13,14,15
#     for x in L[1]:
#         if x=='A':tmp=10
#         elif x=='B':tmp=11
#         elif x=='C':tmp=12
#         elif x=='D':tmp=13
#         elif x=='E':tmp=14
#         elif x=='F':tmp=15
#         else:tmp=int(x)
#         r=''
#         i=4
#         while i>0:
#             r+=str(tmp%2)
#             i-=1
#             tmp//=2
#         R+=r[::-1]
#     print('#%d %s'%(n+1,R))

# # 이진수2
# T=int(input())
# for n in range(T):
#     F=float(input())
#     c=0.5
#     R=''
#     cnt=1
#     while cnt<13:
#         if F>=c:
#             R+=str(1)
#             F-=c
#         else:
#             R+=str(0)
#         if F==0:
#             break
#         c/=2
#         cnt+=1
#     print('#%d'%(n+1),end=' ')
#     if F:
#         print('overflow')
#     else:
#         print(R)

# # 정식이의 은행업무
# def B(x):
#     global b
#     c=0
#     q=2**(L-1)
#     while q>0:
#         b+=int(x[c])*q
#         c+=1
#         q//=2
# def sam(x):
#     global S
#     while len(S)!=LL:
#         S+=str(x%3)
#         x//=3
# T=int(input())
# for n in range(T):
#     N=input()
#     M=input()
#     L=len(N)
#     LL=len(M)
#     for x in range(L):
#         b=0
#         S=''
#         B(N)
#         if N[x]=='0':
#             b+=2**(L-x-1)
#         else:
#             b-=2**(L-x-1)
#         sam(b)
#         S=S[::-1]
#         cnt=0
#         for y in range(LL):
#             if S[y]!=M[y]:
#                 cnt+=1
#         if cnt==1:
#             print('#%d %d'%((n+1),b))
#             break

# 암호코드 스캔
P=['211','221','122','411','132','231','114','312','213','112']
def B(x):
    global C
    tmp=0
    if x=='A':tmp=10
    elif x=='B':tmp=11
    elif x=='C':tmp=12
    elif x=='D':tmp=13
    elif x=='E':tmp=14
    elif x=='F':tmp=15
    else:tmp=int(x)
    b=''
    i=4
    while i>0:
        b+=str(tmp%2)
        i-=1
        tmp//=2
    C+=b[::-1]
T=int(input())
for n in range(T):
    L=[int(x)for x in input().split()]
    A=[input()for y in range(L[0])]
    l=['']*L[0]
    for y in range(L[0]):
        c1=0
        while c1!=L[1]:
            C=''
            B(A[y][c1])
            l[y]+=C
            c1+=1
    R=0
    for x in range(L[0]):
        z=4*L[1]-1
        while z>56:
            if l[x][z]=='1' and l[x-1][z]=='0':
                r=[]
                for c in range(8):
                    C1=''
                    c2,c3,c4=0,0,0
                    while l[x][z]=='1':c2+=1;z-=1
                    while l[x][z]=='0':c3+=1;z-=1
                    while l[x][z]=='1':c4+=1;z-=1
                    while l[x][z]=='0':z-=1
                    m=min(c2,c3,c4)
                    C1+=str(c2//m)+str(c3//m)+str(c4//m)
                    r.append(P.index(C1[::-1]))
                r=r[::-1]
                S=3*sum(r[0:9:2])+sum(r[1:9:2])
                if not S%10:
                    R+=sum(r)
                z+=1
            z-=1
    print('#%d %d'%((n+1),R))
