import sys
sys.stdin = open('bj15684.txt','r')

def LD():
    for x in range(1,2*L[0],2):
        y,d=1,x
        while y!=L[2]+1:
            if M[y][d-1]:
                while M[y][d-1]:d-=1
                c[x][0]+=1
            elif M[y][d+1]:
                while M[y][d+1]:d+=1
                c[x][1]+=1
            y+=1
        if c[x][0]!=c[x][1]:return False
    return True
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[1])]
M=[[0,1]*L[0]+[0]for _ in range(L[2]+2)]
for g in A:
    M[g[0]][2*g[1]]=1
p=[]
for y in range(1,L[2]+1,1):
    for x in range(2,2*L[0]-1,2):
        if not M[y][x] and not M[y][x-2] and not M[y][x+2]:
            p.append([y,x])
P=[[[0,0]],[],[],[]]
for i in range(0,len(p),1):
    P[1].append(p[i])
    for j in range(i+1,len(p),1):
        if p[i][0]==p[j][0] and p[j][1]-p[i][1]==2:continue
        else:P[2].append([p[i],p[j]])
        for k in range(j+1,len(p),1):
            if p[j][0]==p[k][0] and p[k][1]-p[j][1]==2:continue
            else:P[3].append([p[i],p[j],p[k]])
R,C=0,0
while R!=4:
    if not R or R==1:
        for r in P[R]:
            c=[[0,0] for _ in range(2*L[0])]
            M[r[0]][r[1]]=1
            if LD():C=1;break
            M[r[0]][r[1]]=0
    else:
        for r in P[R]:
            c=[[0, 0]for _ in range(2*L[0])]
            for l in range(R):
                M[r[l][0]][r[l][1]]=1
            if LD():C=1;break
            for l in range(R):
                M[r[l][0]][r[l][1]]=0
    if C:break
    R+=1
if R==4:print(-1)
else:print(R)