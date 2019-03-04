import sys
sys.stdin = open("input.txt", "r")

# # KMP
# TC=int(input())
# for num in range(TC):
#     P=input()
#     T=input()
#     pi=[-1,0]
#     i,j,n=0,1,0
#     while len(P)!=len(pi):
#         if P[i]==P[j]:
#             pi.append(pi[j]+1)
#             i+=1
#         else:
#             if P[0]==P[j]:
#                 pi.append(1)
#                 i=1
#             else:
#                 pi.append(0)
#                 i=0
#         j+=1
#     K=len(pi)
#     while i<=len(T)-len(P)+1:
#         r = 0
#         for c in range(K):
#             if T[n]!=P[c]:
#                 n=n-pi[c]
#                 break
#             elif T[n]==P[c]:
#                 r+=1
#                 n+=1
#         if r==K:
#             print("#%d 1"%(num+1))
#             break
#         if n==len(T)-len(P)+1:
#             print("#%d 0"%(num+1))
#             break

# # Bruteforce
# TC=int(input())
# for num in range(TC):
#     P=input()
#     T=input()
#     i=0
#     while i<=len(T)-len(P)+1:
#         j=0
#         for n in range(len(P)):
#             if P[n]==T[i]:
#                 j+=1
#                 i+=1
#             else:
#                 i=i-j+1
#                 break
#         if j==len(P):
#             print("#%d 1" %(num+1))
#             break
#         if i==len(T)-len(P)+1:
#             print("#%d 0"%(num+1))
#             break

# # Easy
# TC=int(input())
# for n in range(TC):
#     P=input()
#     T=input()
#     if P in T:
#         print("#%d 1"%(n+1))
#     else:
#         print("#%d 0"%(n+1))

# # 회문
# TC=int(input())
# for n in range(TC):
#     N=[int(x) for x in input().split()]
#     C=[input() for x in range(N[0])]
#     R=[]
#     for y in range(N[0]):
#         for z in range(N[0]-N[1]+1):
#             a = ''
#             b = ''
#             for x in range(N[1]):
#                 a+=C[y][x+z]
#                 b+=C[x+z][y]
#             R.append(a)
#             R.append(b)
#     for r in range(len(R)):
#         if R[r]==R[r][::-1]:
#             print("#%d %s"%(n+1,R[r]))

# # 글자수
# TC=int(input())
# for n in range(TC):
#     C=input()
#     T=input()
#     result=0
#     for c in range(len(C)):
#         cnt = 0
#         for t in T:
#             if t==C[c]:
#                 cnt+=1
#         if cnt>=result:
#             result=cnt
#     print("#%d %d"%(n+1,result))

# 회문2
# for n in range(1):
#     N=int(input())
#     C=[input() for x in range(8)]
#     R=[]
#     for y in range(8):
#         for x in range(y+1):
#             a=''
#             b=''
#             for z in range(8-y):
#                 a+=C[x+y][z]
#                 b+=C[z][x+y]
#             R.append(a)
#             R.append(b)
#     print(R)
#     # for r in range(len(R)):
#     #     if R[r]==R[r][::-1]:
#     #         print("#%d %s"%(n+1,R[r]))

for num in range(1):
    N=int(input())
    C=[input() for x in range(8)]
    m=8
    for n in range(m,0,-1):
        if C[n]==C[n][::-1]:
            print("#%d %d"%(n+1,m))
        m-=1