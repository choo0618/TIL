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
TC=int(input())
for n in range(TC):
    N=[int(x)for x in input().split()]
    L=[int(x)for x in input().split()]
    A=[[int(x)for x in input().split()]for y in range(N[0]-1)]
    map=[0]*(N[0]*N[1])
    for i in range(len(L)):
        map[i]=L[i]
    for t in range(N[1]-1):
        if A[t][0]>max(map):
            for z in range(N[0]):
                map[N[0]*(t+1)+z]=A[t][z]
        elif A[t][0]<min(map[0:N[0]*(t+1)]):
            tmp1=N[0]*(t+1)-1
            while tmp1>=0:
                map[tmp1+N[0]]=map[tmp1]
                map[tmp1]=0
                tmp1-=1
            for z in range(N[0]):
                map[z]=A[t][z]
        else:
            for l in range(N[0]*(t+2)):
                if map[l]>A[t][0]:
                    tmp=N[0]*(t+1)-1
                    while tmp!=l-1:
                        map[tmp+N[0]]=map[tmp]
                        map[tmp] = 0
                        tmp-=1
                    for z in range(N[0]):
                        map[l]=A[t][z]
                        l+=1
                    break
    print("#%d"%(n+1),end=" ")
    for x in range(10):
        print(map[-1-x],end=" ")
    print()