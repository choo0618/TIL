import sys
sys.stdin = open('bj1706.txt','r')

def Word():
    l=[]
    for i in range(N):
        s=''
        for j in range(M):
            if A[i][j]!='#':s+=A[i][j]
            elif A[i][j]=='#' and s:
                if len(s)>1:l.append(s)
                s=''
        if len(s)>1:l.append(s)
    return l
N,M=map(int,input().split())
A=[input()for _ in range(N)]
S=[]
S+=Word()
N,M,A=M,N,list(map(list,zip(*A[::1])))
S+=Word()
S.sort()
print(S[0])