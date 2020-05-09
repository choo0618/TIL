import sys
sys.stdin = open('bj3040.txt','r')

def DFS(idx,n,r,List):
    global C
    if r>100:return
    if n==7:
        if r==100:
            for p in List:print(p)
        return
    for i in range(idx,9):
        List.append(L[i])
        DFS(i+1,n+1,r+L[i],List)
        List.pop()
L=[int(input())for _ in range(9)]
DFS(0,0,0,[])

L=[int(input())for _ in range(9)]
S=sum(L)
for i in range(9):
    for j in range(i+1,9):
        if L[i]+L[j]+100==S:
            for k in range(9):
                if k!=i and k!=j:print(L[k])
            break