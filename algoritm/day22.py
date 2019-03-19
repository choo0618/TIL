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
P=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
def B(x):
    global R
    tmp=0
    if x == 'A':tmp=10
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
    R+=b[::-1]

L=[int(x)for x in input().split()]
A=[input()for y in range(L[0])]
a='0'*L[1]
cnt=0
i=0
while cnt!=L[0]:
    if A[i]==a:
        A.pop(i)
    elif A[i]==A[i+1] :
        A.pop(i+1)
    else:
        i+=1
    cnt+=1
print(A)
ll=['']*len(A)
for y in range(len(A)):
    cnt1=0
    while cnt1!=L[1]:
        if A[y][cnt1]!='0':
            R=''
            B(A[y][cnt1])
            ll[y]+=R
        else:
            ll[y]+='0'
        cnt1+=1
print(ll)
for x in range(len(ll)):
    ii=len(ll[x])
    R1=[]
    while ii>=0:
        if ll[x][ii-7:ii] in P:
            R1.insert(0,P.index(ll[x][ii-7:ii]))
            ii-=7
        else:ii-=1
    print(R1)
