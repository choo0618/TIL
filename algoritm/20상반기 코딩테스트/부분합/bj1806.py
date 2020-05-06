import sys
sys.stdin = open('bj1806.txt','r')

# N,S=map(int,input().split())
# L=[int(x)for x in input().split()]+[0]
# R,l,r,Sum=10**9,0,0,L[0]
# while l<=r and r<N:
#     if Sum<S:
#         r+=1
#         Sum+=L[r]
#     elif Sum==S:
#         R=min(R,r-l+1)
#         r+=1
#         Sum+=L[r]
#     elif Sum>S:
#         R=min(R,r-l+1)
#         Sum-=L[l]
#         l+=1
# print(R if R!=10**9 else 0)

N,S=map(int,input().split())
L=list(map(int,input().split()))
R,s,j=0,0,0
for i in range(N):
    s+=L[i]
    while s>=S:
        s-=L[j]
        j+=1
    if (R==0 or R>i-j+2) and j:R=i-j+2
print(R)
