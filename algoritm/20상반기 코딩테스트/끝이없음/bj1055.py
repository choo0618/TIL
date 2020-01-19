import sys
sys.stdin = open('bj1055.txt','r')

def Find(N,idx):
    global check
    pos=0
    for c in C:
        if c=='$':
            if not N:
                if idx<=pos+List[N]-1:
                    print(S[idx-pos],end='')
                    check=1
                    return
                else:pos+=List[N]
            else:
                if idx<=pos+List[N]-1:Find(N-1,idx-pos)
                else:pos+=List[N]
        else:
            if pos==idx:
                print(c,end='')
                check=1
                return
            else:pos+=1
        if check: return
S=input()
C=input()
cnt,cc=0,0
for c in C:
    if c=='$':cnt+=1
    else:cc+=1
N=int(input())
Min,Max=map(int,input().split())
if cnt==1:
    Len=len(S)+N*(len(C)-1)
    for n in range(Min-1,Max):
        if n>Len-1:print('-',end='')
        elif n<len(S):print(S[n],end='')
        else:
            s=(n-len(S))%(len(C)-1)+1
            print(C[s],end='')
            if s==len(C):s=1
else:
    List=[len(S)]
    for i in range(1,N+1):
        Len=List[i-1]*cnt+cc
        List.append(Len)
        if Len>Max:N=i;break
    for n in range(Min-1,Max):
        tmp=N
        if n>=List[tmp]:print('-',end='');continue
        while tmp and n<List[tmp]:tmp-=1
        check=0
        Find(tmp,n)
