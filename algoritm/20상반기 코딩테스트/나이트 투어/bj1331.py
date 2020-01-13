import sys
sys.stdin = open('bj1331.txt','r')

L = [input()for x in range(36)]
L+=[L[0]]
a = set()
for i in range(36):
    now = (ord(L[i][0])-64,int(L[i][1]))
    next = (ord(L[i+1][0])-64,int(L[i+1][1]))
    dir = (abs(now[0]-next[0]),abs(now[1]-next[1]))
    if dir==(1,2) or dir==(2,1):
        a.add(L[i])
        continue
if len(a)!=36:print("Invalid")
else:print("Valid")

