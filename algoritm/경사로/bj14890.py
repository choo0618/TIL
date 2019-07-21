import sys
sys.stdin=open('bj14890.txt','r')

L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
a=list(map(list,zip(*A[::-1])))
A+=a
R=0
for l in A:
    m=[0]*L[0]
    n=0
    while n<L[0]-1:
        if not l[n]-l[n+1]:n+=1
        elif l[n]-l[n+1]==1:
            if sum(l[n+1:n+L[1]+1])==L[1]*l[n+1] and not sum(m[n+1:n+L[1]+1]):m[n+L[1]]=1;n+=L[1]
            else:break
        elif l[n]-l[n+1]==-1:
            if sum(l[n-L[1]+1:n+1])==L[1]*l[n] and not sum(m[n-L[1]+1:n+1]):m[n]=1;n+=1
            else:break
        else:break
        if n==L[0]-1:R+=1
print(R)
