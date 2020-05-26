import sys
sys.stdin = open('bj3954.txt','r')

for t in range(int(input())):
    M,C,I=map(int,input().split())
    S,P=input(),input()
    Dic,s={},[]
    for i in range(C):
        if S[i]=='[':s.append(i)
        elif S[i]==']':
            a=s.pop()
            Dic[a],Dic[i]=i,a
    n,p,m,Max,pi=0,0,[0]*M,0,0
    for i in range(50000000):
        c=S[n]
        if c=='-':
            m[p]-=1
            if m[p]==-1:m[p]=255
        elif c=='+':m[p]=(m[p]+1)%256
        elif c=='<':
            p-=1
            if p==-1:p=M-1
        elif c=='>':p=(p+1)%M
        elif c=='[':
            if m[p]==0:n=Dic[n];continue
        elif c==']':
            if m[p]!=0:n=Dic[n];continue
        elif c==',':
            if pi>=I:m[p]=255
            else:m[p]=ord(P[pi]);pi+=1
        n+=1
        Max=max(Max,n)
        if n==C:break
    if n==C:print('Terminates')
    else:print('Loops %d %d'%(Dic[Max],Max))

