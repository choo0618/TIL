import sys
sys.stdin = open('bj1132.txt','r')

R,L=0,[[0,0]for _ in range(10)]
for t in range(int(input())):
    S=input()
    tmp=0
    for c in S[::-1]:
        L[ord(c)-65][0]+=10**tmp
        tmp+=1
    L[ord(S[0])-65][1]=1
L.sort()
if L[0][1]:
    for i in range(10):
        if not L[i][1]:L.insert(0,L.pop(i));break
for i in range(10):R+=L[i][0]*i
print(R)

print(143**0.5)