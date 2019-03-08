import sys
sys.stdin = open("input.txt", "r")

# # 간단한 압축 풀기
# T=int(input())
# for n in range(T):
#     N=int(input())
#     a=''
#     print("#%d"%(n+1))
#     for x in range(N):
#         L=[x for x in input().split()]
#         a+=(L[0]*int(L[1]))
#     p=0
#     for c in a:
#         if p%10==0 and not p==0:
#             print()
#         print(c,end='')
#         p+=1
#     print()

# # 두 개의 숫자열
# T=int(input())
# for n in range(T):
#     L=[int(x) for x in input().split()]
#     A=[[int(x) for x in input().split()]for y in range(2)]
#     R=0
#     if L[0]>L[1]:
#         L[0],L[1]=L[1],L[0]
#         A[0],A[1]=A[1],A[0]
#     for x in range(L[1]-L[0]+1):
#         r=0
#         for m in range(L[0]):
#             r+=A[0][m]*A[1][m+x]
#         if r>R:
#             R=r
#     print("#%d %d"%(n+1,R))

# 추억의 2048
N=int(input())
for num in range(N):
    L=[x for x in input().split()]
    n=int(L[0])
    A=[[int(x) for x in input().split()]for y in range(n)]
    W=0
    if L[1]=='down':
        W=1
    elif L[1]=='right':
        W=2
    elif L[1]=='up':
        W=3
    for _ in range(W):
        A=list(map(list,zip(*A[::-1])))
    for y in range(n):
        for x in range(n):
            i=x
            tmp=i+1
            tmp1=i-1
            if A[y][x]:
                if x!=n-1:
                    while not A[y][tmp]:
                        if tmp==4:
                            break
                        tmp+=1
                    if A[y][i]==A[y][tmp]:
                        A[y][i]*=2
                        A[y][tmp]=0
                    if x!=0:
                        while not A[y][tmp1]:
                            if tmp1<0:
                                break
                            A[y][tmp1]=A[y][i]
                            A[y][i]=0
                            i-=1
                            tmp1-=1

                else:
                    while not A[y][i-1]:
                        if i==0:
                            break
                        A[y][i-1]=A[y][i]
                        A[y][i] = 0
                        i-=1
    for _ in range(4-W):
        A=list(map(list, zip(*A[::-1])))
    print("#%d"%(num+1))
    for R in range(n):
        print(*A[R])











