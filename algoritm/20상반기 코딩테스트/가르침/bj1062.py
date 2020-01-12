import sys
sys.stdin = open('bj1062.txt','r')

# def check():
#     r=0
#     for l in L:
#         tmp=1
#         for c in l:
#             if not A[ord(c)-97]:tmp=0
#         if tmp:r+=1
#     return r
#
# def DFS(n,cnt):
#     global R
#     if cnt == K:
#         r = check()
#         if r>R:
#             R=r
#         return
#     for c in range(n,26):
#         if not A[c]:
#             A[c]=1
#             DFS(c+1,cnt+1)
#             A[c]=0
# N,K=map(int,input().split())
# A = [0]*26
# for c in 'antic':
#     A[ord(c)-97]=1
#     K-=1
# L,R=[],0
# for x in range(N):
#     I=''
#     for i in input():
#         if not A[ord(i)-97] and not i in I:I+=i
#     if len(I)<=K:L.append(I)
# if K<0:print(0)
# else:
#     DFS(0,0)
#     print(R)

n, k = map(int, input().split())
arr = [set(input()) for __ in range(n)]

commons = set('antatica')
ts = sorted(set(chr(cc) for cc in range(ord('a'), ord('z') + 1)) - commons)

import itertools

res = 0

arr = [sum(1 << ord(c) - ord('a') for c in y) for y in arr]
commons = sum(1 << ord(c) - ord('a') for c in commons)
ts = [1 << ord(c) - ord('a') for c in ts]

for t in itertools.combinations(ts, k - 5) if k >= 5 else ():
    # z = commons | set(t)
    # res = max(res, sum(z >= y for y in arr))
    z = commons | sum(t)
    res = max(res, sum((z & y) == y for y in arr))

print(res)
