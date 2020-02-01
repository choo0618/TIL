import sys
sys.stdin = open('bj1759.txt','r')

def DFS(idx,l,a,b):
    if a+b==L and a>=1 and b>=2:
        print(''.join(l))
        return
    for i in range(idx,C):
        l.append(List[i])
        if List[i] in 'aeiou':DFS(i+1,l,a+1,b)
        else:DFS(i+1,l,a,b+1)
        l.pop()
L,C=map(int,input().split())
List=list(map(str,input().split()))
List.sort()
DFS(0,[],0,0)