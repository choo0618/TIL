import sys
sys.stdin = open('bj1647.txt','r')

def find(x):
    if P[x]!=x:P[x]=find(P[x])
    return P[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:P[b]=a;return 0
    return 1
N,M=map(int,input().split())
Q,cnt,R=[],0,0
for i in range(M):
    a,b,c=map(int,input().split())
    Q.append((c,a-1,b-1))
Q.sort()
P=list(range(N))
for m in Q:
    if cnt==N-2:break
    c,a,b=m
    if union(a,b):continue
    cnt+=1
    R+=c
print(R)

# # input 시간 덜걸림
# def find(x):
#     if P[x]!=x:P[x]=find(P[x])
#     return P[x]
# def union(a,b):
#     a=find(a)
#     b=find(b)
#     if a!=b:P[b]=a;return 0
#     return 1
# N,M=map(int,input().split())
# Q,cnt,R=[[int(x)for x in input().split()]for y in range(M)],0,0
# Q.sort(key=lambda t:t[2])
# P=list(range(N))
# for m in Q:
#     if cnt==N-2:break
#     a,b,c=m
#     if union(a-1,b-1):continue
#     cnt+=1
#     R+=c
# print(R)
