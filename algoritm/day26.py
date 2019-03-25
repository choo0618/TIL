import sys
sys.stdin=open('input.txt','r')

# # 종이개수
# def check(y,x,S):
#     for j in range(S):
#         for i in range(S):
#             if A[j+y][i+x]!=A[y][x]:
#                 return False
#     return True
# def CUT(y,x,S):
#     global cnt0,cnt_1,cnt1
#     if check(y,x,S):
#         if A[y][x]==-1:cnt_1+=1
#         elif A[y][x]==0:cnt0+=1
#         elif A[y][x]==1:cnt1+=1
#         return
#     next=S//3
#     for i in range(3):
#         for j in range(3):
#             CUT(y+i*next,x+j*next,next)
# N=int(input())
# A=[[int(x)for x in input().split()]for y in range(N)]
# cnt_1=0
# cnt0=0
# cnt1=0
# visited=[[0]*N for _ in range(N)]
# CUT(0,0,N)
# print(cnt_1)
# print(cnt0)
# print(cnt1)

# # 멱수의 다양한 성질
# def Power2(a,b):
#     if b==0:return 1
#     elif b==1:return a
#     elif b&1: return a*Power2(a,b-1)
#     else:
#         temp=Power2(a,b//2)
#         return temp*temp
# def Power3(a,b):
#     ans=1
#     while b>0:
#         if b&1:ans*=a
#         a=a*a
#         b//=2
#     return ans
# print(Power2(2,3))
# print(Power3(2,3))

# # Quick Sort
# def P(L,l,r):
#     x=L[r]
#     i=l-1
#     for j in range(l,r):
#         if L[j]<=x:
#             i+=1
#             L[i],L[j]=L[j],L[i]
#     L[i+1],L[r]=L[r],L[i+1]
#     return i+1
# def Q(L,p,r):
#     if p<r:
#         s=P(L,p,r)
#         Q(L,p,s-1)
#         Q(L,s+1,r)
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     print(L)
#     Q(L,0,len(L)-1)
#     print('#%d'%(n+1),*L)

# 트리순회
def tree(t,l,r):
    # global r
    # if l<=0 or r<t:
    #     print(T, end=' ')
    #     return

    tree(l,LI[LI.index(l)//2],LI[LI.index(l)+(LI[LI.index(t)]-LI[LI.index(l)]-1)])
    # tree(r,)
N=int(input())
LI=[int(x)for x in input().split()]
LP=[int(x)for x in input().split()]
print(LI)
print(LP)
r=''
lt=LP[LI.index(LP[-1])-1]
rt=LP[-2]
tree(LP[-1],lt,rt)