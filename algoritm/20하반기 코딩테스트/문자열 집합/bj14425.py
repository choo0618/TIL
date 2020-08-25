import sys
sys.stdin = open("bj14425.txt",'r')

from collections import defaultdict
def Insert(word):
    Cur=Dic[len(word)]
    for c in word:
        if not c in Cur:Cur[c]={}
        Cur=Cur[c]
def Find(word):
    Cur=Dic[len(word)]
    for c in word:
        if not c in Cur:return 0
        Cur=Cur[c]
    return 1
N,M=map(int,input().split())
Dic=defaultdict(dict)
for _ in range(N):Insert(input())
R=0
for _ in range(M):R+=Find(input())
print(R)