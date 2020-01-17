import sys
sys.stdin = open('bj1443.txt','r')

# def DFS(n,cnt):
#     global R
#     if n>=Max:return
#     if cnt==P:
#         if n>R:R=n
#         return
#     for m in [2,3,4,5,6,7,8,9]:
#         DFS(n*m,cnt+1)
# D,P=map(int,input().split())
# Max=10**D
# R=-1
# DFS(1,0)
# print(R)


D,P=map(int,input().split())
Max=10**D
Que=[1]
Map=set()
while P:
    Q=[]
    for q in Que:
        for m in [9,8,7,6,5,4,3,2]:
            Len=len(Map)
            if q*m<Max:
                Map.add((q*m,P))
                if Len!=len(Map):Q.append(q*m)
    P-=1
    Que=Q
try:print(max(Que))
except:print(-1)