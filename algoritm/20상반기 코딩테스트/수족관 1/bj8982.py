import sys
sys.stdin = open('bj8982.txt','r')

def Hole(a,b,c,d):
    tmp=0
    for x in range(a,b,c):
        if W[x]==0:return tmp
        d=min(d,W[x])
        tmp+=d
        W[x]-=d
    return tmp
N=int(input())
R,W=0,[]
input()
for _ in range(N//2-1):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    for _ in range(c-a):W.append(b);R+=b
input()
H=[]
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    H.append((W[a],a))
H.sort()
for w,i in H:
    R-=Hole(i+1,len(W),1,W[i])+Hole(i-1,-1,-1,W[i])
    R-=W[i]
    W[i]=0
print(R)