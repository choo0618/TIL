import sys
sys.stdin = open('bj16637.txt','r')

def Cal(a,b,c):
    if c=='+':return a+b
    elif c=='-':return a-b
    else:return a*b
def DFS(i,r):
    global R
    if i>=N:
        R=max(R,r)
        return
    x='+'
    if i:x=S[i-1]
    if i+2<N:
        n=Cal(int(S[i]),int(S[i+2]),S[i+1])
        DFS(i+4,Cal(r,n,x))
    DFS(i+2,Cal(r,int(S[i]),x))
N=int(input())
S=input()
R=-10**9
DFS(0,0)
print(R)