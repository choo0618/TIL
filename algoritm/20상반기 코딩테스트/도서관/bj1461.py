import sys
sys.stdin = open('bj1461.txt','r')

N,M=map(int,input().split())
Pl,Mi=[],[]
R,Max=0,0
for i in [int(x) for x in input().split()]:
    if i>0:Pl.append(i)
    else:Mi.append(i)
    if abs(i)>Max:Max = abs(i)
Pl.sort()
Mi.sort()
Mi.reverse()
while Pl:
    m=1
    r = Pl.pop()
    R+=2*r
    while Pl and m!=M:
        Pl.pop()
        m+=1
while Mi:
    m=1
    r = abs(Mi.pop())
    R+=2*r
    while Mi and m!=M:
        Mi.pop()
        m+=1
print(R-Max)
