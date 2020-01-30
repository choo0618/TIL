import sys
sys.stdin = open('bj16637.txt','r')

def cal(n1,x,n2):
    if x=='+':return n1+n2
    elif x=='-':return n1-n2
    else:return n1*n2
def DFS(idx,result):
    global R
    if idx>=N:
        R=max(R,result)
        return
    x='+'
    if idx:x=L[idx-1]
    if idx+2<N:
        r=cal(int(L[idx]),L[idx+1],int(L[idx+2]))
        DFS(idx+4,cal(result,x,r))
    DFS(idx+2,cal(result,x,int(L[idx])))
N=int(input())
L=list(map(str,input()))
R=-987654321
DFS(0,0)
print(R)