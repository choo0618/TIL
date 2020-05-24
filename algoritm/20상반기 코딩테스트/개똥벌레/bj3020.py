import sys
sys.stdin = open('bj3020.txt','r')

def Check(List,x):
    l,r=0,N//2-1
    while l<=r:
        mid=(l+r)//2
        if List[mid]>x:r=mid-1
        else:l=mid+1
    return N//2-l
N,H=map(int,input().split())
U,D=[],[]
for i in range(N//2):
    D.append(int(input()))
    U.append(int(input()))
U.sort(),D.sort()
R,C=500001,0
for i in range(H):
    r=Check(U,i)+Check(D,H-i-1)
    if r<R:R,C=r,1
    elif r==R:C+=1
print(R,C)

# import sys
# input=sys.stdin.readline
# N,H=map(int, input().split())
# D=[0]*H
# U=[0]*H
# for i in range(N//2):
#     D[int(input())-1]+= 1
#     U[-int(input())]+= 1
# for i in range(H-1):
#     D[~i-1]+=D[~i]
#     U[i+1]+=U[i]
# for i in range(H): D[i]+= U[i]
# m = min(D)
# print(m, D.count(m))