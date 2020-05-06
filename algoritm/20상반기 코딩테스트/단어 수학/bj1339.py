import sys
sys.stdin = open('bj1339.txt','r')

R,L=0,[0]*26
for t in range(int(input())):
    tmp=0
    for c in input()[::-1]:
        L[ord(c)-65]+=10**tmp
        tmp+=1
L.sort(reverse=1)
for r in range(9):R+=L[r]*(9-r)
print(R)
