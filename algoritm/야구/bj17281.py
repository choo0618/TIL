import sys
sys.stdin = open('bj17281.txt','r')

def baseball(List):
    global R
    List.insert(3,0)
    n,r=0,0
    Len=len(Set)
    T=[]
    for _ in range(N):
        for j in List:
            T.append(A[_][j])
    Set.add(tuple(T))
    if Len==len(Set):List.pop(3);return
    for i in range(N):
        o,g=0,[1,0,0,0]
        while o!=3:
            t=A[i][List[n]]
            if not t:o+=1
            elif t==1:r+=g.pop();g.insert(0,1)
            elif t==2:r+=sum(g[2:4]);g=[1, 0]+g[0:2]
            elif t==3:r+=sum(g[1:4]);g=[1,0,0,1]
            else:r+=sum(g);g=[1,0,0,0]
            n+=1
            if n==9:n=0
    List.pop(3)
    R=max(R,r)
def DFS(cnt,List):
    if cnt==8:
        baseball(List)
        return
    for i in range(1,9):
        if not Map[i]:
            Map[i]=1
            List.append(i)
            DFS(cnt+1,List)
            Map[i]=0
            List.pop()
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Map=[0]*9
R=0
Set=set()
DFS(0,[])
print(R)
