import sys
sys.stdin = open('bj16968.txt','r')

Dic={'d':10,'c':26}
S=input()
R=Dic[S[0]]
tmp=Dic[S[0]]-1
for i in range(1,len(S)):
    if S[i]==S[i-1]:R*=tmp;continue
    R*=Dic[S[i]]
    tmp=Dic[S[i]]-1
print(R)
