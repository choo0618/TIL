import sys
sys.stdin = open('bj17140.txt','r')

def RC(t):
    global A
    if t:A=list(map(list,zip(*A[::-1])))
    Len,Max,LL=len(A),0,[]
    Map=[[]for _ in range(Len)]
    for i in range(Len):
        Dic,M={},0
        for j in A[i]:
            if not j:continue
            if j in Dic:Dic[j]+=1
            else:Dic[j]=1
        l=sorted(Dic.items(),key=lambda x:(x[1],x[0]))
        for a,b in l:
            Map[i]+=[a,b]
            M+=2
            if M==100:break
        LL.append(M)
        Max=max(Max,M)
    for i in range(Len):A[i]=Map[i]+[0]*(Max-LL[i])
    if t:A=list(map(list,zip(*A[::1])))
def Check():
    if len(A)<=r or len(A[0])<=c or A[r][c]!=k:return 1
    return 0
r,c,k=map(int,input().split())
r-=1;c-=1
A=[[int(x)for x in input().split()]for y in range(3)]
C=0
while Check():
    if C>100:C=-1;break
    tmp=0
    if len(A)<len(A[0]):tmp=1
    RC(tmp)
    C+=1
print(C)


