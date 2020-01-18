import sys
sys.stdin = open('bj1091.txt','r')

def check(List):
    for i in range(0,len(List),3):
        if List[i:i+3]!=(0,1,2):return False
    return True
def solve():
    N=int(input())
    P=tuple(int(x)for x in input().split())
    S=tuple(int(x)for x in input().split())
    C=set()
    C.add(P)
    while not check(P):
        r=[0]*N
        for i in range(N):r[S[i]]=P[i]
        P=tuple(r)
        if P in C:return -1
        C.add(P)
    return len(C)-1
print(solve())
