import sys
sys.stdin = open("input.txt", "r")

# # 숫자 추가
# T=int(input())
# for t in range(T):
#     Q=[int(x) for x in input().split()]
#     L=[int(x) for x in input().split()]
#     A=[[int(x) for x in input().split()]for y in range(Q[1])]
#     map=[0]*(Q[0]+Q[1])
#     for i in range(len(L)):
#         map[i]=L[i]
#     for i in range(Q[1]):
#         j=Q[0]+i-1
#         while j!=A[i][0]-1:
#             map[j+1]=map[j]
#             j-=1
#         map[A[i][0]]=A[i][1]
#     print('#%d %d'%(t+1,map[Q[2]]))

# 수열 합치기
N=[int(x)for x in input().split()]
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(N[0]-1)]
map=[0]*(N[0]*N[1])
print(L)
print(A)
print(map)
for i in range(len(L)):
    map[i]=L[i]
for t in range(N[1]-1):
    for l in range(N[0]*(t+1)):
        if map[l]>=A[l][0]:
            
print(map)