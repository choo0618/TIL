import sys
sys.stdin = open('bj2504.txt','r')

I=input()
S=[]
R,r,C=0,1,0
for i in range(len(I)):
    c=I[i]
    if c in '([':
        S.append(c)
        r*=2 if c=='(' else 3
    elif c==')':
        if not S or S[-1]=='[':C=1;break
        if I[i-1]=='(':R+=r
        S.pop()
        r//=2
    else:
        if not S or S[-1]=='(':C=1;break
        if I[i-1]=='[':R+=r
        S.pop()
        r//=3
if S:C=1
print(0 if C else R)