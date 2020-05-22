import sys
sys.stdin = open('bj3091.txt','r')

def Re(s,D):
    tmp=L[s]+D[0]
    for i,d in enumerate(D):
        if tmp!=L[s+i]+d:return 0
    return 1
B=[0,[[0],[0,0,0,0]],[[0,0]],[[0,0,-1],[-1,0]],[[-1,0,0],[0,-1]],[[0,0,0],[0,-1],[-1,0,-1],[-1,0]],[[0,0,0],[0,0],[0,-1,-1],[-2,0]],[[0,0,0],[0,0],[-1,-1,0],[0,-2]]]
C,P=map(int,input().split())
L=[int(x)for x in input().split()]
R=0
for l in B[P]:
    for i in range(C-len(l)+1):R+=Re(i,l)
print(R)




