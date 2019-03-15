import sys
sys.stdin=open("input.txt",'r')

# cnt=0
# for x in range(1,101):
#     for y in range(x,101):
#         for z in range(y,101):
#             if x+y+z==100:
#                 print(x,y,z)
#                 cnt+=1
# print(cnt)

# def baek(x,y,z):
#     global cnt
#     if x>y or y>z:
#         return
#     if x+y+z==100:
#         print(x,y,z)
#         cnt+=1
#         return
#     if x+y+z>100:
#         return
#     if visited[x+1][y][z]==False: visited[x+1][y][z]=True; baek(x+1,y,z)
#     if visited[x][y+1][z]==False: visited[x][y+1][z]=True; baek(x,y+1,z)
#     if visited[x][y][z+1]==False: visited[x][y][z+1]=True; baek(x,y,z+1)
# visited=[[[0]*100 for _ in range(100)]for _ in range(100)]
# baek(1,1,1)
# print(cnt)

# Fibo=[-1]*101
# Fibo[0]=0
# Fibo[1]=1
#
# def Getsome(num):
#     if Fibo[num]==-1:
#         Fibo[num]=Getsome(num-1)+Getsome(num-2)
#         return Fibo[num]
#     else:
#         return Fibo[num]
#
# print(Getsome(100))

# L=[int(x) for x in input().split()]
# RS=[0]*len(L)
# RS[0]=L[0]
# r=0
# for now in range(1,len(L)):
#     RS[now]=max(RS[now-1]+L[now],L[now])
# print(max(RS))
# for R in range(RS.index(max(RS)),0,-1):
#     print(L[R],end=" ")
#     r+=L[R]
#     if r==max(RS):
#         break

nn=5
rr=3
IsUsed=[0]*(rr+1)
def GetSome(n,r):
    if r>rr:
        for i in range(1,rr+1):
              print(IsUsed[i],end=' ')
        print()
        return
    if n>nn: return
    IsUsed[r]=n
    GetSome(n,r+1)
    GetSome(n+1,r)

GetSome(1,1)