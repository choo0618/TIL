import sys
sys.stdin = open('bj1074.txt','r')

def DFS(y,x,cnt):
    global N
    if N==2:
        for Y,X in (y,x),(y,x+1),(y+1,x),(y+1,x+1):
            if (Y,X)==(R,C):print(cnt);return
            cnt+=1
        return
    N//=2
    Y,X=y+N,x+N
    if C<X and R<Y:DFS(y,x,cnt)
    elif C>=X and R<Y:DFS(y,x+N,cnt+N*N)
    elif C<X and R>=Y:DFS(y+N,x,cnt+2*N*N)
    else:DFS(y+N,x+N,cnt+3*N*N)
N,R,C=map(int,input().split())
N=2**N
DFS(0,0,0)


N,R,C=map(int,input().split())
r=0
while N:
    s=2**N//2
    if C<s and R<s:i=0
    elif C>=s and R<s:i=1
    elif C<s and R>=s:i=2
    else:i=3
    R%=s
    C%=s
    r+=s**2*i
    N-=1
print(r)
