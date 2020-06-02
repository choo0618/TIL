import sys
sys.stdin = open('bj8901.txt','r')

for t in range(int(input())):
    a,b,c=map(int,input().split())
    A,B,C=map(int,input().split())
    R=0
    for i in range(min(a,b)+1):
        for j in range(min(b-i,c)+1):
            k=min(a-i,c-j)
            R=max(R,A*i+B*j+C*k)
    print(R)