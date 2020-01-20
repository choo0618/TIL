import sys
sys.stdin = open('bj5014.txt','r')

def Solution():
    F,S,G,U,D=map(int,input().split())
    if S==G:return 0
    M=[0]*(F+1)
    M[S]=1
    Que=[S]
    tmp=0
    while Que:
        tmp+=1
        Q=[]
        for q in Que:
            for ud in [U,-D]:
                s=q+ud
                if not 0<s<F+1:continue
                if s==G:return tmp
                if not M[s]:Q.append(s);M[s]=1
        Que=Q
    return 'use the stairs'
print(Solution())

