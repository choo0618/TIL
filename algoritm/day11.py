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

# # 회문2
# for num in range(10):
#     N=int(input())
#     C=[input() for x in range(100)]
#     start=1
#     for y in range(100):
#         a=''
#         for x in range(100):
#             a+=C[x][y]
#         C.append(a)
#     for n in range(200):
#         for c in range(100):
#             for z in range(start,101):
#                 a=C[n][c:z]
#                 b=a[::-1]
#                 if a==b and len(a)>start:
#                     start=len(a)
#     print("#%d %d"%(N,start))
<<<<<<< HEAD

# # 민석이의 과제 체크하기
# N=int(input())
# for n in range(N):
#     L=[int(x) for x in input().split()]
#     L1=[int(x) for x in input().split()]
#     L2=[]
#     for i in range(L[0]):
#         if not i+1 in L1:
#             L2.append(i+1)
#     print(f'#{n+1} {" ".join(map(str,L2))}')

# # GNS
# N=int(input())
# for n in range(N):
#     C=input()
#     L=[x for x in input().split()]
#     E=["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]
#     print("#%d"%(n+1),end='\n')
#     for x in range(10):
#         for i in range(L.count(E[x])):
#             print(E[x],end=' ')
#     print()







=======

#민석이의 과제 체크하기
N=int(input())
for n in range(N):
    L=[int(x) for x in input().split()]
    L1=[int(x) for x in input().split()]
    L2=[]
    for i in range(L[0]):
        if not i+1 in L1:
            L2.append(i+1)
    print(f'#{n+1} {" ".join(map(str,L2))}')
>>>>>>> 60571121018996084abb4977674b70e1e2f19952
