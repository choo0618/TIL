import sys
sys.stdin = open('test.txt','r')

for t in range(int(input())):
    A,B=map(int,input().split())
    L=A*B
    while B:A,B=B,A%B
    print(L//A)