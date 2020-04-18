import sys
sys.stdin = open('bj2504.txt','r')

S=[]
R,r,c=0,1,0
for c in input():
    if c in '([':
        S.append(c)
        r*=2 if c=='(' else 3
    elif c==')':
        if not S or S[-1]=='[':c=1;break
        R+=r
        r//=2 if S[0]=='(' else 3
        S.pop()
    else:
        if not S or S[-1]=='(':c=1;break
        R+=r
        r//=3 if S[0]=='[' else 2
        S.pop()
print(R)