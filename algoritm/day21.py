import sys
sys.stdin=open("input.txt",'r')

# L=[x for x in input().split()]
# for j in range(len(L)):
#     R=0
#     r=128
#     if int(L[j])==1:
#         R+=r
#         r<<=7
#     r>>=1
#     print('%d, %d'%(j+1,R))

# L=input()
# print(L)
# t=0
# for x in range(len(L)):
#     t=t*2+int(L[x])
#     if (x+1)%7==0:
#         print(t)
#         t=0

# # 16진수>>10진수
# L=input()
# print(L)
# R=''
# A,B,C,D,E,F=10,11,12,13,14,15
# for x in L:
#     if x=='A':tmp=10
#     elif x=='B':tmp=11
#     elif x=='C':tmp=12
#     elif x=='D':tmp=13
#     elif x=='E':tmp=14
#     elif x=='F':tmp=15
#     else:tmp=int(x)
#     r=''
#     i=4
#     while i>0:
#         r+=str(tmp%2)
#         i-=1
#         tmp//=2
#     R+=r[::-1]
# print(R)
# t=0
# for x in range(len(R)):
#     t=t*2+int(R[x])
#     if (x+1)%7==0 or x==len(R)-1:
#         print(t)
#         t=0


# Password=['001101','010011','111011','110001','100011','110111','001011','111101','011001','101111']
# L=input()
# print(L)
# R=''
# A,B,C,D,E,F=10,11,12,13,14,15
# for x in L:
#     if x=='A':tmp=10
#     elif x=='B':tmp=11
#     elif x=='C':tmp=12
#     elif x=='D':tmp=13
#     elif x=='E':tmp=14
#     elif x=='F':tmp=15
#     else:tmp=int(x)
#     r=''
#     i=4
#     while i>0:
#         r+=str(tmp%2)
#         i-=1
#         tmp//=2
#     R+=r[::-1]
# print(R)
# i=0
# while i<len(R):
#     if R[i:i+6] in Password:
#         print(Password.index(R[i:i+6]),end=' ')
#         i+=6
#     else:
#         i+=1

# Password=['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     A=[input() for y in range(L[0])]
#     R=[]
#     for x in range(len(A)):
#         if int(A[x]):
#             i=-1
#             while i>-L[1]:
#                 if A[x][i-7:i] in Password:
#                     R.insert(0,Password.index(A[x][i-7:i]))
#                     i-=7
#                 else:i-=1
#             break
#     a,b=0,0
#     for x in range(len(R)):
#         if x%2:b+=R[x]
#         else:a+=R[x]*3
#     print("#%d"%(n+1),end=' ')
#     if not (a+b)%10:print(sum(R))
#     else:print(0)
c=[1,2,3,4,5,6,7,8,9]
T=int(input())
for n in range(T):
    L=[[int(x)for x in input().split()]for y in range(9)]

    for y in range(9):
        r=[]
        for x in range(9):
            r.append(L[x][y])
        L.append(r)
    r=1
    for i in range(18):
        for j in range(9):
            if not c[j] in L[i]:
                r=0
    print('#%d %d'%(n+1,r))
