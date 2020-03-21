import sys
sys.stdin = open('test.txt','r')

N=int(input())
L=set(input()for _ in range(N))
for s in sorted(list(L),key=lambda x:(len(x),x)):print(s)