import sys
sys.stdin = open('bj16918.txt','r')

def DFS(r,Len,List):
    global R
    if Len==1:
        R=max(R,r)
        return
    for i in range(1,Len):
        DFS(r+(List[i-1]*List[i+1]),Len-1,List[:i]+List[i+1:])
N=int(input())
L=[int(x)for x in input().split()]
R=0
DFS(0,len(L)-1,L)
print(R)