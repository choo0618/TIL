import sys
sys.stdin = open('bj17140.txt','r')

def R():
    Len,Max,LL=len(A),0,[]
    Map=[[]for _ in range(Len)]
    for idx,l in enumerate(A):
        Dic,M={},0
        for j in l:
            if not j:continue
            if j in Dic:Dic[j]+=1
            else:Dic[j]=1
        L=sorted(Dic.items(),key=lambda x:(x[1],x[0]))
        for a,b in L:
            Map[idx]+=[a,b]
            M+=2
            if M==100:break
        LL.append(M)
        Max=max(Max,M)
    for i in range(Len):A[i]=Map[i]+[0]*(Max-LL[i])
def C():
    global A
    A=list(map(list, zip(*A[::-1])))
    R()
    A=list(map(list, zip(*A[::1])))
def Check():
    if len(A)<=r or len(A[0])<=c or A[r][c]!=k:return 1
    return 0
r,c,k=map(int,input().split())
r-=1;c-=1
A=[[int(x)for x in input().split()]for y in range(3)]
Re=0
while Check():
    if Re>100:Re=-1;break
    if len(A)>=len(A[0]):R()
    else:C()
    Re+=1
print(Re)