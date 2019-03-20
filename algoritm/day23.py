import sys
sys.stdin=open('input.txt','r')

# # 선택정렬 재귀
# def Recursion(x):
#     if x==len(L)-1:
#         print(L)
#         return
#     m=L.index(min(L[x+1:len(L)]))
#     if L[x]>L[m]:
#         L[x],L[m]=L[m],L[x]
#     Recursion(x+1)
#
#
# L=[int(x)for x in input().split()]
# Recursion(0)

# # Baby Gin 6중 for 문
# def baby(Data):
#     tri = 0
#     run = 0
#     counting = [0] * (max(Data) + 1)
#     for num in range(len(Data)):
#         counting[Data[num]] += 1
#     for t in range(len(counting)):
#         if counting[t] >= 3:
#             counting[t] -= 3
#             tri += 1
#     for r in range(0, len(counting) - 2):
#         if counting[r] == counting[r + 1] == counting[r + 2] >= 1:
#             run += 1
#             counting[r] -= 1
#             counting[r + 1] -= 1
#             counting[r + 2] -= 1
#             if counting[r] == counting[r + 1] == counting[r + 2] == 1:
#                 run += 1
#     if tri + run == 2:return True
#         # print("Baby-Gin!!!")
#     else:return False
#         # print("Nothing")
# L=[int(i)for i in input().split()]
# l=len(L)
# for z in range(l):
#     for y in range(l):
#         if y==z:
#             continue
#         for x in range(l):
#             if x==y or x==z:
#                 continue
#             for w in range(l):
#                 if w==x or w==y or w==z:
#                     continue
#                 for v in range(l):
#                     if v==w or v==x or v==y or v==z:
#                         continue
#                     for u in range(l):
#                         if u==v or u==w or u==x or u==y or u==z:
#                             continue
#                         R=[]
#                         R.append(L[z])
#                         R.append(L[y])
#                         R.append(L[x])
#                         R.append(L[w])
#                         R.append(L[u])
#                         R.append(L[v])
#                         if baby(R):
#                             print("Baby-Gin!!!")
#                         else:
#                             print("Nothing")
#                         break
#                     break
#                 break
#             break
#         break
#     break

# # 조합 For 문
# L=[int(x)for x in input().split()]
# for z in range(L[0]):
#     for y in range(L[0]):
#         if y==z:
#             continue
#         for x in range(L[0]):
#             if x==z or x==y:
#                 continue
#             print(z+1,y+1,x+1)

# # 중복조합
# L=[int(x)for x in input().split()]
# for z in range(L[0]):
#     for y in range(L[0]):
#         for x in range(L[0]):
#             print(z+1,y+1,x+1)

# # 순열
# def GetSome(depth):
#     if depth== l:
#         print(result)
#         return
#     for i in range(l):
#         if not visited[i]:
#             visited[i]=True
#             result[depth]=L[i]
#             GetSome(depth + 1)
#             visited[i] = False
# L=[int(x) for x in input().split()]
# visited=[0]*len(L)
# result=[0]*len(L)
# l=len(L)
# GetSome(0)

# # 중복 순열
# def GetSome(depth):
#     if depth== l:
#         print(result)
#         return
#     for i in range(l):
#         result[depth]=L[i]
#         GetSome(depth + 1)
#
# L=[int(x) for x in input().split()]
# result=[0]*len(L)
# l=len(L)
# GetSome(0)

# 연습문제 3

IsUsed= [0]*(rr+1)
def GetSome(n , r):
    if r > rr :
        for i in range(1, rr+1):
              print(IsUsed[i], end=' ')
        print()
        return
    if n > nn : return
    IsUsed[r] = n
    GetSome(n+1, r+1)
    GetSome(n + 1, r)

L=[int(x)for x in input().split()]
print(L)
GetSome(1,1)




