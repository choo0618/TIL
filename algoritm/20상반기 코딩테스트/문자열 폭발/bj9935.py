import sys
sys.stdin = open('bj9935.txt','r')

def Check():
    for c in range(-1,-Len-1,-1):
        if S[c]!=i[c]:return False
    return True
I=input()
i=input()
Len=len(i)
S=[]
for c in I:
    S.append(c)
    if c==i[Len-1]:
        if len(S)<Len:continue
        if Check():
            for t in range(Len):S.pop()
print(''.join(S) if S else 'FRULA')
