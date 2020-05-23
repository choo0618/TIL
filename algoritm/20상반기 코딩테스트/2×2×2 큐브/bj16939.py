import sys
sys.stdin = open('bj16939.txt','r')

def Check():
    for i in S:
        if L[i]==L[i+1]==L[i+2]==L[i+3]:continue
        return 0
    return 1
def Ro(i,l):
    for j in range(4):
        t1,t2=L[l[0]],L[l[1]]
        for x in range(0,5,2):L[l[x]],L[l[x+1]]=L[l[x+2]],L[l[x+3]]
        L[l[-2]],L[l[-1]]=t1,t2
        L[i],L[i+1],L[i+2],L[i+3]=L[i+1],L[i+3],L[i],L[i+2]
        if (j==0 or j==2) and Check():return 1
    return 0
L=[int(x)for x in input().split()]
S=[0,4,8,12,16,20]
I=[(17,16,5,4,13,12,21,20),(16,18,9,8,15,13,2,3),(18,19,22,23,14,15,6,7),(4,6,8,10,23,21,0,2),(20,22,11,9,7,5,3,1),(12,14,10,11,19,17,1,0)]
R=0
for i in range(6):
    R=Ro(S[i],I[i])
    if R:break
print(R)
