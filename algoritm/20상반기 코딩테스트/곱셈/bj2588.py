import sys
sys.stdin = open('bj2588.txt','r')

A=int(input())
R=[A*int(b) for b in map(int,input())]
print(R[2])
print(R[1])
print(R[0])
print(R[2]+10*R[1]+100*R[0])

A,B=map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

A,B=map(int,input().split())
print('<' if A<B else '>' if A>B else '==')

N=int(input())
print(1 if (not N%4 and N%100) or not N%400 else 0)