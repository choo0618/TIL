import sys
sys.stdin=open('input.txt','r')

# # 연습문제4
# N=int(input())
# A=[[int(x)for x in input().split()]for y in range(N)]
# M=[[987654321]*6 for _ in range(6)]
# for _ in range(6):
#     M[_][_]=0
# for x in range(len(A)):
#     M[A[x][0]][A[x][1]]=A[x][2]
# U=[0]
# T=[0,1,2,3,4,5]
# D=M[0]
# print(D)
# while len(U)!=5:
#     w=D.index(min(D[T[1]:T[-1]]))
#     U.append(w)
#     T.pop(1)
#     for i in T:
#         D[i]=min(D[i],D[w]+M[w][i])
# print(D)

# # 웜바이러스
# def Find_Set(x):
#     if x==P[x]:return x
#     else: return Find_Set(P[x])
# def Union(x,y):
#     P[Find_Set(y)]=Find_Set(x)
# N=int(input())
# N1=int(input())
# A=[[int(x)for x in input().split()]for y in range(N1)]
# P=[0]+[0]*N
# for j in range(N+1):
#     P[j]=j
# for i in range(N1):
#     Union(A[i][0],A[i][1])
# cnt=0
# for c in range(len(P)):
#     if Find_Set(c)==Find_Set(1):cnt+=1
# print(cnt-1)

# # 웜바이러스(플로이드 워셜)
# N=int(input())
# N1=int(input())
# A=[[int(x)for x in input().split()]for y in range(N1)]
# M=[[0]*(N+1) for _ in range(N+1)]
# for m in range(N1):
#     M[A[m][0]][A[m][1]]=1
#     M[A[m][1]][A[m][0]]=1
# for via in range(1,N+1):
#     for start in range(1,N+1):
#         for end in range(1,N+1):
#             M[start][end]=M[start][end] or (M[start][via] and M[via][end])
# print(M)
# cnt=0
# for c in range(N+1):
#     if M[1][c] or M[c][1]:cnt+=1
# print(cnt-1)

# 보급로