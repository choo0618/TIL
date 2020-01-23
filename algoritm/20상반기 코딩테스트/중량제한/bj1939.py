import sys
sys.stdin=open('bj1939.txt','r')

def BFS(k):
    Que=[S]
    Map=[0]*(N+1)
    Map[S]=1
    while Que:
        Q=[]
        for q in Que:
            if q==E:return True
            for i in Dic[q]:
                if k<=i[1] and not Map[i[0]]:
                    Map[i[0]]=1
                    Q.append(i[0])
        Que=Q
    return False
N,M=map(int,input().split())
Left,Right=0,0
Dic={}
for i in range(M):
    x,y,k=map(int,input().split())
    try:Dic[x].append((y,k))
    except:Dic[x]=[];Dic[x].append((y,k))
    try:Dic[y].append((x,k))
    except:Dic[y]=[];Dic[y].append((x,k))
    Right=max(Right,k)
S,E=map(int,input().split())
while Left<=Right:
    mid=(Left+Right)//2
    if BFS(mid):Left=mid+1
    else:Right=mid-1
print(Right)


