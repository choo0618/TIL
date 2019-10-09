

# def solution(genres, plays):
#     R=[]
#     Sum = dict()
#     for i in range(len(genres)):
#         Sum[genres[i]]=[]
#     for i in range(len(genres)):
#         Sum[genres[i]]+=[[plays[i],i]]
#     Sum = sorted(Sum.items(),reverse=True)
#     for i in Sum:
#         i[1].sort()
#         i[1].reverse()
#         if len(i[1])<=2:
#             for r in i[1]:
#                 R.append(r[1])
#         else:
#             n=0
#             for r in range(1,len(i[1])):
#                 if i[1][r][0]!=i[1][r-1][0]:
#                     R.append(i[1][r-1][1])
#                     n+=1
#                 else:
#                     R.append(i[1][r][1])
#                     n+=1
#                 if n==2:break
#     print(R)
#     return R
#
# print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[150, 600, 150, 800, 2500]))

# dx = [1,0]
# dy = [0,1]
# def solution(m, n, puddles):
#     M=[[0]*m for _ in range(n)]
#     for p in puddles:
#         M[p[0]-1][p[1]-1]= -1
#     print(M)
#     M[0][0]=1
#     Q=[[0,0]]
#     while Q:
#         hY,hX = Q.pop(0)
#         for dir in range(2):
#             nY = hY+dy[dir]
#             nX = hX+dx[dir]
#             if -1<nY<n and -1<nX<m and M[nY][nX]!=-1:
#                 M[nY][nX]+=1
#                 Q.append([nY,nX])
#
#     return M[n-1][m-1]%1000000007
#
# print(solution(4,3,[[2,2]]))

# def solution(m, n, puddles):
#     M=[[0]*m for _ in range(n)]
#     for p in puddles:
#         M[p[0]-1][p[1]-1]= -1
#     print(M)
#     M[0][0]=1
#     Q=[[0,0]]
#     while Q:
#         hY,hX = Q.pop(0)
#         for dir in range(2):
#             nY = hY+dy[dir]
#             nX = hX+dx[dir]
#             if -1<nY<n and -1<nX<m and M[nY][nX]!=-1:
#                 M[nY][nX]+=1
#                 Q.append([nY,nX])
#
#     return M[n-1][m-1]%1000000007
#
# print(solution(4,3,[[2,2]]))

# def solution(weight):
#     weight.sort()
#     M=[0]*(sum(weight)+1)
#     n,i=0,0
#     while True:
#         M[]
#     print(weight)
#     return None
#
# print(solution([3, 1, 6, 2, 7, 30, 1]))




















